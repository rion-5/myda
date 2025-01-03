# src/data/analyze.py
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.append(project_root)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(y_test, y_pred, y_pred_proba):
    """
    모델 성능 평가 지표 계산
    Args:
        y_test: 실제 값
        y_pred: 예측 값
        y_pred_proba: 예측 확률
    Returns:
        dict: 다양한 성능 평가 지표
    """
    from sklearn.metrics import confusion_matrix, classification_report
    
    results = {
        'confusion_matrix': confusion_matrix(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, y_pred_proba)
    }
    return results


def perform_analysis(processed_data: pd.DataFrame):
    """
    GPA와 TOEIC 점수가 취업여부에 미치는 영향 분석
    Args:
        processed_data: 전처리된 데이터프레임
    Returns:
        dict: 분석 결과
    """
    # 필요한 feature만 선택
    X = processed_data[['GPA', 'TOEIC_score']]
    y = processed_data['employ_status']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 로지스틱 회귀 모델 학습
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # 예측 및 성능 평가
    y_pred = model.predict(X_test)
    y_pred_prob = model.predict_proba(X_test)[:, 1]

     # 추가된 평가 지표
    evaluation_metrics = evaluate_model(y_test, y_pred, y_pred_prob)

    results = {
        'accuracy': accuracy_score(y_test, y_pred),
        'evaluation_metrics': evaluation_metrics,
        'coefficients': dict(zip(['GPA', 'TOEIC_score'], model.coef_[0])),
        'intercept': model.intercept_[0]
    }
    
    return results

def interpret_results(analysis_results):
    """분석 결과 해석"""
    accuracy = analysis_results['accuracy']
    evaluation_metrics = analysis_results['evaluation_metrics']
    coefficients = analysis_results['coefficients']
    
    print("\n=== 모델 성능 ===")
    print(f"정확도: {accuracy:.2f}")  # 0.7 이상이면 양호
    print(f"ROC-AUC: {evaluation_metrics['roc_auc']:.2f}") # 0.5=랜덤, 0.7이상=양호
    
    print("\n=== Confusion Matrix ===")
    print(evaluation_metrics['confusion_matrix'])
    
    print("\n=== Classification Report ===")
    print(evaluation_metrics['classification_report'])
    
    print("\n=== 특성 영향도 ===")
    for feature, coef in coefficients.items():
        impact = "양의" if coef > 0 else "음의"
        strength = abs(coef)
        print(f"{feature}: {coef:.4f} ({impact} 영향, 강도: {strength:.4f})")
    
    print("\n=== 결론 ===")
    print("1. GPA와 TOEIC 점수가 취업에 미치는 영향:")
    for feature, coef in coefficients.items():
        if abs(coef) > 0.5:
            print(f"- {feature}는 취업에 유의미한 영향을 미침")
        else:
            print(f"- {feature}는 취업에 약한 영향을 미침")

if __name__ == "__main__":
    # Test code
    from src.data.preprocessing import clean_data
    from src.data.make_dataset import collect_data
    
    raw_data = collect_data()
    processed_data = clean_data(raw_data)
    analysis_results = perform_analysis(processed_data)
    
    print("\n분석 결과:")
    print(analysis_results)
    
    interpret_results(analysis_results)
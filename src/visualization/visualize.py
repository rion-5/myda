import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_visualizations(processed_data: pd.DataFrame):
    """Create multiple visualizations for analysis"""
    
    # employ_status를 문자열 레이블로 변환
    status_map = {0: 'Unemployed', 1: 'Employed'}  # 또는 한글로: {0: '미취업', 1: '취업'}
    processed_data['employ_status_label'] = processed_data['employ_status'].map(status_map)
    
    # 산점도 생성
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=processed_data,
                   x='GPA',
                   y='TOEIC_score',
                   hue='employ_status_label',  # 레이블 사용
                   alpha=0.6)
    plt.title('GPA vs TOEIC Score by Employment Status')
    plt.savefig('reports/figures/employment_analysis.png')
    plt.close()
    
    # 분포도 추가
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # GPA 분포
    sns.boxplot(data=processed_data, 
                x='employ_status_label',  # 레이블 사용
                y='GPA', 
                ax=ax1,
                order=['Unemployed', 'Employed'])  # 순서 지정
    ax1.set_title('GPA Distribution by Employment Status')
    
    # TOEIC 분포
    sns.boxplot(data=processed_data, 
                x='employ_status_label',  # 레이블 사용
                y='TOEIC_score', 
                ax=ax2,
                order=['Unemployed', 'Employed'])  # 순서 지정
    ax2.set_title('TOEIC Distribution by Employment Status')
    
    plt.tight_layout()
    plt.savefig('reports/figures/distributions.png')
    plt.close()
import os
import pandas as pd
import numpy as np
from src.data.make_dataset import collect_data
from src.data.preprocessing import clean_data
from src.analysis.analyze import perform_analysis, interpret_results
from src.visualization.visualize import create_visualizations

def main():
    # 데이터 수집
    def setup_project_structure():
        """프로젝트 디렉토리 구조 자동 생성"""
        directories = [
            'data/raw',
            'data/processed',
            'data/external',
            'notebooks',
            'src/data',
            'src/analysis',
            'src/visualization',
            'reports/figures'
        ]
        for dir_path in directories:
            os.makedirs(dir_path, exist_ok=True)
    
    # 프로젝트 초기 설정
    setup_project_structure()
    
    # 데이터 수집
    raw_data = collect_data()
    
    # 데이터 전처리
    processed_data = clean_data(raw_data)

    # print(processed_data)
    # # 처리된 데이터에서 특정 컬럼 20개 출력
    # columns_to_show = ['GPA', 'TOEIC_score','company_name','department', 'employment_type', 'employ_status']
    # print("\n선택된 컬럼 20개 데이터:")
    # print(processed_data[columns_to_show].head(20))


    # # 데이터 분석
    analysis_results = perform_analysis(processed_data)

   # 분석 결과 출력
    print("\n분석 결과:")
    print(analysis_results)
    
    interpret_results(analysis_results)
    
    # 시각화
    create_visualizations(processed_data)
    
    # 결과 저장
    results_df = pd.DataFrame([analysis_results])
    results_df.to_csv('reports/analysis_results.csv', index=False)

if __name__ == '__main__':
    main()
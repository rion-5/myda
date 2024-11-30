#main.py

import os
import pandas as pd
import numpy as np
import logging
from src.data.make_dataset import collect_data_db, collect_data
from src.data.preprocessing import clean_data
from src.analysis.analyze import perform_analysis, interpret_results
from src.visualization.visualize import create_visualizations
from src.utils.logger import setup_logger

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
        'reports/figures',
        'logs'  # 추가된 부분
    ]
    
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)

def main():
    # 로거 설정
    setup_logger()
    logger = logging.getLogger(__name__)
    
    # 프로젝트 초기 설정
    setup_project_structure()
    logger.info("프로젝트 구조 설정 완료")
    
    # 데이터 수집
    # raw_data = collect_data_db()
    raw_data = collect_data()
    logger.info("데이터 수집 완료")
    
    # 데이터 전처리
    processed_data = clean_data(raw_data)
    logger.info("데이터 전처리 완료")

    # 데이터 분석
    analysis_results = perform_analysis(processed_data)
    logger.info("데이터 분석 완료")

    # 분석 결과 출력
    print("\n분석 결과:")
    print(analysis_results)
    
    interpret_results(analysis_results)
    
    # 시각화
    create_visualizations(processed_data)
    logger.info("시각화 완료")
    
    # 결과 저장
    results_df = pd.DataFrame([analysis_results])
    results_df.to_csv('reports/analysis_results.csv', index=False)
    logger.info("결과 저장 완료")

if __name__ == '__main__':
    main()
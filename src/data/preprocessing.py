# preprocessing.py
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.append(project_root)

import numpy as np
import pandas as pd
from typing import List
from psycopg2.extras import RealDictRow

def clean_data(raw_data: List[RealDictRow]) -> pd.DataFrame:
    """
    데이터 전처리 수행
    Args:
        raw_data: RealDictRow 객체 리스트
    Returns:
        pd.DataFrame: 전처리된 데이터프레임
    """
    df = pd.DataFrame(raw_data)
    
    # 1. 외국인학생 이진값 변환
    df['외국인학생'] = df['외국인학생'].map({'예': 1, '아니오': 0})
    
    # 2. 교환유학생여부 이진값 변환
    df['교환유학생여부'] = df['교환유학생여부'].map({'예': 1, '아니오': 0})
    
    # 3. 졸업년월 datetime으로 변환
    df['졸업년월'] = pd.to_datetime(df['졸업년월'].astype(str), format='%Y.%m')
    
    # 4. 평점평균 숫자형으로 변환
    df['평점평균'] = pd.to_numeric(df['평점평균'], errors='coerce')
    
    # 5. 토익점수 숫자형으로 변환
    df['토익점수'] = pd.to_numeric(df['토익점수'], errors='coerce')
    
    # 6. 회사명, 부서, 근무지의 빈 문자열을 NaN으로 변환
    df['회사명'] = df['회사명'].replace('', pd.NA)
    df['부서'] = df['부서'].replace('', pd.NA)

    # 7. employ_status 컬럼 추가 (취업여부)
    df['employ_status'] = np.where(
        df['취업구분'].isin(['기타', '선택', '미상']), 
        0, 
        1
    )
    
    # Define column mapping dictionary
    column_mapping = {
        '학과명': 'major',
        '성별': 'gender',
        '졸업년월': 'graduation_date',
        '출신고교': 'high_school',
        '외국인학생': 'foreign_student',
        '회사명': 'company_name',
        '부서': 'department',
        '근무지': 'workplace',
        '평점평균': 'GPA',
        '입학전형명': 'admission_type',
        '토익점수': 'TOEIC_score',
        '교환유학생여부': 'exchange_student',
        '취업구분': 'employment_type'
    }

    # Rename columns in the clean_data function
    df = df.rename(columns=column_mapping)

    # 8. Remove rows where TOEIC_score is NaN
    df = df.dropna(subset=['TOEIC_score'])


    return df

if __name__ == "__main__":
    from src.data.make_dataset import collect_data
    
    raw_data = collect_data()
    processed_df = clean_data(raw_data)
    
    # Debug prints
    print("\nData Info:")
    print(processed_df.info())
    print("\nMissing Values:")
    print(processed_df.isnull().sum())
    

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor  # 이 부분 추가
from .database import get_db_connection  # 상대 경로 import
# def fetch_stock_data():
#     # 데이터베이스 연결
#     conn = get_db_connection()
    
#     if conn is None:
#         return
    
#     try:
#         # 커서 생성 (딕셔너리 형태로 결과 반환)
#         with conn.cursor(cursor_factory=RealDictCursor) as cursor:
#             # 쿼리 실행
#             cursor.execute("SELECT trading_date symbol, adjusted, volume FROM stock where symbol='TSLA' and trading_date='2024-11-25'")
            
#             # 모든 레코드 가져오기
#             records = cursor.fetchall()
            
#             # 데이터 출력
#             for record in records:
#                 print(record)
    
#     except Exception as e:
#         print(f"쿼리 실행 중 오류 발생: {e}")
    
#     finally:
#         # 연결 종료
#         if conn:
#             conn.close()
#             print("데이터베이스 연결 종료")


def fetch_stock_data():
    conn = get_db_connection()
    
    if conn is None:
        return
    
    try:
        # 일반 커서 사용
        with conn.cursor() as cursor:
            cursor.execute("select 학과명, 성별, 졸업년월, 출신고교, 외국인학생, 회사명,부서, 근무지, 평점평균, 입학전형명, 토익점수, 교환유학생여부, 취업구분 from 취업통계졸업생명단 ")
            
            # 모든 레코드 가져오기
            records = cursor.fetchall()
            
            # 데이터 출력
            for record in records:
                print(record)
    
    except Exception as e:
        print(f"쿼리 실행 중 오류 발생: {e}")
    
    finally:
        if conn:
            conn.close()
            print("데이터베이스 연결 종료")


if __name__ == "__main__":
    fetch_stock_data()
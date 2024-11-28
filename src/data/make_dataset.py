from .database import get_db_connection  # src/data/database.py

def collect_data():
    conn = get_db_connection()
    
    if conn is None:
        return None
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("select 학과명, 성별, 졸업년월, 출신고교, 외국인학생, 회사명,부서, 근무지, 평점평균, 입학전형명, 토익점수, 교환유학생여부, 취업구분 from 취업통계졸업생명단")
            records = cursor.fetchall()
            return records
    
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    
    finally:
        if conn:
            conn.close()

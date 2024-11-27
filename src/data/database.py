import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

# .env 파일 로드
load_dotenv()

# 환경변수에서 DB 접속 정보 가져오기
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print(f"PostgreSQL 연결 중 오류 발생: {error}")
        return None
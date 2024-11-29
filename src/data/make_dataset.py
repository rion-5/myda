from typing import Optional, List, Dict
import logging
from psycopg2.extras import RealDictCursor
from .database import get_db_connection # src/data/database.py

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def collect_data() -> Optional[List[Dict]]:
    """
    Collect data from database in dictionary format
    Returns:
        Optional[List[Dict]]: Database records as list of dictionaries
    """
    conn = get_db_connection()
    
    if conn is None:
        logger.error("Database connection failed")
        return None
    
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            query = """
                SELECT 학과명, 성별, 졸업년월, 출신고교, 외국인학생,
                       회사명, 부서, 근무지, 평점평균, 입학전형명,
                       토익점수, 교환유학생여부, 취업구분
                FROM 취업통계졸업생명단
            """
            cursor.execute(query)
            records = cursor.fetchall()
            logger.info(f"Retrieved {len(records)} records")
            return records
            
    except Exception as e:
        logger.error(f"Query execution error: {e}")
        return None
        
    finally:
        if conn:
            conn.close()

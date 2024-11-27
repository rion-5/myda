import pandas as pd
from sqlalchemy import text
from .database import DatabaseConnection

class DataLoader:
    def __init__(self):
        self.db_conn = DatabaseConnection()

    def load_table_to_dataframe(self, table_name, query=None):
        """
        Load table or custom query result to pandas DataFrame
        
        :param table_name: Name of the table to load
        :param query: Optional custom SQL query
        :return: pandas DataFrame
        """
        try:
            session = self.db_conn.get_session()
            
            if query is None:
                query = f"SELECT * FROM {table_name}"
            
            df = pd.read_sql(text(query), session.bind)
            session.close()
            
            return df
        
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def save_dataframe_to_table(self, df, table_name, if_exists='replace'):
        """
        Save pandas DataFrame to PostgreSQL table
        
        :param df: pandas DataFrame
        :param table_name: Target table name
        :param if_exists: Action if table exists ('fail', 'replace', 'append')
        """
        try:
            df.to_sql(table_name, self.db_conn.engine, if_exists=if_exists, index=False)
            print(f"DataFrame saved to {table_name}")
        except Exception as e:
            print(f"Error saving DataFrame: {e}")


    def execute_query_to_dataframe(self, query):
        """
        Execute SQL query and return results as a pandas DataFrame
        
        :param query: SQL query to execute
        :return: pandas DataFrame with query results
        """
        try:
            session = self.db_conn.get_session()
            
            # 쿼리 실행 및 결과를 DataFrame으로 변환
            df = pd.read_sql(text(query), session.bind)
            session.close()
            
            return df
        
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def execute_write_query(self, query):
        """
        Execute a write query (INSERT, UPDATE, DELETE)
        
        :param query: SQL write query to execute
        :return: Number of affected rows
        """
        try:
            session = self.db_conn.get_session()
            
            # 쿼리 실행
            result = session.execute(text(query))
            session.commit()
            session.close()
            
            return result.rowcount
        
        except Exception as e:
            print(f"Error executing write query: {e}")
            return None    
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Load environment variables
load_dotenv()

class DatabaseConnection:
    def __init__(self, db_url=None):
        """
        Initialize database connection
        
        :param db_url: Optional database URL. If not provided, uses environment variables
        """
        if not db_url:
            db_url = self._construct_db_url()
        
        try:
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)
        except SQLAlchemyError as e:
            print(f"Error connecting to database: {e}")
            raise

    def _construct_db_url(self):
        """
        Construct database URL from environment variables
        
        :return: SQLAlchemy compatible database URL
        """
        DB_USER = os.getenv('DB_USER', 'postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = os.getenv('DB_PORT', '5432')
        DB_NAME = os.getenv('DB_NAME', 'mydatabase')

        return f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    def get_session(self):
        """
        Get a database session
        
        :return: SQLAlchemy session
        """
        return self.Session()

    def test_connection(self):
        """
        Test database connection
        
        :return: Boolean indicating connection status
        """
        try:
            with self.engine.connect() as connection:
                return True
        except SQLAlchemyError:
            return False
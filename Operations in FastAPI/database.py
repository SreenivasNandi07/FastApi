
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "mysql+pymysql://root@localhost/fastapi_db"
engine = create_engine()
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

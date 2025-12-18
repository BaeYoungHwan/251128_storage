from db.connection import get_engine

engine = get_engine()

with engine.connect() as conn:
    print("PostgreSQL 연결 성공!")

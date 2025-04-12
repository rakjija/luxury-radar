from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DB 연결 정보 (개발용)
DATABASE_URL = "mysql+pymysql://luxury_user:password@localhost:3306/luxury"

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"charset": "utf8mb4"},
)

# 세션 팩토리 설정
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 모델 정의를 위한 Base 클래스
Base = declarative_base()

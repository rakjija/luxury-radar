from crawler import models
from crawler.db import Base, engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully.")

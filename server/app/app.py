import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    print("Here")
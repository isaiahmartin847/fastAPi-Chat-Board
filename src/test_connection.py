from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine




URL_database = "mysql+pymysql://developer:Developer1*@localhost:3306/Lagoon_test"
                



engine = create_engine(URL_database)

with engine.connect() as connection:
    result = connection.execute("SELECT 'Hello, world!'")
    for row in result:
        print(row)
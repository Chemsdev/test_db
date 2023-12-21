import pandas as pd
from sqlalchemy import create_engine

def connect_mysql(host, user, password, database):
    engine   = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine.connect()


engine = connect_mysql(
    host="stackoverflow.mysql.database.azure.com", 
    user="chemsdine", 
    password="simplon123@", 
    database="stackoverflow"
)

data = {
    "idu": [1],
    "Title": ["123"],
    "Body": ["azaz"],
}

table = pd.DataFrame(data)
table.to_sql('selmanelegrandfou', engine, if_exists='append', index=False)
engine.close()
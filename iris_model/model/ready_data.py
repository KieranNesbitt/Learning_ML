import pandas as pd
from sqlite3 import connect
from sklearn.preprocessing import OneHotEncoder
db_uri = 'Learning_ML\iris_model\sql_db\iris.db'
def get_data(conn):
    iris_db = hot_encoding(pd.read_sql("SELECT * FROM Iris_database;", conn))
    return iris_db

def hot_encoding(iris_db):
    flower_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    one_hot_encoded_data = one_hot_encoder.fit_transform(iris_db[['encoded_class']])
    one_hot_db = pd.DataFrame(one_hot_encoded_data, columns=flower_names)
    return pd.concat([iris_db.drop("encoded_class", axis=1), one_hot_db], axis=1)

def create_encoding_and_split():
    conn = connect(db_uri)
    new_db = get_data(conn)
    new_db.to_sql(name = "Iris_database", con=conn, if_exists="replace")
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='Iris_database';")
    schema = cursor.fetchone()[0]
    print("\nSQL Schema for Iris_database:")
    print(schema)

    conn.close()

create_encoding_and_split()
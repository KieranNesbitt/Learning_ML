from sklearn.datasets import load_iris
import pandas as pd
import sqlite3
data = load_iris()

data_dic = {"sepal_length": data.data[:,0], "sepal_width": data.data[:,1], "petal_length": data.data[:,2], "peta_width": data.data[:,3], "encoded_class": data.target}
iris_dataframe = pd.DataFrame(data=data_dic)
iris_dataframe["flower_id"] = iris_dataframe.index +1
db_uri = 'Learning_ML\iris_model\sql_db\iris.db'

with sqlite3.connect(db_uri) as con:
    iris_dataframe.to_sql('Iris_database', con=con, dtype={'flower_id': 'INTEGER PRIMARY KEY'}, if_exists="replace" , index =False)
    cursor = con.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='Iris_database';")
    schema = cursor.fetchone()[0]
    print("\nSQL Schema for Iris_database:")
    print(schema)
    con.close

    
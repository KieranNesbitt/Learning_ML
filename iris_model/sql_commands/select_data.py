import sqlite3
import pandas as pd
db_uri = r'Learning_ML\iris_model\sql_db\iris.db'

def select_data(column_name: str = "*") -> pd.DataFrame:
    """
    function is used to grab the whole database for ingress into model
    """
    query_string = f"SELECT {column_name} FROM Iris_database;"
    with sqlite3.connect(db_uri) as con:
        cursor = con.cursor()
        query_result = cursor.execute(query_string)
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        
        query = cursor.fetchall()
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        
        return pd.DataFrame(query, columns=field_names)

def show_table(): # Used for trouble shooting
    query_string = f"SELECT * FROM Iris_database;"
    with sqlite3.connect(db_uri) as con:
        conn = sqlite3.connect(db_uri)
        cursor = con.cursor()
        
        print(cursor.description)
        quesry_result = cursor.fetchall()
        print(pd.DataFrame(quesry_result))


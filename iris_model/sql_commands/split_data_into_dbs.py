import sqlite3
import os

db_uri = 'Learning_ML\iris_model\sql_db\iris.db'


with sqlite3.connect(db_uri) as con:
    cursor = con.cursor()
    print(f"Successfully connected to database at: {db_uri}")

    cursor.execute("DROP TABLE IF EXISTS iris_train_data;")
    cursor.execute("DROP TABLE IF EXISTS iris_test_data;")

    cursor.execute("""
    CREATE TABLE iris_train_data AS
    SELECT
        sepal_length,
        sepal_width,
        petal_length,
        petal_width,
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica"
    FROM
        Iris_database
    WHERE
        RANDOM() % 100 < 80;
    """)

    cursor.execute("""
    CREATE TABLE iris_test_data AS
    SELECT
        sepal_length,
        sepal_width,
        petal_length,
        petal_width,
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica"
    FROM
        Iris_database
    WHERE
        RANDOM() % 100 >= 80;
    """)

    con.commit()
    print("Train and Test tables created successfully within the database file.")

    cursor.execute("SELECT COUNT(*) FROM iris_train_data;")
    train_count = cursor.fetchone()[0]
    print(f"Number of rows in iris_train_data: {train_count}")

    cursor.execute("SELECT COUNT(*) FROM iris_test_data;")
    test_count = cursor.fetchone()[0]
    print(f"Number of rows in iris_test_data: {test_count}")

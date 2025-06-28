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
    iris_db
WHERE
    RANDOM() % 100 < 80; -- RANDOM() returns a large integer, so use modulo

-- Create Test Data Table (20%)
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
    iris_db
WHERE
    RANDOM() % 100 >= 80;
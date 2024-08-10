'''
python script to run experiments using mlflow on spark compute
'''

import mlflow.spark
import os
import shutil
from pyspark.sql import SparkSession

# Create and persist some dummy data
# Note: On environments like Databricks with pre-created SparkSessions,
# ensure the org.mlflow:mlflow-spark:2.22.0 is attached as a library to
# your cluster
spark = SparkSession.builder.appName("TestMlFlow").master("spark://192.168.1.14:7077").getOrCreate()


loaded_df = spark.read.csv(
    '/home/saurabhk/Downloads/books_task.csv', header=True, inferSchema=True
)
# Call toPandas() to trigger a read of the Spark datasource. Datasource info
# (path and format) is logged to the current active run, or the
# next-created MLflow run if no run is currently active
with mlflow.start_run() as active_run:
    pandas_df = loaded_df.toPandas()

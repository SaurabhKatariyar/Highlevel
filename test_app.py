from pyspark.sql import SparkSession

# Replace with your Spark master URL
spark = SparkSession.builder.appName("SimplePySparkJob").master("spark://192.168.1.14:7077").getOrCreate()


# Create a simple DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29), ("David", 35)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Perform a simple transformation
df_transformed = df.withColumn("Age Next Year", df["Age"] + 1)

# Show the transformed DataFrame


# Perform an action to trigger execution
count = df_transformed.count()
print(f"Total records: {count}")
print(df_transformed.show())

# Stop the Spark session
spark.stop()

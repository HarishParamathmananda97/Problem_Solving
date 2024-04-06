from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum

# file = r"C:\Users\harish\Documents\Euroclear\Euroclear\CAREF.2024022001.txt"
file = r"\\ferack50\FEProcess\FairValue\Processed_Files\Testing_\2024\Feb-2024\19 feb\RD\USD\USD\Input\BondsCleanPrices_19Feb24.csv"

# Create a Spark session
spark = SparkSession.builder \
    .appName("ReadTextFile") \
    .getOrCreate()

# Read data from txt file into a DataFrame
df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .load(file)

# Perform transformations
# Filter data for a specific condition
filtered_df = df.filter(col("column_name") == "value")

# Group by a column and count the occurrences
grouped_df = filtered_df.groupBy("group_column").agg(count("*").alias("count"))

# Perform aggregation
aggregated_df = grouped_df.groupBy("group_column").agg(sum("count").alias("total_count"))

# Write the result to a Parquet file
aggregated_df.write \
    .format("parquet") \
    .mode("overwrite") \
    .save("result.parquet")

# Stop the Spark session
spark.stop()

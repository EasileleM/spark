from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, count

# Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)

# Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)

student_data_filename = "student_data.csv"
spark = SparkSession.builder.appName("Test").master("spark://192.168.128.7:7077").getOrCreate()

student_data = spark.read \
    .option("header", True) \
    .csv(student_data_filename) \
    .select("medu", "fedu", "g3", "dalc", "walc") \
    .repartition(6) \
    .groupBy("medu", "fedu") \
    .agg(mean('g3'), count("*"), mean('dalc'), mean('walc'))

student_data.show()

student_data \
    .repartition(1) \
    .write \
    .option("header", "true") \
    .csv("result")

spark.stop()

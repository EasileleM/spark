from pyspark.sql import SparkSession
from pyspark.sql.functions import mean

student_data_filename = "/tasks/bruteforce/student_data.csv"
spark = SparkSession.builder.appName("Test").master("spark://172.24.0.8:7077").getOrCreate()

student_data = spark.read \
    .option("header", True) \
    .csv(student_data_filename) \
    .select("medu", "fedu", "g3") \
    .repartition(6) \
    .groupBy("medu", "fedu") \
    .agg(mean('g3')) \
    .repartition(1) \
    .write \
    .option("header", "true") \
    .csv("/tasks/bruteforce/result")

spark.stop()

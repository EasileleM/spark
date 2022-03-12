from pyspark.sql import SparkSession

file = "/tasks/bruteforce/text.md"
spark = SparkSession.builder.appName("Test").master("spark://172.24.0.7:7077").getOrCreate()
data = spark.read.text(file).cache()

numAs = data.filter(data.value.contains("a")).count()
numBs = data.filter(data.value.contains("b")).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()

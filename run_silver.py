exec(open("/home/onyxia/work/ece-bigdata-2026/spark_setup.py").read())
spark.conf.set("spark.sql.shuffle.partitions", "4")
exec(open("/home/onyxia/work/ece-bigdata-2026/silver.py").read())

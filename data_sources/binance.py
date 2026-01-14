import requests
import json
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

# creating spark session
spark = SparkSession.builder.getOrCreate()

# def get_binance_price(symbol="BTCUSDT"):
url = f'https://api.bybit.com/v5/market/funding/history?category=linear&symbol=BTCUSDT'


data = requests.get(url).json()

# the above data is nested json

df = spark.read.json(spark.sparkContext.parallelize([data]))
print(df)

# flattening json
df_flat = df.withColumn("row",explode(col("result.list"))).select(
    col("retCode"),
    col("retMsg"),
    col("result.category").alias("category"),
    col("row.symbol").alias("symbol"),
    col("row.fundingRate").cast("double").alias("Funding_rate"),
    col("row.fundingRateTimestamp").cast("long").alias("funding_rate_timestamp"),
    col("time").alias("ingestion_time")

)

df_pandas =  df_flat.toPandas()
df_pandas["ingestion_time"] = pd.to_datetime(df_pandas["ingestion_time"], errors="coerce")
df_pandas["funding_rate_timestamp"] = pd.to_datetime(
df_pandas["funding_rate_timestamp"], errors = "coerce"
                                                     )
print(df_pandas)

import pandas as pd


PATH = "s3://bruno-lastfm-datalake/processed/silver/geo_top_tracks.parquet"

df = pd.read_parquet(PATH)

print(df.head())
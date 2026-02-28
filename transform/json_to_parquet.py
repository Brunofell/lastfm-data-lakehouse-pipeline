from list_s3 import list_files, read_json_from_s3
import json
import pandas as pd

chart_top_tracks = "raw/lastfm/get_chart_top_tracks/2026/02/15/"
chart_top_artists = "raw/lastfm/get_chart_top_artists/2026/02/15/"
geo_top_artists = "raw/lastfm/get_geo_top_artists/2026/02/15/"
geo_top_tracks = "raw/lastfm/get_geo_top_tracks/2026/02/15/"

file1 = list_files(chart_top_tracks)
file2 = list_files(chart_top_artists)
file3 = list_files(geo_top_artists)
file4 = list_files(geo_top_tracks)

data1 = read_json_from_s3(file1[0])
data2 = read_json_from_s3(file2[0])
data3 = read_json_from_s3(file3[0])
data4 = read_json_from_s3(file4[0])

# print(data1.keys())
# print(data1)
# print(json.dumps(data1, indent=2))

data1_list = data1["tracks"]["track"]
data2_list = data2["artists"]["artist"]
data3_list = data3["topartists"]["artist"]
data4_list = data4["tracks"]["track"]


## PANDAS

df_chart_top_tracks = pd.DataFrame(data1_list)
df_chart_top_artists = pd.DataFrame(data2_list)
df_geo_top_artists = pd.DataFrame(data3_list)
df_geo_top_tracks = pd.DataFrame(data4_list)

# pro parquet funcionar baixar isso: pip install pyarrow

df_chart_top_tracks.to_parquet(
    "data/chart_top_tracks.parquet",
    index=False
    )

df_chart_top_artists.to_parquet(
    "data/chart_top_artists.parquet",
    index=False
    )

df_geo_top_artists.to_parquet(
    "data/geo_top_artists.parquet",
    index=False
    )

df_geo_top_tracks.to_parquet(
    "data/geo_top_tracks.parquet",
    index=False
    )

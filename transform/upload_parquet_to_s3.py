import boto3

s3 = boto3.client("s3")
BUCKET = "bruno-lastfm-datalake"

def upload_to_s3(local_path, s3_path):
    s3.upload_file(
        local_path,
        BUCKET,
        s3_path
    )
    print("upload OK!!")
    
    
chart_top_artists_file = "data/chart_top_artists.parquet"
chart_top_tracks_file = "data/chart_top_tracks.parquet"
geo_top_artists_file = "data/geo_top_artists.parquet"
geo_top_tracks_file = "data/geo_top_tracks.parquet"

s3_key_chart_top_artists = "processed/bronze/chart_top_artists.parquet"
s3_key_chart_top_tracks = "processed/bronze/chart_top_tracks.parquet"
s3_key_geo_top_artists = "processed/bronze/geo_top_artists.parquet"
s3_key_geo_top_tracks = "processed/bronze/geo_top_tracks.parquet"

upload_to_s3(chart_top_artists_file, s3_key_chart_top_artists)
upload_to_s3(chart_top_tracks_file, s3_key_chart_top_tracks)
upload_to_s3(geo_top_artists_file, s3_key_geo_top_artists)
upload_to_s3(geo_top_tracks_file, s3_key_geo_top_tracks)


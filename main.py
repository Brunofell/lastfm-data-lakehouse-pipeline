from extract.lastfm_client import get_chart_top_artists
from extract.lastfm_client import get_chart_top_tracks
from extract.lastfm_client import get_geo_top_artists
from extract.lastfm_client import get_geo_top_tracks
from load.s3_raw_loader import upload_json 

data_get_chart_top_artists = get_chart_top_artists()
data_get_chart_top_tracks = get_chart_top_tracks()
data_get_geo_top_artists = get_geo_top_artists()
data_get_geo_top_tracks = get_geo_top_tracks()

upload_json(data_get_chart_top_artists, "get_chart_top_artists")
upload_json(data_get_chart_top_tracks, "get_chart_top_tracks")
upload_json(data_get_geo_top_artists, "get_geo_top_artists")
upload_json(data_get_geo_top_tracks, "get_geo_top_tracks")
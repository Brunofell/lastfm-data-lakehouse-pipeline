import boto3
import json
# create client s3
s3 = boto3.client("s3")
BUCKET = "bruno-lastfm-datalake" # mudar para var de ambiente

# buscar arquivos no bucket

def list_files(prefix):
    response = s3.list_objects_v2(
        Bucket=BUCKET,
        Prefix=prefix
    )
    if "Contents" not in response:
        return []
    
    files = []
    
    for obj in response["Contents"]:
        files.append(obj["Key"])
        
    return files

# files = list_files("raw/lastfm/get_chart_top_artists/")
# print(files)


def read_json_from_s3(key):
    response = s3.get_object(
        Bucket=BUCKET,
        Key=key
    )
    content = response["Body"].read().decode("utf-8")
    
    data = json.loads(content)
    
    return data


# files = list_files("raw/lastfm/get_chart_top_tracks/2026/02/15/") # s3://bruno-lastfm-datalake/raw/lastfm/get_chart_top_tracks/2026/02/15/
# if(len(files) > 0):
#     key = files[0]
#     data = read_json_from_s3(key)
#     print(data)

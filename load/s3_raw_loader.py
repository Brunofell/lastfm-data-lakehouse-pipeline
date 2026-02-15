import boto3
import json
from datetime import datetime
import time

s3 = boto3.client("s3")

BUCKET = "bruno-lastfm-datalake"

def upload_json(data, folder):

    print("Starting upload to S3...")
    
    # manter controle da data
    today = datetime.now().strftime("%Y/%m/%d")
    timestamp = datetime.now().strftime("%H%M%S")
    
    # caminho para criação do arquivo
    key = f"raw/lastfm/{folder}/{today}/data_{timestamp}.json" # particionamento por data pra fazer consulta no athena
    
    # simulating loading, because why not!
    print("Sending...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print()  # line break
    
    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    
    print("Uploaded!")
    
    return key



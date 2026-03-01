import pandas as pd

BRONZE_FILE = "s3://bruno-lastfm-datalake/processed/bronze/geo_top_tracks.parquet"
SILVER_ARCHIVE_PATH = "s3://bruno-lastfm-datalake/processed/silver/geo_top_tracks.parquet"


df = pd.read_parquet(BRONZE_FILE)

# pegar a imagem tamanho large apra incluir no arquivo novo

def get_image(images, size="extralarge"):
    if not isinstance(images, list):
        return None

    for img in images:
        if img.get("size") == size:
            return img.get("#text")

    return None

df["image_large"] = df["image"].apply(get_image)


# Abrir coluna artist

df["artist_name"] = df["artist"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
df["artist_mbid"] = df["artist"].apply(lambda x: x.get("mbid") if isinstance(x, dict) else None)

# converter em tipos numéricos
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")
df["listeners"] = pd.to_numeric(df["listeners"], errors="coerce")


# Selecionar só o que interessa

df_silver = df[[
    "name",
    "duration",
    "listeners",
    "url",
    "artist_name",
    "artist_mbid",
    "image_large"
]]

# renomear

df_silver = df_silver.rename(columns={
    "name": "track_name",
    "duration": "duration_sec",
    "listeners": "listeners_count"
})


# salvar na silver 

df_silver.to_parquet(SILVER_ARCHIVE_PATH, index=False)
print("Geo_Top_Tracks successfully saved in silver layer!!!")
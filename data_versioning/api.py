# Get url from DVC
import pandas as pd
import dvc.api

path='data_versioning/data/wine_original.csv'
repo='./data_versioning'
vnum = 'v3'

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev=vnum
  )

data = pd.read_csv(data_url, sep=";")
print(data)
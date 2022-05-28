import pandas
from gps_extractor import gps_extractor
photos = gps_extractor()
photos.to_csv("photos.csv")

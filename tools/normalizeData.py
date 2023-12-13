import numpy as np
import json
import os
import csv
import pandas as pd

def read_data(path):
  video_data = []
  with open(path, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
      video_data.append(row)
  return video_data

# normalize data according to the size of videos in different dataset
def normalize(list, width, height):
  normalized = []
  for record in list:
    for i in range(0, 54, 3):
        record[i] = float(record[i])/ width
        record[i + 1] = float(record[i + 1]) / height
    normalized.append(record)
  return normalized
    
path = r'C:\Users\sam\Desktop\tem_csv\fall.csv'
data = read_data(path)
normalizedData = normalize(data, 1280, 720)
csvData = pd.DataFrame.from_records(normalizedData)
csvData.to_csv (r'C:\Users\sam\Desktop\tem_csv\fall_train.csv', index = False, header=False)
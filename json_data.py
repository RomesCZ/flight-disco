import json
from datetime import datetime
from datetime import timezone

def getJSONData():
  f = open('data_example.json', 'r')
  jsond = json.load(f)
  json_data = jsond['data']
  return json_data

def formateDateTime(inp):
  return datetime.utcfromtimestamp(inp).strftime("%Y-%m-%d %H:%M")
  #return datetime.utcfromtimestamp(inp)
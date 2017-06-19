import json
from datetime import datetime
from datetime import timezone
import urllib.request

def getJSONDataSample():
  f = open('data_example.json', 'r')
  jsond = json.load(f)
  json_data = jsond['data']
  return json_data

def formateDateTime(inp):
  return datetime.utcfromtimestamp(inp).strftime("%Y-%m-%d %H:%M")
  #return datetime.utcfromtimestamp(inp)
  
def getJSONData(url):
  f = urllib.request.urlopen(url)
  jsond = json.load(f)
  json_data = jsond['data']
  return json_data
  
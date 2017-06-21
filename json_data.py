import json
from datetime import datetime
from datetime import timezone
#import urllib.request
import requests
import logging
logger = logging.getLogger() #main logger

def getJSONDataSample():
  logger.info("getJSONDataSample()")
  f = open('data_example.json', 'r')
  jsond = json.load(f)
  json_data = jsond['data']
  #logger.debug("json_data: {0}".format(json_data))
  return json_data

def formateDateTime(inp):
  #logger.info("formateDateTime(inp):")
  #logger.debug("ret{0}".format(datetime.utcfromtimestamp(inp).strftime("%Y-%m-%d %H:%M")))
  return datetime.utcfromtimestamp(inp).strftime("%Y-%m-%d %H:%M")
  #return datetime.utcfromtimestamp(inp)
  
def getJSONData(url):
  logger.info("getJSONData(url):")
  r = requests.get(url)
  logger.info("r.status_code {0}".format(r.status_code))
  r.raise_for_status()
  jsond = r.json()
  json_data = jsond['data']
  return json_data
  
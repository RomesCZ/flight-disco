from pathlib import Path
from openpyxl import Workbook, load_workbook
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
  filename='__DEBUG.log',level=logging.DEBUG)
  
#vrati existujici nebo vytvori novej
def getExcelFile(fileName):
  if Path(fileName).exists():
    logging.debug('loading file: {0}'.format(fileName))
    wb = load_workbook(fileName)
  else:
    logging.debug('creating file: {0}'.format(fileName))
    wb = Workbook()
  ws = wb.create_sheet(index=0)
  ws.sheet_properties.tabColor = "1072BA"
  return wb
###

def generateHeader(ws):
  header = ['FlyFrom','FlyTo','PriceCZK','DepartureTime','ArrivalTime']
  ws.append(header)

  
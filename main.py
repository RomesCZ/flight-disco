import parse_params
import excel_file
import json_data
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
  filename='__DEBUG.log',level=logging.DEBUG)
logging.debug('************************************************')

print("--------")
#params load
p = parse_params.getP()
print("--------")
#create/load excel file
wb = excel_file.getExcelFile(p.file)
ws = wb.active
#save to file
wb.save(p.file)
###
json_datad = json_data.getJSONData()
excel_file.generateHeader(ws)
for d in json_datad:
  row = []
  row.append(d['flyFrom'])
  row.append(d['flyTo'])
  row.append(d['conversion']['CZK'])
  row.append(json_data.formateDateTime(d['dTime']))
  row.append(json_data.formateDateTime(d['aTime']))
  
  for r in d['route']:
    row.append(r['flyFrom'])
    row.append(r['flyTo'])
  
  row.append(d['deep_link'])
  ws.append(row)

wb.save(p.file)
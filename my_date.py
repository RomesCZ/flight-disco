from datetime import date
from datetime import timedelta
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
  filename='__DEBUG.log',level=logging.DEBUG)

#vrati naformatovany dnesek
# dd/mm/yyyy
def strActualDate():
  today = date.today()
  logging.debug('strActualDate()')
  logging.debug('return value: {0}'.format(today.strftime("%d/%m/%Y")))
  return today.strftime("%d/%m/%Y")

#vrati naformavany d+N
# dd/mm/yyyy
def strPlusDate(intDay):
  logging.debug("intDay:{0}".format(intDay))
  today = date.today()
  delta = timedelta(days=intDay)
  r = today + delta
  logging.debug('strPlusDate(intDay)')
  logging.debug('return value: {0}'.format(r.strftime("%d/%m/%Y")))
  return r.strftime("%d/%m/%Y")

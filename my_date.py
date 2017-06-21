from datetime import date
from datetime import timedelta
import logging
logger = logging.getLogger() #main logger

#vrati naformatovany dnesek
# dd/mm/yyyy
def strActualDate():
  today = date.today()
  logger.info('strActualDate()')
  logger.debug('return value: {0}'.format(today.strftime("%d/%m/%Y")))
  return today.strftime("%d/%m/%Y")

#vrati naformavany d+N
# dd/mm/yyyy
def strPlusDate(intDay):
  logger.info("strPlusDate(intDay)")
  logger.debug("intDay:{0}".format(intDay))
  today = date.today()
  delta = timedelta(days=intDay)
  r = today + delta
  logger.debug('return value: {0}'.format(r.strftime("%d/%m/%Y")))
  return r.strftime("%d/%m/%Y")

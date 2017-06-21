import argparse
import my_date
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
  filename='__DEBUG.log',level=logging.DEBUG)

def getP():
  defDateFrom = my_date.strActualDate()
  defDateTo = my_date.strPlusDate(1)

  parser = argparse.ArgumentParser()

  # prepinace
  parser.add_argument("--flyfrom", help="From", default="PRG")
  parser.add_argument("--flyto", help="To", default="anywhere")
  parser.add_argument("--datefrom", help="From dd/mm/yyyy", default=defDateFrom)
  parser.add_argument("--dateto", help="To dd/mm/yyyy", default=defDateTo)
  parser.add_argument("--file", help="Excel file name", default="export.xlsx")
  parser.add_argument("--typeflight", help="Possible values: oneway, return, round")
  parser.add_argument("--daysindestinationfrom", help="TODO")
  parser.add_argument("--daysindestinationto", help="TODO")
  parser.add_argument("--limit", help="TODO", default="300")
  parser.add_argument("--currency", help="TODO", default="CZK")
  parser.add_argument("--directflights", help="TODO", default=0)
  parser.add_argument("--demo", help="TODO", action="store_true")

  args = parser.parse_args()
  print("Fly From:    {0}".format(args.flyfrom))
  print("Fly To:      {0}".format(args.flyto))
  print("Date From:   {0}".format(args.datefrom))
  print("Date To:     {0}".format(args.dateto))
  print("File:        {0}".format(args.file))
  logging.debug('getP:return value {0}'.format(args))
  return args

def createUrl(args):
  baseUrl = 'https://api.skypicker.com/flights?'
  fullUrl = baseUrl
  fullUrl += "flyFrom={0}".format(args.flyfrom)
  fullUrl += "&to={0}".format(args.flyto)
  fullUrl += "&dateFrom={0}".format(args.datefrom)
  fullUrl += "&dateTo={0}".format(args.dateto)  
  fullUrl += "&curr={0}".format(args.currency)
  fullUrl += "&limit={0}".format(args.limit)
  fullUrl += "&directFlights={0}".format(args.directflights)
  if args.typeflight is None:
    fullUrl += "&typeFlight="
  else:
    fullUrl += "&typeFlight={0}".format(args.typeflight)
  if args.daysindestinationfrom is None:
    fullUrl += "&daysInDestinationFrom="
  else:
    fullUrl += "&daysInDestinationFrom={0}".format(args.daysindestinationfrom)
  if args.daysindestinationto is None:
    fullUrl += "&daysInDestinationTo="
  else:
    fullUrl += "&daysInDestinationTo={0}".format(args.daysindestinationto)
  fullUrl += "&partner=picky&partner_market=cz"
  
  logging.debug("URL: {0}".format(fullUrl))
  return fullUrl

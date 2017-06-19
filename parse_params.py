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
  parser.add_argument("--typeflight", help="Possible values:  round, oneway", default="round")
  parser.add_argument("--daysindestinationfrom", help="TODO", default=1)
  parser.add_argument("--daysindestinationto", help="TODO", default=2)
  parser.add_argument("--limit", help="TODO", default=300)

  args = parser.parse_args()
  print("Fly From:    {0}".format(args.flyfrom))
  print("Fly To:      {0}".format(args.flyto))
  print("Date From:   {0}".format(args.datefrom))
  print("Date To:     {0}".format(args.dateto))
  print("File:        {0}".format(args.file))
  logging.debug('getP:return value {0}'.format(args))
  return args

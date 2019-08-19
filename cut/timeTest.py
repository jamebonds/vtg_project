from datetime import datetime
now = datetime.now() # current date and time
nowdate = now.strftime("%Y%m%d")
fileReport = 'Reporting_' +nowdate +'-Job.xls'

print(fileReport)
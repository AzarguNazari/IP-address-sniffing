from utils import timesAndIpsFromLeftLog,timesAndWebsiteFromRightLog
from datetime import datetime
from dateutil.parser import parse

print("#################################################")
print("#                                               #")
print("#               Question 2                      #")
print("#                                               #")
print("#################################################")

# To collect the nominated ips that were trying to access between 20:14:30 - 20:15:30
ips = timesAndIpsFromLeftLog("./intersec/left.txt")
nominatedIps = set()
for tuple in ips:
    dt = parse(tuple[1][1:-1])
    if dt.time().hour == 20 and (14 <= dt.time().minute <= 15) and dt.time().second == 30:
        nominatedIps.add(tuple[0])

print(len(nominatedIps), " ip addresses are the nominated ip addresses")
print(nominatedIps)

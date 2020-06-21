from utils import timesAndIpsFromLeftLog,timesAndWebsiteFromRightLog
from datetime import datetime
from dateutil.parser import parse

print("#################################################")
print("#                                               #")
print("#               Question 3                      #")
print("#                                               #")
print("#################################################") 


## to collect the times between 10:00 +/- 1 that www.tv-movie.de was accessed 
timesAndWebsites = timesAndWebsiteFromRightLog("./intersec/right.txt")
nominatedTimes = set()
for tuple in timesAndWebsites:
    dt = parse(tuple[0][1:-1])
    if tuple[1] == 'http://www.tv-movie.de':
        if (dt.time().hour == 22 and (0 <= dt.time().minute <= 1)) or (dt.time().hour == 21 and (dt.time().minute == 59)):
            nominatedTimes.add(tuple[0][1:-1])



## To collect the ips and its corresponding time
ips = timesAndIpsFromLeftLog("./intersec/left.txt")
nominatedIps = {}
for tuple in ips:
    dt = parse(tuple[1][1:-1])
    if (dt.time().hour == 22 and (0 <= dt.time().minute <= 1)) or (dt.time().hour == 21 and (dt.time().minute == 59)):
        nominatedIps[tuple[1][1:-1]] = tuple[0]


# To compare the times and through it print the specific ips that were accessed to www.tv-movie.de
ips = set()
for time,ip in nominatedIps.items():
    dt1 = parse(time)
    for webTime in nominatedTimes:
       dt2 = parse(webTime)
       if dt2.time().hour == dt1.time().hour and dt2.time().minute == dt1.time().minute and dt1.time().second == dt2.time().second + 5:
           ips.add(ip)
           
# print the ips
print(ips)

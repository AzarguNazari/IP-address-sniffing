from utils import countRequests,ipaddresses
from collections import Counter
import operator

print("#################################################")
print("#                                               #")
print("#               Question 1                      #")
print("#                                               #")
print("#################################################")

#1 > How many requests are contained in the left-log and right-log, respectively?
leftSideRequestsTotal = countRequests("./intersec/left.txt")
rightSideRequestsTotal = countRequests("./intersec/right.txt")

print("\nPart 1")
print("Total Requests on left-log", leftSideRequestsTotal)
print("Total Requests on right-log", rightSideRequestsTotal)


#2 > How many different users, identified by their IP address, exist, how many webservers?
userIps = {}
totalIps = ipaddresses("./intersec/left.txt")
if totalIps:
    userIps = set(totalIps)
totalNumberOfUsers = len(userIps)

print("\nPart 2")
print("Total number of users", totalNumberOfUsers)

#3 > What are the five most visited websites?
print("\nPart 3")
totalIps = ipaddresses("./intersec/right.txt")
ipaddressSet = dict(Counter(totalIps))
sorted_ips = sorted(ipaddressSet.items(), key=operator.itemgetter(1))[::-1]

print("Top 5 visited websites")
for ip in sorted_ips[1::5]:
    print("IP:", ip[0], "  Total Visits: ", ip[1])

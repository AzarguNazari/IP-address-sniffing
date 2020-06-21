import re as regex


# total number of requests
def countRequests(fname):
    with open(fname, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Fetches IP address from file
def ipaddresses(fname):
    with open(fname,"r") as f:
        line = f.read()
    totalIps = regex.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',line)
    return totalIps

# Fetches IP address and Time from file
def timesAndIpsFromLeftLog(fname):
    file1 = open(fname, 'r') 
    Lines = file1.readlines()
    ips = []
    times = []
    for line in Lines: 
        lineParts = regex.split("( )", line)
        ips.append(lineParts[0])
        times.append(lineParts[2])
    res = []
    for x in range(0, len(ips)):
        res.append((ips[x],times[x]))
    return res

# Fetches IP address and Time from file
def timesAndWebsiteFromRightLog(fname):
    file1 = open(fname, 'r') 
    Lines = file1.readlines()
    times = []
    websites = []
    for line in Lines: 
        lineParts = regex.split("( )", line)
        times.append(lineParts[0])
        websites.append(lineParts[4][:-1])
    res = []
    for x in range(0, len(times)):
        res.append((times[x],websites[x]))
    return res

#!/usr/bin/evn python

from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity

def getLocation(pkt):
    if 'IP' in pkt:
        ip_src = pkt.getlayer('IP').src
        ip_dst = pkt.getlayer('IP').dst
    else:
        return
    
    response_src = DbIpCity.get(ip_src,api_key='free')
    response_dst = DbIpCity.get(ip_dst,api_key='free')
    
    src = mapLocation(response_src)
    dst = mapLocation(response_dst)

    print(src['country'] + ' -> ' + dst['country'] + '\n')
    
    
def mapLocation(response):
    locationDict = {
        "city" : "",
        "region" : "", 
        "country" : "",
        "longitude" : "",
        "latitude" : ""
    }
    locationDict['city'] = response.city
    locationDict['region'] = response.region
    locationDict['country'] = response.country
    locationDict['longitude'] = response.longitude
    locationDict['latitude'] = response.latitude
    
    # print("IP Address: {0}\nCity: {1} \nRegion: {2} \nCountry: {3} \nLongitude: {4} \nLatitude {5}"
    # .format(response.ip_address,response.city,response.region,response.country,response.longitude,
    # response.latitude))

    return locationDict

def main():
    sniff(filter="ip", prn=getLocation)
    return 0
    
if __name__ == "__main__":
    main()
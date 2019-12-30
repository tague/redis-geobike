#!/usr/bin/env python3

import load_station_data as station
import urllib.request
import json
import redis


def main(feedURL):
    "Fetch feed examples and pretty print for blog post"
    
    feed = station.fetch_url(feedURL)
    print("GBFS top: ")
    print(json.dumps(feed, indent=4, sort_keys=True))
    
    station_info_url = station.station_status_feed_url(feed)
    station_info = station.fetch_url(station_info_url)
    print ("Station Feed Example: ")
    print(json.dumps(station_info, indent=4))
    
    
    
if __name__ == '__main__':
    feedURL = "http://gbfs.citibikenyc.com/gbfs/gbfs.json"
    main(feedURL)

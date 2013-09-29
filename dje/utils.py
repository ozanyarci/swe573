
"""
Utilities for Sentiolytics Frontend
"""

import urllib2
import django.utils.simplejson as json

def service_request(id, data):
    url = "http://sentios.cloudapp.net/api/%s" % id
    if data:
        d = json.dumps(data)
        try:
            result = urllib2.urlopen(url,d)
            j_obj = json.loads(result.read())
            list_data = j_obj["data"]
            return list_data
        except:
            empty = []
            return empty

def tryService():
    print service_request("GetBestScorers", {"league_id": 1, "season_id": 9064, "count": 3})


tryService()


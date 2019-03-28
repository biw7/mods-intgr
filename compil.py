import requests
import json
import logs


def sh (op,url):
   if op == 0:
      return url
   if op == 1:
      api = logs.apiCKfy 
      linkREQUEST = requests.get('https://clicksfly.com/api?api='+api+'&url=' + url)
      parse = linkREQUEST.json()
      link = parse['shortenedUrl']
      return link
      
   if op == 2:
      api = logs.apiRBR 
      r = requests.post("https://api.rebrandly.com/v1/links",
                        data=json.dumps({
                           "destination": url
                           , "domain": {"fullName": "rebrand.ly"}
                           }),
                        headers={
                           "Content-type": "application/json",
                           "apikey": api,
                           "workspace": ""
                        })

      if (r.status_code == requests.codes.ok):
         Tlink = r.json()
         link = Tlink["shortUrl"]
         return link


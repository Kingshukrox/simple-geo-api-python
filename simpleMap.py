import urllib.error
import urllib.parse
import urllib.request
import json
import time
serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'
while True:
    inp_addr = input("enter address: ")
    if len(inp_addr) < 1:
        break
    mapurl = serviceurl+urllib.parse.urlencode({"address": inp_addr})
    # print(mapurl)
    print("\nFinding", inp_addr, '....')
    start = time.time()
    url = urllib.request.urlopen(mapurl)
    json_recv = url.read()
    json_recv = json_recv.decode()
    json_formatted = json.loads(json_recv)
    if json_formatted['status'] != 'OK':
        print('not found')
        continue
    print(json_formatted['results'][0]['formatted_address'])
    stop = time.time()
    # print('Time taken= ', stop - start)

# maps.googleapis.com/maps/api/geocode/json?
# http://py4e-data.dr-chuck.net/json?key=42&

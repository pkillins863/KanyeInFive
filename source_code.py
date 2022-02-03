import time
import requests

x = range(0, 3)

#for n in x:
while(True):
    time.sleep(10)
    r = requests.get('https://api.kanye.rest')
    print(r.text[9:-1], '- Kanye West')
    
print('done')
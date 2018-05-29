#!/usr/bin/python

#from flask import Flask
#application = Flask(__name__)

#@application.route("/")
#def hello():
#    return "Hello World!"

#if __name__ == "__main__":
#    application.run()


import re
import time
import urllib.request
import urllib.parse

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


while 1:

    html_content = urllib.request.urlopen('http://www.cmi.ac.in//admissions/entrance-results-2018.php').read().decode('utf-8')
    #print (html_content)
    matches = re.findall('C-', html_content) # Because Computer Science Starts as C-BLR-0006
	
    if len(matches) == 0:
       print ("Yeah, Result Not Declared. Going to sleep at" + time.ctime()) #will not send anything
       time.sleep(1000) #sleep for 2 hours
    
    else:
       selected = re.findall('18200613', html_content)#18200613
       
       if len(selected) == 0:
           
           msg="CMI Results are Out! You are NOT Selected"
           res = sendSMS('FqRMhPtOha4-hg2Tl2F7qUUllZA3qFrDLeR3wGvwP2', '918277576500', 'TXTLCL', msg)
       
       else:
           
           msg="CMI Results are Out! You are Selected :) "
           res = sendSMS('FqRMhPtOha4-hg2Tl2F7qUUllZA3qFrDLeR3wGvwP2', msg)
           
       print (res)
       quit()

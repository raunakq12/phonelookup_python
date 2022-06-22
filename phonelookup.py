import requests
import pandas as pd
from bs4 import BeautifulSoup
 
# link for extract html data
# Making a GET request
     
def getdata(url):
    r=requests.get(url)
    return r.text

api = 'bae5eb02920abcc3c9fe9b7e9bdd1a9b'
 
# number and country code
number = '9108167232'
country = 'IN'
 
# pass Your API, number and country code
# in getdata function
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
text = BeautifulSoup(htmldata, 'html.parser')
print(text)

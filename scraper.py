import urllib
from urllib import urlopen
import re

stocks = ['pfe', 'bx', 'alxn', 'nflx', 'crm', 'yelp'] #list of stocks i'm interested in
url_addendum = '\%2C' #end of url for each stock's yahoo finance page
base_url = "http://finance.yahoo.com/q?uhb=uh3_finance_vert&fr=&type=2button&s=" #beginning of url
for i in stocks:
    url = base_url + i + url_addendum #combines the three components of the url
    f = urllib.urlopen(url) #saves the html as a file
    words = f.read().decode('utf-8') #makes html readable
    find_query_1 = "<span id=\"yfs_l86_" #this is part of the tag that precedes the price i'm looking for
    find_query_2 = "\">(.+)</span></span> <span class=\"" #this succeeds the price i'm looking for
    query = find_query_1 + i + find_query_2 #this combines the three components to specify what to look for in the html
    price = re.findall(query, words) #this finds where that query is and returns the unknown value
    print i, price[0] #this prints the stock symbol and that value

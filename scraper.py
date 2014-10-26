import urllib
from urllib import urlopen
import re

stocks = ['pfe', 'bx', 'alxn', 'nflx', 'crm', 'yelp']
url_addendum = '\%2C'
base_url = "http://finance.yahoo.com/q?uhb=uh3_finance_vert&fr=&type=2button&s="
for i in stocks:
    url = base_url + i + url_addendum
    f = urllib.urlopen(url)
    words = f.read().decode('utf-8')
    find_query_1 = "<span id=\"yfs_l86_"
    find_query_2 = "\">(.+)</span></span> <span class=\""
    query = find_query_1 + i + find_query_2
    price = re.findall(query, words)
    print i, price[0]

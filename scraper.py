import urllib
from urllib import urlopen
import re

url = "http://finance.yahoo.com/q?uhb=uh3_finance_vert&fr=&type=2button&s=AMZN%2C"
f = urllib.urlopen(url)
words = f.read().decode('utf-8')
price = re.findall("<span id=\"yfs_l86_amzn\">(.+)</span></span> <span class=\"up_g\">", words)
print price[0]

import pandas as pd
from bs4 import BeautifulSoup
import os
import re
from lxml import html

fp = 'C:/Temp/retropay/2265148062.html'

f = open(fp, 'r')
content = f.read()
soup = BeautifulSoup(f.read())

f.close()

header = soup.find("div", {"id": "win0div$ICField324$0"})
table = soup.find("table", {"id": "TCHKDAT3_VW$scroll$0"})
apanda = pd.read_html(table.prettify())
bpanda = pd.read_html(header.prettify())

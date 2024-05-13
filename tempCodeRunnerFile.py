
from bs4 import BeautifulSoup;
import requests;

url='https://www.practicepython.org/assets/nameslist.txt';

# r=requests.get(url);
# r_text=r.text
# soup=BeautifulSoup(r_text,'html.parser');
with open (url,'r') as open_file:
    all_text=open_file.read();
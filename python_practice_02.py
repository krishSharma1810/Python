#  question 17
# Use the BeautifulSoup and requests Python packages to print out a list 
# of all the article titles on the New York Times homepage.
## answer ->
# import requests;
# from bs4 import BeautifulSoup;
# url='https://www.nytimes.com/';
# response=requests.get(url);
# response_html=response.text;
# soup=BeautifulSoup(response_html,'html.parser')
# headings=soup.find_all('p',class_='indicate-hover')
# headings_list=[tag.get_text(strip=True) for tag in headings]
# for i in headings_list:
#     print(i,"\n");


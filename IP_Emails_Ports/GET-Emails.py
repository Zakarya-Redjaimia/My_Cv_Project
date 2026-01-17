# Web Scraping
# pip install bs4 , re , requests , selenium
# {email , phone , link , htmltopdf} !
import re
import time
from requests import get
from selenium import webdriver 
from selenium.webdriver.common.by import By
url = str(input("Enter Site To Get Emails :"))
time.sleep(1)
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach",True)
#brow = webdriver.Chrome(options=options)
br = get(url).text
email = re.findall('\S+@\S+',br)
for i in email :
    print (i)
#=============== Get Phone Number =================
from selenium import webdriver
import re , time

url = str(input("Enter Site To Get Phone :"))
time.sleep(1)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
brows = webdriver.Chrome(options=options)
brows.get(url)  # "https://ar.mytrashmobile.com/"
go = brows.page_source
phone = re.findall(r'[\d]{3}[\d]{3}[\d]{4}',go)
for i in phone :
    print(i)
#=============== Get All Link In One Site =================
# C:\Users\ZRY\Desktop
from bs4 import BeautifulSoup
import requests , time

target = str(input("Enter Site To Get Link : "))
time.sleep(1)
req = requests.get(target)
bs = BeautifulSoup(req.text,"html.parser")
for link in bs.find_all('a'):
    print(link.get('href'))
# "C:/Users/ZRY/Desktop/l_link.txt"
#=============== Html To Pdf =================
import pdfkit,os
pdffile = "C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = pdffile)
url = input("Enter URL : ")
save = url + ".pdf"
pdfkit.from_url(url , save , configuration=config)
os.startfile(save)
import requests
from bs4 import BeautifulSoup
import smtplib   #smtp is also used for sending emails
import time


url=requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
    #print(url) we have accessed the url success
#accessing contents of url
cont=url.content
#print(cont)   #this will give us complete html code of the web page
soup=BeautifulSoup(cont,'html.parser')
 #print(soup.prettify())
price=float(soup.find('p',class_='price_color').text[1:]) #this string from index1 to end

if price<60:
    smt=smtplib.SMTP('smtp.gmail.com',587)
    #create a server
    smt.ehlo() #greeting our server
    smt.starttls() #security measure 
    smt.login('priyankabani13official@gmail.com','hyraeglyedpdbjbl')
    #time to sent msg
    smt.sendmail('priyankabani13official@gmail.com','priyankabani62@gmail.com',f"Subject : Headphones  price notifier\n\n Hi,price has dropped to {price} ,Buy it now")
    smt.quit()
    time.sleep(24*60*60)

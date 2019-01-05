"""
This program gets the daily horoscope and mails to the user.
Author: Rupali Sinha
"""


from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def retrieve_horoscope(url):
    """
    This function gets the html content of the url and returns the title and text of the actual content wanted.
    :param url: url of a horoscope website
    :return: title and the content of the horoscope from the html page
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find('meta',property='og:title')['content']
    content = soup.find('meta',property='og:description')['content']
    return title, content


if __name__=='__main__':
    # change the url
    url = 'https://www.xxxxxxxxx/horoscopes/general/horoscope-general-daily-today.aspx?sign=4'
    title, content = retrieve_horoscope(url)


    # connect with google smtp server to send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # change your gmail id and password
    server.login('xxxxxx@gmail.com', 'xxxxxxxxx')
    msg = MIMEMultipart()

    # change the from and to address
    fromaddr = "xxxxxx@gmail.com"
    toaddr = "xxxxxx@gmail.com"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Your daily horoscope"
    body = title + content
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
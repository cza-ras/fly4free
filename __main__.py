from bs4 import BeautifulSoup
import requests
from email_sender import email_sender

if __name__ == '__main__':
    
    # URL strony z alertami + antyroboty
    url = 'https://www.fly4free.pl/tanie-loty/promocje/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

    strona = requests.get(url, headers=head)
    soup = BeautifulSoup(strona.content, 'html.parser')
    ogloszenia = soup.find_all(class_='item__title')

    #reguly alertów
    rule_a= "Peru"
    rule_b = "Lima"
    rule_c = "Tokio"
    rule_d = "Japoni"
    rule_e = "Bilbao"
    final = ''

    for i, p in enumerate(ogloszenia, 1):
        if rule_a in p.text or rule_b in p.text or rule_c in p.text or rule_d in p.text or rule_e in p.text:
            final = final.__add__(f"Znalezione w ofercie numer {i}: {p.text} \n ")

    if final!='':
        email_sender.send_email(final)
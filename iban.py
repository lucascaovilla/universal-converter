import requests
from bs4 import BeautifulSoup

def scraping_iban():
  #lista utilizada
  list = []

  #Request
  r_iban = requests.get('https://www.iban.com/currency-codes')
  
  #BS
  html_iban = r_iban.text
  soup = BeautifulSoup(html_iban, 'html.parser')
  
  #organiza o scraping em uma lista de dicts(html)
  tr_list = soup.find_all('td')
  for item in tr_list:
    country = {
      'country': tr_list[0].get_text(),
      'currency': tr_list[1].get_text(),
      'code': tr_list[2].get_text(),
      'number': tr_list[3].get_text()
    }
    tr_list.pop(3)
    tr_list.pop(2)
    tr_list.pop(1)
    tr_list.pop(0)
    if country['currency'] == 'No universal currency':
      continue
    else:
      list.append(country)
  
  #emite a lista de números e países
  for dict in list:
    position = list.index(dict) + 1
    dict['position'] = position
  return list
    
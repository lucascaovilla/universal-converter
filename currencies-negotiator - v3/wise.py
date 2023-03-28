import requests
from bs4 import BeautifulSoup
from iban import scraping_iban
from babel import numbers
import sys

def scraping_wise(first_currency, second_currency, amount):
  url_wise = f'https://wise.com/gb/currency-converter/{first_currency}-to-{second_currency}-rate?amount={amount}'
  url_wise = url_wise.replace(' ','')
  print(url_wise)
  try:
    r_wise = requests.get(url_wise)
  except:
    return ('error')
  html_wise = r_wise.text
  soup = BeautifulSoup(html_wise, 'html.parser')
  convertion_rate = soup.find('span', class_='text-success').get_text()
  converted_value = int(amount)*float(convertion_rate)
  
  currency_1 = first_currency + ' '
  currency_2 = second_currency + ' '

  formated_currency_1 = numbers.format_currency(amount, currency_1, locale='es_CO', group_separator=True)
  formated_currency_2 = numbers.format_currency(converted_value, currency_2, locale='es_CO', group_separator=True)

      
  return formated_currency_1, amount, formated_currency_2, convertion_rate
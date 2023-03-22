import requests
from bs4 import BeautifulSoup
from iban import scrapping_iban
from babel import numbers
import sys

countries = []
values = []
url_base = ''
#brl-to-usd-rate?amount=50

def scrapping_wise():
  countries_tuple = scrapping_iban()
  for item in countries_tuple:
    countries.append(item)

  amount = input(f'Informe o valor em {countries[1]} que deseja converter para {countries[3]}.\n')
  url_wise = f'https://wise.com/gb/currency-converter/{countries[1]}-to-{countries[3]}-rate?amount={amount}'
  try:
    r_wise = requests.get(url_wise)
  except:
    sys.exit("Uma ou ambas moedas não possuem registro. Favor utilize outras moedas.")
  html_wise = r_wise.text
  soup = BeautifulSoup(html_wise, 'html.parser')
  find_value = soup.find('span', class_='text-success')
  converted_value = str(int(amount)*float(find_value.get_text()))
  
  currency_1 = countries[1] + ' '
  currency_2 = countries[3] + ' '

  format_1 = numbers.format_currency(amount, currency_1, locale='es_CO', group_separator=True)
  format_2 = numbers.format_currency(converted_value, currency_2, locale='es_CO', group_separator=True)
  conversion_status = f'O valor de {format_1} convertido é de {format_2}'
      
  return conversion_status

print(scrapping_wise())
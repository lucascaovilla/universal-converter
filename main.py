import requests
from bs4 import BeautifulSoup

url_iban = 'https://www.iban.com/currency-codes'
r_iban = requests.get(url_iban)

html_iban = r_iban.text
soup = BeautifulSoup(html_iban, 'html.parser')
list = []
list_1 = []
list_2 = []
tr_list = soup.find_all('td')

for item in tr_list:
  countries = {
    'country': tr_list[0],
    'currency': tr_list[1],
    'code': tr_list[2],
    'number': tr_list[3]
  }
  tr_list.pop(3)
  tr_list.pop(2)
  tr_list.pop(1)
  tr_list.pop(0)
  list.append(countries)



for dict in list:
  countries_str = {
  'country': dict['country'].get_text(),
  'currency':dict['currency'].get_text(),
  'code': dict['code'].get_text(),
  'number': dict['number'].get_text()
   }
  list_1.append(countries_str)

for dict in list_1:
  if dict['currency'] != 'No universal currency':
    list_2.append(dict)
  
  


print('Bem-vindo ao Negociador de Moedas\nEscolha pelo numero da lista o país que deseja consultar o código da moeda.')
for dict in list_2:
  position = list_2.index(dict)
  dict['position'] = position
  print(f'#{position}', dict['country'])



   

while True:
  try:
    user = int(input())
    if user >= 216:
      print('Não existe. Escolha uma opção da lista:')
      continue
    elif user <= 215 and type(user) == int:
      for dict in list_2:
        if user == dict['position']:
          print(f'Você escolheu {dict["country"]}\nO código da moeda é {dict["code"]}')
      break
  except:
    print('isso não é um número')
    continue
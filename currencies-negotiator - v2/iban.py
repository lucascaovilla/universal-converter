import requests
from bs4 import BeautifulSoup

def scrapping_iban():
  #lista utilizada
  list = []

  #Request
  r_iban = requests.get('https://www.iban.com/currency-codes')
  
  #BS
  html_iban = r_iban.text
  soup = BeautifulSoup(html_iban, 'html.parser')
  
  #organiza o scrapping em uma lista de dicts(html)
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
    print(f'#{position}', dict['country'])
    
  #print do texto de boas-vindas
  
  #verifica se a input é um número/está dentro da lista - retorna nome de país e código da moeda

  while True:
      user_input_1 = input('\n\nBem-vindo ao Negociador de Moedas\nEscolha pelo numero da lista o país que deseja consultar o código da moeda.\n')
      try:
        user_input_1 = int(user_input_1)
      except:
        print('Isso não é um número.')
        continue      
      if user_input_1 > len(list):
        print('Não existe. Escolha uma opção da lista:')
        continue
      else:
        country_1_data = list[user_input_1-1]
        print(f'Você escolheu {country_1_data["country"]}\nO código da moeda é {country_1_data["code"]}\n')
        country_1 = country_1_data["country"]
        currency_1 = country_1_data["code"]
        user_input_2 = input('Informe o código do país cuja moeda deseja comparar:\n')
        try:
          user_input_2 = int(user_input_2)
        except:
          print('Isso não é um número.')
          continue     
        if user_input_2 > len(list):
          print('Não existe. Escolha uma opção da lista:')
          continue
        elif user_input_2 == user_input_1:
          print('Os países devem ser diferentes para comparar')
          continue
        else:
          country_2_data = list[user_input_2-1]
          print(f'Você escolheu {country_2_data["country"]}\nO código da moeda é {country_2_data["code"]}\n')
          country_2 = country_2_data["country"]
          currency_2 = country_2_data["code"]
          return country_1, currency_1, country_2, currency_2

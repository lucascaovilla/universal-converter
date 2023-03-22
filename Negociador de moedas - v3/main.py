from wise import scraping_wise
from flask import Flask, render_template, request, redirect , send_file, send_from_directory
from wise import scraping_wise
from iban import scraping_iban

app = Flask('Currency Negotiator')

@app.route('/')
def home():
    countries_list = scraping_iban()

    first_currency = str(request.args.get('fc')).upper()
    second_currency = str(request.args.get('sc')).upper()
    amount = str(request.args.get('amt'))
    
    print(first_currency, second_currency, amount)

    try:
        result = scraping_wise(first_currency, second_currency, amount)
        return render_template('home.html', countries = countries_list, result = result)
    except:
        return render_template('home.html', countries = countries_list)


app.run(host='0.0.0.0')
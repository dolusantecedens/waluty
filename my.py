from flask import Flask, request, render_template
import requests
import csv


app=Flask(__name__)


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
cur=(data[0]['rates'])
x=['currency','code','bid','ask']
with open ('waluty.csv', mode='w') as waluty:
    writer=csv.DictWriter(waluty, x, delimiter=';')
    writer.writeheader()
    writer.writerows(cur)
    
@app.route('/kantor', methods=['GET','POST'])
def kantor():
    currencies=[]
    for i in cur:
        currencies.append(i['currency'])
    if request.method=='POST':
        print(request.form)
        y=cur[int(request.form.get('cokolwiek'))]['ask']
        s=float((request.form.get('kwota')))
        wynik=s*y
        return render_template('main.html', wynik=wynik, currencies=currencies )
    return render_template('main.html', currencies=currencies)    


if __name__ == '__main__':
    app.run(debug=True)    
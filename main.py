from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import random
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/src', methods=['POST'])
def src():
    cnt=math.floor(random.randrange(0,6)*5)
    gym = request.form['gym']
    mtx = []
    sttr=[]
    url = 'https://br.search.yahoo.com/search;_ylt=AwrEpb3UI5dmLcgMlI3z6Qt.;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=estudos+site%3Ayoutube.com&pz=7&fr=sfp&fr2=sb-top&b='+str(15*cnt)+'&pz=7&xargs=0'

    # Fazer a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os elementos <a> que contêm os links
        links = soup.find_all('a',href=True)
        
        # Iterar sobre os elementos <a> e imprimir os links
        for link in links:
            if '/watch?v=' in link['href']:

                sttr.append(link['href'])
        
        
    
        
    
    return render_template('vids.html', varb=str(sttr[0].replace('watch?v=', 'embed/')),varb2=str(sttr[1].replace('watch?v=', 'embed/')))

    #return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def homecat():
    title = 'home'
    return render_template('home.html',
                           context={'title':title}
                            
    )


@app.route('/func/<cat>')
def randomcat(cat: str):
    
    title = 'random_cat'
    sarlavha = "Tasodifiy mushuklardan birini tanlang."
    catlist = []
    for i in range(8):
        url_cat = "https://api.thecatapi.com/v1/images/search"
        respons = requests.get(url_cat)
        data = respons.json()[0]['url']
        catlist.append(data)
    
    return render_template('cat.html',
                            context = {
                                'title':title,
                                'sarlavha':sarlavha,
                                'catlist':catlist,
                                'cat':cat,
                                
                            }
    )

@app.route('/data/<dog>')
def randomdog(dog: str):
    title = "randomm_dog"
    sarlavha = "Tasodifiy kuchuklardan tanlang."
    doglist = []
    for i in range(8):
        url_dog = 'https://random.dog/woof.json'
        respons = requests.get(url_dog)
        data = respons.json()['url']
        doglist.append(data)
    
    return render_template('dog.html',
                            context = {
                                'title':title,
                                'doglist':doglist,
                                'dog':dog,
                                'sarlavha':sarlavha,
                            }
    )

if __name__ == "__main__":
    app.run(debug = os.getenv("DEBUG"), port = os.getenv("PORT"))
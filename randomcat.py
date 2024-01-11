from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/<cat>')
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

if __name__ == "__main__":
    app.run(debug = True, port = 8000)
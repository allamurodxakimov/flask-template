from flask import Flask,request, render_template
import requests

app = Flask(__name__)

@app.route('/random/<dog>')
def dogandcat(dog: str):
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
    app.run(debug=True, port = 4000)

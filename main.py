from flask import Flask, request, render_template
import requests

app = Flask(__name__)

url = "https://randomuser.me/api/"

@app.route('/<name>/<gender>')
def home(name: str,gender: str):
    title = 'randomuser_gender'
    imglist = []
    for i in range(12):
        payload = {
            "gender":gender
        }
        respons = requests.get(url,params = payload)
        data = respons.json()['results'][0]
        img = data['picture']['large']
        imglist.append(img)
    gender = data['gender']
    return render_template('index.html', 
                           context={
                                "title": title,
                                "name": name,
                                "gender":gender,    
                                "imglist":imglist,
                            }
                        )


if __name__ == '__main__':
    app.run(debug=True, port=8000)
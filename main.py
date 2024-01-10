from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/<name>')
def home(name: str):

    title = 'Bosh sahifa'
    nums = range(30)
    return render_template('index.html', 
                           context={
                                "title": title,
                                "name": name,
                                "nums": nums
                            }
                        )


if __name__ == '__main__':
    app.run(debug=True, port=8000)
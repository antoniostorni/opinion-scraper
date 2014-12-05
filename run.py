from flask import Flask, render_template, json, url_for

app = Flask(__name__)

@app.route('/')
def opinions():
    json_data = open("result.json")
    data = json.load(json_data)
    return render_template('list.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run()

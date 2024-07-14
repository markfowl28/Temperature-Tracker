from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from data_display import find_data
from temperature_display import find_temperature

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Toxicity01!!'
app.config['MYSQL_DB'] = 'weather'

mysql = MySQL(app)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route('/temperature', methods=['POST', 'GET'])
def check_temperature():
    if request.method == 'GET':
        results = find_temperature()
    return render_template("temperature.html", location=results[0], temperature=results[1] + '°F')

@app.route('/data', methods=['POST', 'GET'])
def check_trends():
    if request.method == 'POST':
        month = request.form.get("month")
        day = request.form.get("day")
        data = find_data(mysql, month, day)
        return render_template("result.html", graph=data)
    else:
        return render_template("data.html")

if __name__ == '__main__':
    app.run(debug=True)

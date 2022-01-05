from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static-chart')
def static_chart():
    return render_template('static-chart.html')


@app.route('/random-chart')
def random_chart():
    return render_template('random-chart.html')


@app.route('/dynamic-chart')
def dynamic_chart():
    return render_template('dynamic-chart.html')


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/api/cpu-load/<qty>')
def cpu_load(qty=1):
    try:
        qty = abs(int(qty))
    except:
        qty = 1
    sample_data = {
        0: {
            'created_at': '2020-01-01 00:00:01',
            'load': '62.5'
        },
        1: {
            'created_at': '2020-01-01 00:00:06',
            'load': '56.2'
        },
        2: {
            'created_at': '2020-01-01 00:00:11',
            'load': '34.9'
        },
        3: {
            'created_at': '2020-01-01 00:00:16',
            'load': '24.6'
        },
        4: {
            'created_at': '2020-01-01 00:00:21',
            'load': '3.1'
        },
        5: {
            'created_at': '2020-01-01 00:00:26',
            'load': '4.9'
        }
    }
    items_required = dict(list(sample_data.items())[0:qty])
    return jsonify(items_required)


@app.route('/api/cpu-load')
def cpu_load_latest():
    return cpu_load(1)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

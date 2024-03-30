from pathlib import Path

import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/tractor', methods=['GET'])
def get_tractor_data():
    tractor_id = request.args.get(key='tractor_id', type=str)
    data = pd.read_csv(Path(
        f'./data/исходные данные от оператора/022C4097/'
        f'log(336804182)[26-03-2024_16-06-01] 01.06-01.07.csv'),
        delimiter=';').head(100)
    # Assuming the first column is datetime
    # data['datetime'] = pd.to_datetime(data.iloc[:, 0])
    return jsonify({'datetime': data.iloc[:, 0].to_list()})


if __name__ == '__main__':
    app.run(debug=True)

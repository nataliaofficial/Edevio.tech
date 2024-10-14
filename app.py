from flask import Flask, request, jsonify
import random
import torch
import torch.nn as nn
import torch.optim as optim

app = Flask(__name__)


@app.route('/api/get_forecast', methods=['POST'])
def get_forecast():
    data = request.get_json()
    location = data.get('location')

    if location:
        
        forecasted_energy = cuda_forecast_model(location)
        forecast = get_solar_forecast(location)
        forecast['energy'] = forecasted_energy 
        return jsonify(forecast)
    else:
        return jsonify({"error": "Location not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

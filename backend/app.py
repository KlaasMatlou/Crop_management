from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import random
import os
import requests

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crop_monitoring.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database models
class SensorLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    moisture = db.Column(db.Integer)
    humidity = db.Column(db.Integer)

class PestDetectionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    result = db.Column(db.String(100))

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    data = {
        'temperature': round(20 + random.random() * 10, 1),
        'moisture': round(40 + random.random() * 30),
        'humidity': round(50 + random.random() * 30)
    }
    # Save to database
    log = SensorLog(**data)
    db.session.add(log)
    db.session.commit()
    return jsonify(data)

@app.route('/upload-pest-image', methods=['POST'])
def upload_pest_image():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    # Dummy pest detection logic
    result = 'Pest detected: Aphids'
    log = PestDetectionLog(filename=file.filename, result=result)
    db.session.add(log)
    db.session.commit()
    return jsonify({'result': result})

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = 'your_openweathermap_api_key_here'  # Replace with your actual key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        result = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'condition': data['weather'][0]['description']
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch weather data', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

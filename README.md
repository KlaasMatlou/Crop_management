# 🌾 Crop Monitoring System

A web application that allows farmers to remotely monitor their crops with real-time sensor data, weather forecasts, and pest detection.

## 🚀 Features

- 🌡️ Real-time Sensor Data: Simulated sensor readings for temperature, soil moisture, and humidity.
- 🌦️ Weather Forecast: Integration with [OpenWeatherMap API](https://openweathermap.org/api) to fetch current weather by city.
- 🐛 Pest Detection: Upload plant images and get dummy pest detection feedback.
- ⚙️ RESTful API: Backend built with Flask.

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **External API**: OpenWeatherMap

## 📁 Project Structure

```
Crop_management/
├── backend/
│   ├── app.py                # Flask backend server
│   ├── pitch_deck.py         # Generates pitch deck PDF
│   ├── crop_monitoring.db    # SQLite database
│   └── uploads/              # Uploaded pest images
├── frontend/
│   ├── index.html            # Main dashboard
│   ├── style.css             # Page styling
│   └── script.js             # JavaScript for interaction
```

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/klaasmatlou/crop-monitoring.git
cd crop-monitoring
```

### 2. Install Backend Dependencies
```bash
cd backend
pip install flask flask-cors flask-sqlalchemy requests
```

### 3. Get a Free Weather API Key
- Visit [OpenWeatherMap](https://openweathermap.org/api)
- Sign up and get your free API key, if you need to change it,
- Replace `'the key i have put in there'` in `app.py` with your actual key

### 4. Run the Flask Backend
```bash
python app.py
```

### 5. Open the Frontend
Just open `frontend/index.html` in your web browser.

## 📸 Sample API Usage

### ✅ Real-time Sensor Data
```
GET /sensor-data
```

### ✅ Weather Forecast
```
GET /weather?city=Nairobi
```

### ✅ Pest Detection
```
POST /upload-pest-image (multipart/form-data with image)
```

## 📌 Notes

- This is a prototype. Sensor and pest detection data are simulated/dummy.
- For production, integrate real sensors and machine learning models for pest detection.

## 🤝 Credits

- Powered by [OpenWeatherMap](https://openweathermap.org)

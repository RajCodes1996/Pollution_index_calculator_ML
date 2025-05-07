# 🌍 Pollution Index Calculator 🚦

A web-based Pollution Index Calculator built with **Python**, **Django**, and **Machine Learning** to predict air pollution levels based on user-input PM values and geographic coordinates. It also visualizes predictions using dynamic charts.

---

## 📌 Features

- 🔍 Predicts pollution index using PM2.5, PM10, PM1.0, latitude, and longitude.
- 🤖 Uses Linear Regression for predictions.
- 📉 Graphical output of pollution index (Matplotlib + Seaborn).
- 🌐 Web-based user interface with Django templates.
- 📊 Categorizes results into air quality levels (Good, Moderate, Hazardous, etc.).

---

## 🛠️ How It Works

- **Dataset**: `pollution_data.csv` in `calculator/data/`
- **Index Formula** (if missing in data):  
  `pollution_index = pm2_5 * 0.5 + pm10 * 0.3 + pm1_0 * 0.2`
- **Features Used**:  
  `pm2_5`, `pm1_0`, `pm10`, `lat`, `long`
- **Model**: Linear Regression (via `scikit-learn`)
- **Scaler**: StandardScaler

---

## 📈 Pollution Levels

| Index Range     | Air Quality Level                   |
|------------------|-------------------------------------|
| 0 - 50           | Good                                |
| 51 - 100         | Moderate                            |
| 101 - 150        | Unhealthy for Sensitive Groups      |
| 151 - 200        | Unhealthy                           |
| 201 - 300        | Very Unhealthy                      |
| 301+             | Hazardous                           |

---

## 🧪 Screens & Routes

| URL Route       | Description                             |
|------------------|-----------------------------------------|
| `/`              | Input form for pollution parameters     |
| `/result/`       | Displays prediction, message, and chart |
| `/chart/`        | Reserved for extra visualizations       |

---

## 🧑‍💻 Local Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/pollution-index-calculator.git
   cd pollution-index-calculator

Install requirements
pip install -r requirements.txt
Run the server

bash
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/


📦 Dependencies
Django

pandas

numpy

scikit-learn

matplotlib

seaborn

Install all using pip install -r requirements.txt

📁 Project Structure
calculator/
├── data/
│   └── pollution_data.csv
├── templates/
│   └── calculator/
│       ├── index.html
│       ├── result.html
│       └── chart.html
├── views.py
├── urls.py
└── ...

🚀 Future Scope
Real-time sensor data/API integration

Geolocation auto-detection

Historical trends and comparisons

User accounts with prediction history

import os
import numpy as np
import pandas as pd
from django.conf import settings
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# Train model function (same as before)
def train_model():
    csv_file_path = os.path.join(settings.BASE_DIR, 'calculator', 'data', 'pollution_data.csv')
    data = pd.read_csv(csv_file_path, dtype={'pm2_5': 'float', 'pm1_0': 'float', 'pm10': 'float'})
    data.ffill(inplace=True)
    
    if 'pollution_index' not in data.columns:
        data['pollution_index'] = data['pm2_5'] * 0.5 + data['pm10'] * 0.3 + data['pm1_0'] * 0.2
    
    X = data[['pm2_5', 'pm1_0', 'pm10', 'lat', 'long']]
    y = data['pollution_index']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

# Generate pollution index prediction and message
def predict_index(request):
    model, scaler = train_model()

    if request.method == 'POST':
        pm2_5 = float(request.POST['pm2_5'])
        pm1_0 = float(request.POST['pm1_0'])
        pm10 = float(request.POST['pm10'])
        lat = float(request.POST['lat'])
        long = float(request.POST['long'])

        input_data = np.array([[pm2_5, pm1_0, pm10, lat, long]])
        input_scaled = scaler.transform(input_data)

        predicted_pollution_index = model.predict(input_scaled)[0]

        # Determine pollution level message
        if predicted_pollution_index <= 50:
            pollution_message = "Good"
        elif 51 <= predicted_pollution_index <= 100:
            pollution_message = "Moderate"
        elif 101 <= predicted_pollution_index <= 150:
            pollution_message = "Unhealthy for Sensitive Groups"
        elif 151 <= predicted_pollution_index <= 200:
            pollution_message = "Unhealthy"
        elif 201 <= predicted_pollution_index <= 300:
            pollution_message = "Very Unhealthy"
        else:
            pollution_message = "Hazardous"

        # Plot graph
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(x=['Predicted Pollution Index'], y=[predicted_pollution_index], ax=ax, color='blue')
        ax.set_title('Predicted Pollution Index')
        ax.set_ylabel('Pollution Index')
        plt.tight_layout()

        # Save the plot to a PNG image in memory
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Encode the image to base64
        graph = base64.b64encode(image_png).decode('utf-8')

        # Pass data to template
        context = {
            'prediction': predicted_pollution_index,
            'pollution_message': pollution_message,
            'input_data': request.POST,
            'graph': graph
        }
        return render(request, 'calculator/result.html', context)

    return render(request, 'calculator/index.html')

def chart(request):
    return render(request, 'calculator/chart.html')  # Render the chart.html

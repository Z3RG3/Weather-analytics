# 🏍️🚲 Weather Analytics for Optimal Biking

<div align="center">
  <img src="https://www.invent.ai/hubfs/weather-article-banner-2.png" alt="Weather Analytics Banner" width="800">
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
  ![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)
  ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white)
  ![Weather API](https://img.shields.io/badge/Weather_API-orange?style=for-the-badge)
  
  *An intelligent weather analysis system that determines optimal biking conditions in the upcoming 72 hours*
</div>

## 📊 Project Overview

Weather Analytics is a personal portfolio project that demonstrates data processing and visualization skills using real-time weather data. The system analyzes upcoming weather conditions to identify the best times for biking based on customizable parameters including temperature, wind speed, precipitation, and humidity.

> **"Life is like riding a bicycle. To keep your balance, you must keep moving."** - Albert Einstein

## ✨ Features

- **Real-time Weather Data Analysis**: Processes weather forecast data for the next 72 hours
- **Customizable Biking Parameters**: Set your preferences for ideal riding conditions
- **Bikeability Score™**: Proprietary algorithm that calculates optimal biking windows
- **Interactive Visualizations**: Rich graphical representations of weather patterns
- **Time-Series Analysis**: Trend identification and forecasting
- **Personalized Recommendations**: Get specific time windows for your bike rides

## 🖥️ Tech Stack

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation and numerical operations
- **Matplotlib & Seaborn**: Data visualization
- **Weather API**: Real-time weather data source
- **Jupyter Notebooks**: Interactive development and presentation

## 📈 Exploratory Data Analysis (EDA)

The heart of this project is the comprehensive analysis of weather patterns. The EDA process includes:

<img src="https://raw.githubusercontent.com/Z3RG3/Weather-analytics/main/assets/visualization_sample.png" alt="Visualization Sample" align="right" width="300">

- Data cleaning and preprocessing
- Statistical analysis of key weather metrics
- Visualization of temperature, wind, and precipitation trends
- Time-series decomposition to identify patterns
- Correlation analysis between different weather parameters

The analysis provides insights into how weather conditions change throughout the day and which periods might be most suitable for outdoor activities like biking.

## 🚴 Bikeability Score™ Algorithm

The core of the project is the Bikeability Score™ algorithm that considers:

- Temperature ranges (customizable comfort zones)
- Wind speed thresholds
- Precipitation probability and intensity
- Humidity levels
- Daylight availability

Each time period receives a score from 0-100, with recommendations categorized as:

| Score Range | Recommendation |
|-------------|----------------|
| 80-100      | Perfect biking conditions! 🟢 |
| 60-79       | Good conditions with minor compromises 🟡 |
| 40-59       | Acceptable if you're determined 🟠 |
| 0-39        | Not recommended for biking 🔴 |

## 🗂️ Project Structure

```
Weather-analytics/
├── Data/
│   └── api_response2025-04-17.json
├── Notebooks/
│   ├── EDA_and_Visualization.ipynb
│   └── Bikeability_Score_Development.ipynb
├── Scripts/
│   ├── analysisJson.py
│   ├── bikeability_calculator.py
│   └── visualization.py
├── assets/
│   ├── banner.png
│   └── visualization_sample.png
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Required packages listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Z3RG3/Weather-analytics.git
   cd Weather-analytics
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook:
   ```bash
   jupyter notebook Notebooks/EDA_and_Visualization.ipynb
   ```

### Usage

1. Customize your biking preferences in the notebook:
   ```python
   biking_preferences = {
       'min_temp_c': 15,       # Minimum comfortable temperature (°C)
       'max_temp_c': 30,       # Maximum comfortable temperature (°C)
       'max_wind_kph': 20,     # Maximum acceptable wind speed (km/h)
       'max_precip_mm': 0.5,   # Maximum acceptable precipitation (mm)
       'max_humidity': 80,     # Maximum acceptable humidity (%)
       'daylight_required': True  # Whether daylight is required
   }
   ```

2. Run the analysis to get personalized biking recommendations:
   ```python
   optimal_times = calculate_bikeability_score(weather_data, biking_preferences)
   ```

## 📊 Sample Visualizations

<div align="center">
  <img src="https://raw.githubusercontent.com/Z3RG3/Weather-analytics/main/assets/temperature_trend.png" width="400">
  <img src="https://raw.githubusercontent.com/Z3RG3/Weather-analytics/main/assets/bikeability_heatmap.png" width="400">
</div>

## 🔮 Future Enhancements

- [ ] Real-time API integration
- [ ] Mobile app for on-the-go recommendations
- [ ] Machine learning to improve predictions
- [ ] User profiles to save preferences
- [ ] Integration with fitness tracking apps
- [ ] Interactive web dashboard

## 📝 Learning Outcomes

This project demonstrates:
- Working with real-world API data
- Data cleaning and preprocessing techniques
- Time-series analysis and visualization
- Algorithm development for practical applications
- Building customizable, user-centered data products

## 🤝 Contributing

While this is primarily a personal portfolio project, suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.


## 👨‍💻 About the Author

I'm an aspiring data scientist passionate about creating practical applications that solve everyday problems. This project combines my love for motorbiking with my interest in data analysis and weather patterns.

---

<div align="center">
  <i>If you found this project interesting, please consider giving it a ⭐!</i>
</div>

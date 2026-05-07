# Weather-Data-Analysis-Using-Python

# Weather Data Analysis Using Python

## Project Overview
This project analyzes a weather dataset using Python and Pandas.

The analysis includes:
- Data cleaning
- Finding unique values
- Filtering weather conditions
- Statistical operations
- GroupBy analysis
- Conditional filtering

## Technologies Used
- Python
- Pandas

## Dataset
The dataset contains weather information such as:
- Temperature
- Humidity
- Wind Speed
- Visibility
- Pressure
- Weather Conditions

## Features Implemented

### Basic Data Exploration
- Display dataset head
- Check shape and columns
- View datatypes
- Count unique values

### Weather Analysis
- Find clear weather records
- Analyze snow conditions
- Fog condition filtering
- Wind speed analysis

### Statistical Analysis
- Mean visibility
- Pressure standard deviation
- Humidity variance

### Conditional Queries
Examples:
- Wind speed greater than 24 km/h
- Visibility equal to 25
- Weather clear with humidity above 50

## Sample Code

```python
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]

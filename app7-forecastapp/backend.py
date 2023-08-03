import requests

API_KEY = "a48045891cdc49ff97054412230308"

# Add title, text input, slider, selectbox, and subheader
def get_data(place, forecast_days=None):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={place}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
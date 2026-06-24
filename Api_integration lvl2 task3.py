import requests

country = input("enter country name: ").strip()   # 🔥 FIX HERE

url = "https://restcountries.com/v3.1/name/" + country
response = requests.get(url)

print(response.status_code)

try:
    data = response.json()

    if response.status_code == 200 and isinstance(data, list):

        country_data = data[0]

        print("\nCountry Details:")
        print("Name:", country_data["name"]["common"])
        print("Capital:", country_data["capital"][0])
        print("Region:", country_data["region"])
        print("Population:", country_data["population"])

    else:
        print("Failed to fetch data or invalid country")

except Exception as e:
    print("Error:", e)
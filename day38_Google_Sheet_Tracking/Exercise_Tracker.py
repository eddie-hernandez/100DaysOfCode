import requests
from datetime import datetime

GENDER = "GENDER"
WEIGHT_KG = 123
HEIGHT_CM = 123
AGE = 123

NUTRITIONIX_APP_ID = "NUTRITIONIX_APP_ID"
NUTRITIONIX_API_KEY = "1NUTRITIONIX_API_KEY"
SHEETY_BEARER_TOKEN = "SHEETY_BEARER_TOKEN"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "sheet_endpoint"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Bearer Token
bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)

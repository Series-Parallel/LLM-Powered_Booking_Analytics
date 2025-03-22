# Task 5: (Part 2) Performance Evaluation - Calculating response time of the api

import requests
import time

url = "http://127.0.0.1:8000/ask"
payload = {"query": "Do you have rooms available next weekend?"}

start_time = time.time()
response = requests.post(url, json=payload)
end_time = time.time()

print("Response Time:", end_time - start_time, "seconds")
print("Response:", response.json())


# Response Time: 55.93956136703491 seconds
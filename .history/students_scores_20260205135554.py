import requests
url = "https://raw.githubusercontent.com/Test-pen/AI-ML-Trainee-/refs/heads/main/students.json"
r = requests.get(url)
print(r.json())

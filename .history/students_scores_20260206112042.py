import requests
import matplotlib.pyplot as plt

#fetch dataset from API
url = "https://raw.githubusercontent.com/Test-pen/AI-ML-Trainee-/refs/heads/main/students.json"
response = requests.get(url)
data = response.json()

students = []
scores = []

# Step 2: Process dataset
for student in data:
    students.append(student["name"])
    scores.append(student["score"])

# Step 3: Calculate average
average = sum(scores) / len(scores)
print("Average Score:", average)

# Step 4: Visualization
plt.bar(students, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()

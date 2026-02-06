import matplotlib.pyplot as plt

students = ["Rahul", "Anita", "John", "Sara"]
scores = [85, 92, 78, 88]

average = sum(scores) / len(scores)
print("Average Score:", average)

plt.bar(students, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()

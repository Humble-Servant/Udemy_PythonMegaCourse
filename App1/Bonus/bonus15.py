import json

with open('App1\\Data\\questions.json', 'r') as file:
    content = file.read()

score = 0
data = json.loads(content)
print()
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"], 1):
        print(f"{index} - {alternative}")
    user_choice = int(input("\nEnter your answer: "))
    question["user_choice"] = user_choice

print()

for index, question in enumerate(data, 1):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct!"
    else:
        result = "Wrong!"
    message = f"{index} - {result} You answered {question['user_choice']}, Correct answer was {question['correct_answer']}"
    print(message)

print("===================")
print(f"    Score= {score}/{len(data)}")
print("===================")
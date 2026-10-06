import random

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "new delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars"
    },
    {
        "question": "How many days are there in a week?",
        "answer": "7"
    },
    {
        "question": "What is the largest ocean in the world?",
        "answer": "pacific ocean"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "answer": "charles babbage"
    },
    {
        "question": "How many continents are there in the world?",
        "answer": "7"
    },
    {
        "question": "Which gas do humans need to breathe?",
        "answer": "oxygen"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "jupiter"
    },
    {
        "question": "How many hours are there in a day?",
        "answer": "24"
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "answer": "lion"
    }
]

print("===== GENERAL KNOWLEDGE QUIZ =====")

score = 0

selected_questions = random.sample(questions, 5)

for i, item in enumerate(selected_questions, start=1):

    print(f"\n{i}. {item['question']}")

    answer = input("Your answer: ")

    if answer.strip().lower() == item["answer"]:
        print("Correct! ✓")
        score += 1
    else:
        print("Wrong! ✗")
        print("Correct answer:", item["answer"])

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent! 🎉")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")
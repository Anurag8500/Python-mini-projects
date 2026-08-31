print("=== Python Quiz ===")

questions = [
    {
        "question": "Which data structure stores key-value pairs?",
        "options": [
            "A. List",
            "B. Tuple",
            "C. Dictionary",
            "D. Set"
        ],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. func",
            "B. define",
            "C. def",
            "D. function"
        ],
        "answer": "C"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": [
            "A. add()",
            "B. append()",
            "C. insert()",
            "D. push()"
        ],
        "answer": "B"
    },
    {
        "question": "What does len() return?",
        "options": [
            "A. The type of an object",
            "B. The largest value",
            "C. The number of items",
            "D. The memory size"
        ],
        "answer": "C"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": [
            "A. //",
            "B. <!--",
            "C. #",
            "D. --"
        ],
        "answer": "C"
    }
]


score = 0

for number, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {number}/{len(questions)}")
    print(question_data["question"])

    for option in question_data["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == question_data["answer"]:
        print("✓ Correct!")
        score += 1
    else:
        print(
            f"✗ Incorrect. "
            f"The correct answer is {question_data['answer']}."
        )


percentage = (score / len(questions)) * 100

print("\n=== Final Result ===")
print(f"Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Result: Excellent!")
elif percentage >= 60:
    print("Result: Good job!")
elif percentage >= 40:
    print("Result: Keep practicing!")
else:
    print("Result: More practice needed.")


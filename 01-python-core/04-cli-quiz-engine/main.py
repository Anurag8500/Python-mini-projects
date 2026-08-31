import random


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
    },
    {
        "question": "Which keyword is used to repeat a block of code while a condition is true?",
        "options": [
            "A. repeat",
            "B. loop",
            "C. while",
            "D. during"
        ],
        "answer": "C"
    },
    {
        "question": "Which data type represents True or False?",
        "options": [
            "A. int",
            "B. bool",
            "C. str",
            "D. float"
        ],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": [
            "A. ^",
            "B. **",
            "C. //",
            "D. %%"
        ],
        "answer": "B"
    }
]


random.shuffle(questions)

score = 0
wrong_answers = []


for number, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {number}/{len(questions)}")
    print(question_data["question"])

    for option in question_data["options"]:
        print(option)

    valid_options = ["A", "B", "C", "D"]

    while True:
        user_answer = input("Your answer: ").strip().upper()

        if user_answer in valid_options:
            break

        print("Invalid answer. Please enter A, B, C, or D.")

    correct_answer = question_data["answer"]

    if user_answer == correct_answer:
        print("✓ Correct!")
        score += 1
    else:
        print(f"✗ Incorrect. Correct answer: {correct_answer}")
        wrong_answers.append({
            "question": question_data["question"],
            "your_answer": user_answer,
            "correct_answer": correct_answer
        })


total_questions = len(questions)
wrong_count = total_questions - score
percentage = (score / total_questions) * 100


print("\n=== Final Result ===")
print(f"Score: {score}/{total_questions}")
print(f"Correct: {score}")
print(f"Incorrect: {wrong_count}")
print(f"Percentage: {percentage:.2f}%")


if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good job!")
elif percentage >= 40:
    print("Performance: Keep practicing!")
else:
    print("Performance: More practice needed.")


if wrong_answers:
    print("\n=== Review Incorrect Answers ===")

    for number, result in enumerate(wrong_answers, start=1):
        print(f"\n{number}. {result['question']}")
        print(f"   Your answer: {result['your_answer']}")
        print(f"   Correct answer: {result['correct_answer']}")
else:
    print("\nPerfect score! You got every question correct.")


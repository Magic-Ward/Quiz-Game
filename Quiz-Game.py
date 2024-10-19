# Simple Quiz Game

score = 0
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet?", "Jupiter"),
    ("Who wrote 'Hamlet'?", "Shakespeare"),
]

for question, correct_answer in questions:
    answer = input(question + " ")
    if answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your final score is: {score}/{len(questions)}")

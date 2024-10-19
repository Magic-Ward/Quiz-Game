# Simple Quiz Game
import easygui

score = 0
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet?", "Jupiter"),
    ("Who wrote 'Hamlet'?", "Shakespeare"),
]

for question, correct_answer in questions:
    answer = easygui.enterbox(question, "Give your answers")
   
    if answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

easygui.msgbox(f"Your final score is: {score}/{len(questions)}", "Result")


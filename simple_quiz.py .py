def check_ans(question, answer, score):
    still_answering = True
    attempt = 0
    while still_answering and attempt < 3:  # Limited to 3 attempts
        if question.lower() == answer.lower():
            print("Correct Answer!")
            score += 1
            still_answering = False
        else:
            if attempt < 2:
                question = input("Sorry, that's incorrect. Try again: ")
            attempt += 1
    if attempt == 3:
        print("The correct answer is:", answer)
    return score
    
score = 0
print("Answer the Questions!")

questions = [
    ("Who developed the Python language?", "Guido van Rossum"),
    ("What is the correct extension of the Python file?", ".py"),
    ("What do we use to define a block of code in Python language?", "Indentation"),
    ("Which type of programming does Python support?", "object-oriented, structured, and functional programming"),
    ("Is Python code compiled or interpreted?", "Both compiled and interpreted"),
    ("Which keyword is used for function in Python language?", "def"),
    ("Which character is used to give single-line comments in Python?", "#"),
    ("What does pip stand for in Python?", "Preferred Installer Program"),
    ("What is the definition for packages in Python?", "A folder of python programs is called packages in python"),
    ("In which year was the Python language developed?", "1989")
]

for idx, (que_text, ans) in enumerate(questions, 1):
    response = input(f"Question {idx}: {que_text} ")
    score = check_ans(response, ans, score)

print(f"Your total score out of {len(questions)} is {score}.")

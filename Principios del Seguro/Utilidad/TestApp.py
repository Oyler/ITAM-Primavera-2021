import nltk


def grade_question(answer, correct_answer, points):
    d = nltk.edit_distance(correct_answer, answer)
    out = " "
    score = 0
    if d == 0:
        score = points
        out = f'Correct!    points: {score}/{points}'
    elif 0 < d <= 3:
        score = points // 2
        out = f'Correct     points: {score}/{points}'
    else:
        out = f'Incorrect!      points: {score}/{points}'
    return out, score


def create_questionnaire(num_questions):
    questions = []
    for k in range(num_questions):
        q = input("Enter the question:\n")
        a = input("Enter the answer:\n")
        p = int(input("Question maximum score:  "))
        temp = [q, a, p]
        questions.append(temp)

    return questions


def add_question(questions):
    q = input("Enter the question:\n")
    a = input("Enter the answer:\n")
    p = int(input("Question maximum score:  "))
    new_question = [q, a, p]
    questions.append(new_question)


def remove_question(questions, number):
    questions.pop(number)


def print_list(questions):
    for k in range(len(questions)):
        print(f'Question No.{k + 1}')
        print(f'Q: {questions[k][0]}')
        print(f'A: {questions[k][1]}')
        print(f'Points: {questions[k][2]}')
        print(" ")


def run_test(questions):
    answers = len(questions) * [" "]
    total = 0
    score = 0
    for j in range(len(questions)):
        total += questions[j][2]
    for i in range(len(questions)):
        print(questions[i][0])
        answers[i] = input("Enter answer:\n")
        g = grade_question(answers[i], questions[i][1], questions[i][2])[0]
        score += grade_question(answers[i], questions[i][1], questions[i][2])[1]
        print(g)
    print(f'You got {score} out of {total} points')

def menu():

    input("press any key to continue")
    while True:
        print("MENU")
        print("1. Create a questionnaire")
        print("2. Show questions")
        print("3. Add question")
        print("4. Remove question")
        print("5. Run test")
        print("6. Exit")

        flag = int(input("Awaiting input: "))
        print("\n")
        if flag == 6:
            break
        else:
            if flag == 1:
                num_questions = int(input("How many questions?\n"))
                questionnaire = create_questionnaire(num_questions)
                print("\n")
            elif flag == 2:
                print_list(questionnaire)
                print("\n")
            elif flag == 3:
                add_question(questionnaire)
                print("\n")
            elif flag == 4:
                question = int(input("Enter the number of the question to remove: ")) - 1
                remove_question(questionnaire, question)
                print("\n")
            elif flag == 5:
                run_test(questionnaire)
                print("\n")
            else:
                break



menu()


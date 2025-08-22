data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def quiz():
    correct = 0
    wrong = 0
    wrong_answers = []

    print(" Welcome to the Star Wars Quiz! ")
    print("Answer the following questions:\n")

    for item in data:
        answer = input(item["question"] + " ")
        if answer.lower() == item["answer"].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(" Wrong!\n")
            wrong += 1
            wrong_answers.append([item["question"], answer, item["answer"]])

    print(f"=== RESULTS ===")
    print(f"You got {correct} correct and {wrong} wrong.")

    if wrong > 0:
        print("\nQuestions you missed:")
        for q, your, right in wrong_answers:
            print(f"Q: {q}")
            print(f"Your answer: {your}")
            print(f"Correct answer: {right}")
            print()

    if wrong > 3:
        play_again = input("You missed more than 3. Play again? (yes/no): ")
        if play_again.lower() == "yes":
            quiz()
        else:
            print("Thanks for playing!")


quiz()
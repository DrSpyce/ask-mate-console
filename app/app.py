from data import models


def display_questions():
    questions = models.get_questions()
    for question in questions:
        print(f"{question['id']}. {question['title']}")


def display_question_with_answers(question_id):
    question, answers = models.get_question_with_answers(question_id)
    if question:
        print("\nQuestion:")
        print(f"{question[0]['title']}\n{question[0]['content']}\n")

        if answers:
            print("Answers:")
            for answer in answers:
                print(f"{answer['content']}")
        else:
            print("No answers yet.")
    else:
        print("Question not found.")


if __name__ == '__main__':
    while True:
        print("\n=== Console Ask Mate application ===")
        print("1. View List of Questions")
        print("2. View Questions with Answers")
        print("3. View Question and Answers")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            display_questions()
        elif choice == '2':
            display_questions()
        elif choice == '3':
            question_id = int(input("Write id of question: "))
            display_question_with_answers(question_id)
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")

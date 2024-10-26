import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)

    def shuffle_options(self, options):
        random.shuffle(options)
        return options

    def ask_question(self, question_data):
        question, options, correct_answer = question_data
        shuffled_options = self.shuffle_options(options.copy())  # Shuffle options for this question
        print(f"\n{question}")
        for i, option in enumerate(shuffled_options):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Enter the option number: "))
            selected_option = shuffled_options[answer - 1]
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
            return False

        if selected_option == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return False

    def run_quiz(self):
        random.shuffle(self.questions)  # Shuffle the questions before starting the quiz
        for cnt, question_data in enumerate(self.questions):
            if cnt == 10:  # Limit to 10 questions
                break
            if self.ask_question(question_data):
                self.score += 1

    def display_result(self):
        percentage = (self.score / 10) * 100
        print(f"\nYou got {self.score} out of {10} correct.")
        print(f"Your percentage: {percentage:.2f}%")

# Define the quiz questions
quiz_questions = [
    ("What is the capital of Japan?", ["Seoul", "Beijing", "Tokyo", "Bangkok"], "Tokyo"),
    ("Which element has the atomic number 1?", ["Helium", "Hydrogen", "Oxygen", "Lithium"], "Hydrogen"),
    ("Who was the first person to walk on the moon?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"], "Neil Armstrong"),
    ("What is the hardest natural mineral?", ["Ruby", "Sapphire", "Diamond", "Emerald"], "Diamond"),
    ("In which year did the Titanic sink?", ["1905", "1912", "1918", "1920"], "1912"),
    ("Which artist is known for the 'Starry Night' painting?", ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Henri Matisse"], "Vincent van Gogh"),
    ("What is the smallest continent by land area?", ["Africa", "Australia", "Europe", "Antarctica"], "Australia"),
    ("Which planet is closest to the sun?", ["Venus", "Earth", "Mercury", "Mars"], "Mercury"),
    ("What is the main ingredient in traditional hummus?", ["Chickpeas", "Lentils", "Beans", "Peas"], "Chickpeas"),
    ("Who wrote the novel '1984'?", ["Aldous Huxley", "George Orwell", "Ray Bradbury", "F. Scott Fitzgerald"], "George Orwell"),
    ("What is the largest organ in the human body?", ["Heart", "Liver", "Skin", "Lung"], "Skin"),
    ("Which scientist is famous for the laws of motion?", ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Stephen Hawking"], "Isaac Newton"),
    ("What is the primary language spoken in Argentina?", ["Spanish", "Portuguese", "English", "French"], "Spanish"),
    ("What is the currency of Japan?", ["Yen", "Won", "Dollar", "Rupee"], "Yen"),
    ("Who is known for the theory of evolution by natural selection?", ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Albert Einstein"], "Charles Darwin")
]

# Create a quiz instance and run it
quiz = Quiz(quiz_questions)
quiz.run_quiz()
quiz.display_result()
import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Python Quiz")
        self.parent.geometry("750x400")

        self.bg_color = "#e0f7fa"
        self.parent.config(bg=self.bg_color)

        self.frame = tk.Frame(self.parent, bg=self.bg_color)
        self.frame.pack(expand=True, fill='both')

        self.start_label = tk.Label(self.frame, text="Welcome to Python Quiz", font=("Arial", 18), bg=self.bg_color)
        self.start_label.pack(pady=20)

        self.play_button = tk.Button(self.frame, text="Play", font=("Arial", 14), width=15, command=self.start_quiz)
        self.play_button.pack(pady=10)

        self.quit_button = tk.Button(self.frame, text="Quit", font=("Arial", 14), width=15, command=self.quit_app)
        self.quit_button.pack(pady=10)

    def start_quiz(self):
        self.frame.destroy()
        self.questions = [
            {
                "question": "Which of the following is an invalid variable name?",
                "options": ["my_var", "1stVar", "var_2", "_variable"],
                "correct_answer": "1stVar"
            },
            {
                "question": "What does the 'range' function in Python return?",
                "options": ["List", "Tuple", "Dictionary", "Range object"],
                "correct_answer": "Range object"
            },
            {
                "question": "Which of the following is a mutable data type?",
                "options": ["Tuple", "List", "Set", "String"],
                "correct_answer": "List"
            },
            {
                "question": "What does the 'continue' statement do in a loop?",
                "options": ["Ends the loop", "Skips the rest ", "Jumps to a specified label", "Raises an exception"],
                "correct_answer": "Skips the rest "
            },
            {
                "question": "What does the 'len()' function do in Python?",
                "options": ["Returns the length of a string", "Returns the length of a list", "Returns the number of elements in a tuple", "All of the above"],
                "correct_answer": "All of the above"
            },
            {
                "question": "What is the result of 3 * 'abc'?",
                "options": ["'abcabcabc'", "TypeError", "'aaaabbbbcccc'", "'abcabc'"],
                "correct_answer": "TypeError"
            },
            {
                "question": "What is the correct way to declare a tuple with one element?",
                "options": ["(1)", "(1,)", "1,", "[1]"],
                "correct_answer": "(1,)"
            },
            {
                "question": "What does the 'sorted()' function do in Python?",
                "options": ["Sorts a list in ascending order", "Sorts a list in descending order", "Returns a new sorted list", "All of the above"],
                "correct_answer": "All of the above"
            },
            {
                "question": "What is the result of 3 ** 2?",
                "options": ["9", "6", "32", "27"],
                "correct_answer": "9"
            },
            {
                "question": "What does the 'pop()' method do in Python?",
                "options": ["Removes and returns the last element of a list", "Removes and returns the first element of a list", "Inserts an element at the specified position", "None of the above"],
                "correct_answer": "Removes and returns the last element of a list"
            },
            {
                "question": "What is the correct syntax for a set comprehension?",
                "options": ["{x for x in range(10)}", "(x for x in range(10))", "{x: x for x in range(10)}", "{x: for x in range(10)}"],
                "correct_answer": "{x for x in range(10)}"
            },
            {
                "question": "What does the 'keys()' method return for a dictionary?",
                "options": ["Returns a list of all keys", "Returns a list of all values", "Returns a list of tuples containing key-value pairs", "Returns a generator object"],
                "correct_answer": "Returns a list of all keys"
            },
            {
                "question": "Which of the following is a Python reserved keyword?",
                "options": ["var", "lambda", "function", "do"],
                "correct_answer": "lambda"
            },
            {
                "question": "What is the output of the code: print('hello'[::-1])?",
                "options": ["'hello'", "'olleh'", "'olle'", "'hell'"],
                "correct_answer": "'olleh'"
            },
            {
                "question": "What does the 'strip()' method do in Python?",
                "options": ["Removes leading and trailing whitespace", "Returns a copy of the string with all occurrences of a substring replaced", "Splits the string into a list", "None of the above"],
                "correct_answer": "Removes leading and trailing whitespace"
            },
            {
                "question": "What is the result of [1, 2, 3] + [4, 5, 6]?",
                "options": ["[1, 2, 3, 4, 5, 6]", "[1, 2, 3, [4, 5, 6]]", "[1, 2, 3, 4, 5, 6,]", "TypeError"],
                "correct_answer": "[1, 2, 3, 4, 5, 6]"
            },
            {
                "question": "What does the 'join()' method do in Python?",
                "options": ["Concatenates strings", "Joins elements of a list into a single string", "Joins elements of a tuple into a single string", "None of the above"],
                "correct_answer": "Joins elements of a list into a single string"
            },
            {
                "question": "What is the result of 'hello'.upper()?",
                "options": ["'hello'", "'HELLO'", "'Hello'", "'hello'"],
                "correct_answer": "'HELLO'"
            },
            {
                "question": "What is the correct way to declare an empty dictionary?",
                "options": ["{}", "()", "[]", "{()}"],
                "correct_answer": "{}"
            },
            {
                "question": "What does the 'map()' function do in Python?",
                "options": ["Applies a function to every item of an iterable", "Returns a new list containing the results of applying a function to the items of the input lists", "Filters the elements of an iterable based on a function", "None of the above"],
                "correct_answer": "Applies a function to every item of an iterable"
            }
        ]
        
        
        self.current_question = 0
        self.score = 0

        self.frame = tk.Frame(self.parent, bg=self.bg_color)
        self.frame.pack(expand=True, fill='both')

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 14), bg=self.bg_color)
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.frame, text="", font=("Arial", 12), width=70, command=lambda i=i: self.check_answer(i))
            button.pack(pady=15)
            self.option_buttons.append(button)

        self.display_question()

    def quit_app(self):
        self.parent.destroy()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_result()

    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question]
        selected_option = question_data["options"][selected_index]
        if selected_option == question_data["correct_answer"]:
            self.score += 1
        self.current_question += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}")
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

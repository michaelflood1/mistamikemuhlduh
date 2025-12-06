import random
import json
import os
from typing import List, Dict, Union

class Question:
    """Base class for quiz questions"""
    def __init__(self, question_text: str, correct_answer: Union[str, bool], question_type: str):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.question_type = question_type
    
    def check_answer(self, user_answer: Union[str, bool]) -> bool:
        """Check if the user's answer is correct"""
        if self.question_type == "true_false":
            return str(user_answer).lower() == str(self.correct_answer).lower()
        else:
            return user_answer.upper() == self.correct_answer.upper()
    
    def to_dict(self) -> Dict:
        """Convert question to dictionary for saving"""
        return {
            "question_text": self.question_text,
            "correct_answer": self.correct_answer,
            "question_type": self.question_type
        }

class MultipleChoiceQuestion(Question):
    """Multiple choice question with options A, B, C, D"""
    def __init__(self, question_text: str, options: Dict[str, str], correct_answer: str):
        super().__init__(question_text, correct_answer, "multiple_choice")
        self.options = options
    
    def display(self):
        """Display the question and options"""
        print(f"\n{self.question_text}")
        for key in sorted(self.options.keys()):
            print(f"  {key}. {self.options[key]}")
    
    def to_dict(self) -> Dict:
        """Convert to dictionary including options"""
        data = super().to_dict()
        data["options"] = self.options
        return data

class TrueFalseQuestion(Question):
    """True/False question"""
    def __init__(self, question_text: str, correct_answer: bool):
        super().__init__(question_text, correct_answer, "true_false")
    
    def display(self):
        """Display the question"""
        print(f"\n{self.question_text}")
        print("  A. True")
        print("  B. False")

class QuizApp:
    """Main quiz application"""
    def __init__(self, filename: str = "quiz_questions.json"):
        self.filename = filename
        self.questions: List[Question] = []
        self.load_questions()
    
    def load_questions(self):
        """Load questions from JSON file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for q_data in data:
                        if q_data["question_type"] == "multiple_choice":
                            self.questions.append(
                                MultipleChoiceQuestion(
                                    q_data["question_text"],
                                    q_data["options"],
                                    q_data["correct_answer"]
                                )
                            )
                        elif q_data["question_type"] == "true_false":
                            self.questions.append(
                                TrueFalseQuestion(
                                    q_data["question_text"],
                                    q_data["correct_answer"]
                                )
                            )
                print(f"Loaded {len(self.questions)} questions from {self.filename}")
            except Exception as e:
                print(f"Error loading questions: {e}")
    
    def save_questions(self):
        """Save questions to JSON file"""
        try:
            data = [q.to_dict() for q in self.questions]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Saved {len(self.questions)} questions to {self.filename}")
        except Exception as e:
            print(f"Error saving questions: {e}")
    
    def add_multiple_choice_question(self):
        """Add a new multiple choice question"""
        print("\n--- Add Multiple Choice Question ---")
        question_text = input("Enter the question: ").strip()
        
        options = {}
        for letter in ['A', 'B', 'C', 'D']:
            option = input(f"Enter option {letter}: ").strip()
            if option:  # Allow fewer than 4 options
                options[letter] = option
        
        if not options:
            print("No options provided. Question not added.")
            return
        
        while True:
            correct = input("Enter the correct answer (A/B/C/D): ").upper()
            if correct in options:
                break
            print(f"Invalid answer. Please choose from: {', '.join(options.keys())}")
        
        self.questions.append(MultipleChoiceQuestion(question_text, options, correct))
        print("Question added successfully!")
    
    def add_true_false_question(self):
        """Add a new true/false question"""
        print("\n--- Add True/False Question ---")
        question_text = input("Enter the question: ").strip()
        
        while True:
            answer = input("Is the answer True or False? ").lower()
            if answer in ['true', 'false', 't', 'f']:
                correct = answer in ['true', 't']
                break
            print("Please enter 'True' or 'False'")
        
        self.questions.append(TrueFalseQuestion(question_text, correct))
        print("Question added successfully!")
    
    def run_quiz(self, randomize: bool = False):
        """Run the quiz with all questions"""
        if not self.questions:
            print("No questions available. Please add some questions first.")
            return
        
        questions_to_ask = self.questions.copy()
        if randomize:
            random.shuffle(questions_to_ask)
        
        score = 0
        total = len(questions_to_ask)
        
        print(f"\n{'='*50}")
        print(f"Starting quiz with {total} questions")
        print(f"Mode: {'Random' if randomize else 'Sequential'}")
        print(f"{'='*50}")
        
        for i, question in enumerate(questions_to_ask, 1):
            print(f"\nQuestion {i} of {total}")
            print("-" * 30)
            question.display()
            
            if isinstance(question, TrueFalseQuestion):
                while True:
                    answer = input("\nYour answer (A for True, B for False): ").upper()
                    if answer in ['A', 'B']:
                        user_answer = answer == 'A'
                        break
                    print("Please enter A or B")
            else:
                while True:
                    answer = input("\nYour answer: ").upper()
                    if isinstance(question, MultipleChoiceQuestion):
                        if answer in question.options:
                            user_answer = answer
                            break
                        print(f"Please enter one of: {', '.join(question.options.keys())}")
            
            if question.check_answer(user_answer):
                print("✓ Correct!")
                score += 1
            else:
                print("✗ Incorrect!")
                if isinstance(question, TrueFalseQuestion):
                    print(f"The correct answer is: {question.correct_answer}")
                else:
                    print(f"The correct answer is: {question.correct_answer}")
        
        print(f"\n{'='*50}")
        print(f"Quiz Complete!")
        print(f"Your score: {score}/{total} ({score/total*100:.1f}%)")
        print(f"{'='*50}")
    
    def view_questions(self):
        """View all questions"""
        if not self.questions:
            print("No questions available.")
            return
        
        print(f"\n--- All Questions ({len(self.questions)} total) ---")
        for i, question in enumerate(self.questions, 1):
            print(f"\n{i}. [{question.question_type.upper()}]")
            print(f"   Q: {question.question_text}")
            if isinstance(question, MultipleChoiceQuestion):
                for key, value in sorted(question.options.items()):
                    marker = "→" if key == question.correct_answer else " "
                    print(f"   {marker} {key}. {value}")
            else:
                print(f"   Answer: {question.correct_answer}")
    
    def delete_question(self):
        """Delete a question"""
        if not self.questions:
            print("No questions to delete.")
            return
        
        self.view_questions()
        try:
            num = int(input("\nEnter question number to delete (0 to cancel): "))
            if num == 0:
                return
            if 1 <= num <= len(self.questions):
                deleted = self.questions.pop(num - 1)
                print(f"Deleted: {deleted.question_text}")
                self.save_questions()
            else:
                print("Invalid question number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def main_menu(self):
        """Display main menu and handle user choices"""
        while True:
            print(f"\n{'='*50}")
            print("QUIZ APPLICATION MAIN MENU")
            print(f"{'='*50}")
            print(f"Questions loaded: {len(self.questions)}")
            print("\n1. Add Multiple Choice Question")
            print("2. Add True/False Question")
            print("3. Take Quiz (Sequential)")
            print("4. Take Quiz (Random)")
            print("5. View All Questions")
            print("6. Delete a Question")
            print("7. Save and Exit")
            print("8. Exit without Saving")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                self.add_multiple_choice_question()
            elif choice == '2':
                self.add_true_false_question()
            elif choice == '3':
                self.run_quiz(randomize=False)
            elif choice == '4':
                self.run_quiz(randomize=True)
            elif choice == '5':
                self.view_questions()
            elif choice == '6':
                self.delete_question()
            elif choice == '7':
                self.save_questions()
                print("Goodbye!")
                break
            elif choice == '8':
                confirm = input("Exit without saving? (y/n): ").lower()
                if confirm == 'y':
                    print("Goodbye!")
                    break
            else:
                print("Invalid choice. Please try again.")

def main():
    """Main entry point"""
    print("Welcome to the Quiz Application!")
    print("-" * 50)
    
    # Allow user to specify custom filename
    use_custom = input("Use custom filename? (y/n, default: n): ").lower()
    if use_custom == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if filename:
            filename = f"{filename}.json"
        else:
            filename = "quiz_questions.json"
    else:
        filename = "quiz_questions.json"
    
    app = QuizApp(filename)
    app.main_menu()

if __name__ == "__main__":
    main()
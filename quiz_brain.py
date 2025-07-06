class QuizBrain:
    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def next_question(self):
        question = self.q_list[self.q_num]
        user_answer = input(f"Q.{self.q_num+1}: {question.text} (True/False): ").title()
        self.q_num += 1
        return user_answer

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def check_answer(self):
        answer = self.next_question()
        if answer == self.q_list[self.q_num-1].ans:
            self.score += 1
            print(f"Correct! Score: {self.score}/{self.q_num}\n")
        else:
            print(f"Incorrect. Score: {self.score}/{self.q_num}\n")



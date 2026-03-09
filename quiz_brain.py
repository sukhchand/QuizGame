import html

class QuizBrain:
    def __init__(self, questions_list ):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return len(self.questions_list) != self.question_number

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question["question"])
        return f"Q.{self.question_number}: {q_text} (True/False): "
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            return True
        else:
            return False

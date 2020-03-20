class UserInputService:
    def run(self):
        self.get_answer_list_by_questions(text_list=[])

    def get_answer_list_by_questions(self, text_list: list) -> list:
        return [input(text) for text in text_list]

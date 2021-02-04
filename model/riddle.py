class RiddleList:

    def __init__(self):
        self.riddle_it = []
        self.riddle_math = []
        self.riddle_history = []
        self.riddle_politics = []

        self.keys = []
        self.riddles = {
            'german': [],
            'weeb': [],
            'useless': [],
        }

        self.fill_key_list()

    def fill_key_list(self):
        for key in self.riddles:
            self.keys.append(key)


class Riddle:

    def __init__(self, _cat='', _question='', _answer=''):
        self.cat = _cat
        self.question = _question
        self.answer = _answer

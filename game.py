import data

class Game():

    def __init__(self, answer=None):
        if not answer:
            self.answer = data.correct_word()[0]
        else:
            self.answer = answer
   

    def guess_letter(self, letter):
        return [i for i in(range(len(self.answer))) if self.answer[i].upper() == letter.upper()]
  

    def guess_word(self, word):
        return word == self.answer.upper()

    def get_pattern(self):
        return ['_'] * len(self.answer)
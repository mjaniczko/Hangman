import view


class Player():

    def __init__(self, game, lifes):
        self.game = game
        self.lifes = lifes
        self.pattern = game.get_pattern()
        self.tries = []

    def try_letter(self, letter):
        indices = self.game.guess_letter(letter) 
        if indices:           
            for i in range(len(self.pattern)):  
                for j in indices:               
                    if i == j:
                        self.pattern[i] = letter
            new_pattern = ''.join(self.pattern)
            return self.game.guess_word(new_pattern.upper())
        else:
            self.lifes -= 1
            self.tries.append(letter.upper())
            print('Letters used already : ', ', '.join(self.tries))
            print('Left chances: ', self.lifes)
            return False

    def try_word(self, word):
        if self.game.guess_word(word.upper()):
            self.pattern = word
            return True
        else:
            self.lifes -= 2
            print('Left chances: ', self.lifes)
            return False
    
    def move(self):
        if self.lifes <= 0:
            print('You died. The answer is ', self.game.answer)
            return True
        print('Pattern: ', ''.join(self.pattern))
        guess = view.guess()
        if len(guess) == 1:
            success = self.try_letter(guess)
        else:
            success = self.try_word(guess)
        if success:
            print('You won: ', ''.join(self.pattern))
        return success

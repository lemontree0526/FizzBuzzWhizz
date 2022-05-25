
class FizzBuzzWhizz:
    def __init__(self, number):
        self.number = number

    def game_num(self):
        if self.is_divisible_by_3():
            return "Fizz"
        return self.game_num

    def is_divisible_by_3(self):
        return self.number % 3 == 0



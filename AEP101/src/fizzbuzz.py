
class FizzBuzzWhizz:
    def __init__(self, number):
        self.number = number

    def game_num(self):
        if self.is_divisible_by_3() and self.is_divisible_by_5():
            return "FizzBuzz"
        if self.is_divisible_by_3():
            return "Fizz"
        if self.is_divisible_by_5():
            return "Buzz"
        if self.is_divisible_by_7():
            return "Whizz"
        return self.game_num

    def is_divisible_by_3(self):
        return self.number % 3 == 0

    def is_divisible_by_5(self):
        return self.number % 5 == 0

    def is_divisible_by_7(self):
        return self.number % 7 == 0


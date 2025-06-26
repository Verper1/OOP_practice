from random import shuffle
from string import ascii_letters, digits, punctuation


class PasswordGenerator:
    symbols = list(digits + ascii_letters + punctuation)

    def generation(self, amount):
        shuffle(self.symbols)
        password = ''.join(self.symbols[:amount])

        return password


try1 = PasswordGenerator()
password = try1.generation(11)
print(password)

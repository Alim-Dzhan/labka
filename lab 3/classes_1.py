class Strings:
    def __init__(self):
        self.txt = ""

    def get_string(self):
        self.txt = input()

    def print_upper(self):
        print(self.txt.upper())


word = Strings()
word.get_string()
word.print_upper()

  

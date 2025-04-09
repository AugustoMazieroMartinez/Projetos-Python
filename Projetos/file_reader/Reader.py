class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def read(self):
        valor = open(self.file_path, "r")
        data = valor.read()
        return data
    
    def count_words(self):
        data = self.read()
        words = data.split()
        return len(words)
    
    def count_repeating_letters(self):
        data = self.read()
        letters = {}
        for letter in data:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        return letters
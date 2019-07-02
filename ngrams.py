#
# Author: Alvin Thai
# Description:
#     Uses classes to initialize input and open text files to remove punctuation and search for n-grams.  N-grams are groups of words in N, where N is an integer.  The frequency of these n-grams appearing is updated by using a dictionary where keys are the contactenated strings of these n-gram elements and the values are their frequencies.  The first input prompts for a text file, and the second input prompts n in n-grams.  N-grams with the maximum occurence are printed at the end. 
#
# The first class is created here.  It uses __init__ to define an input file and defines it to a variable while opening it.  The wordlist method splits the lines of the file into lists of words to be processed.  Punctuation marks are stripped and empty strings are skipped elements are appended to the list wordlist.
class Input:
    def __init__(self):
        self.file = input()
        self.a = open(self.file)
    def wordlist(self):
        wordlist = []
        for line in self.a:
            line = line.split()
            assert len(line) >= 1 and type(line) == list
            for word in line:
                assert type(word) == str
                word = word.strip(",'.;-")
                word = word.strip('"').lower()
                if word == "":
                    continue
                else:
                    wordlist.append(word)
        return wordlist

# The second class is used to process the wordlist created from the first class.  The __init__ method takes an integer as an input and creates a dictionary that will be used to count ngram occurences.  The update method contactenates ngrams found in wordlist into strings, so that they can be used as dictionary keys while assigning them to values which indicate frequency.  The process_wordlist method reads through wordlist from the argument to create ngrams, then uses the update method to create dictionary items.  print_max_grams will define the maximum frequency for the n-gram and print the ngrams with that frequency.
class Ngrams:
    def __init__(self):
        self.n = int(input())
        assert type(self.n) == int and self.n > 0, \
        "Integer must be typed greater than zero"
        self.ngram_count = {}
    def update(self, ngram):
        string = " "
        if string.join(ngram) not in self.ngram_count:
            self.ngram_count[string.join(ngram)] = 1
        else:
            self.ngram_count[string.join(ngram)] += 1
    def process_wordlist(self, wordlist):
        ngram = []
        for i in range(0, len(wordlist)-1):
            assert type(wordlist) == list, "only lists can be processed"
            if len(wordlist) < self.n:
                break
            elif len(wordlist) >= self.n:
                for j in range(self.n):
                    assert type(wordlist[0]) == str
                    ngram.append(wordlist[0])
                    del wordlist[0]
                self.update(ngram)
                while len(wordlist) >= 1:
                    assert len(ngram) == self.n
                    del ngram[0]
                    ngram.append(wordlist[0])
                    del wordlist[0]
                    self.update(ngram)
    def print_max_ngrams(self):
        M = 0
        for k, v in self.ngram_count.items():
            assert type(k) == str and type(v) == int
            if v >= M:
                M = v                            # changes M to new value
        for k, v in self.ngram_count.items():
            assert type(k) == str and type(v) == int
            if v == M:
                print("{:d} -- {}".format(v, k))
        
def main():
    obj = Input()                     
    wordlist = obj.wordlist()         # assigns wordlist to a global variable
    obj2 = Ngrams()                   
    obj2.process_wordlist(wordlist)   # carry out instance methods with variable
    obj2.print_max_ngrams()
main()
    
    

        
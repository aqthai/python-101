#
# Author: Alvin Thai
# Description: 
#     Accepts text file with words and their phonemes through input and a word that exists in that file, then prints words in the text file that fits the conditions of a perfect rhyme by searching through them in for-loops.  
#

# reads an input file of words and their phonemes and organizes them into a dictionary
def makes_dictionary():
    pfile = input()
    r = open(pfile, 'r')
    phonemes = r.readlines()
    pronounciation = []
    syllables = []
    dictionary = {}
    for line in phonemes:
        line = line.split()
        if line[0] in dictionary:
            for syllable in range(1, len(line)):
                syllables.append(line[syllable])
            dictionary[line[0]].append(syllables)   # appends different pronounciations to pre-existing words/keys in the dictionary
        else:
            for syllable in range(1, len(line)):
                pronounciation.append(line[syllable])
            syllables.append(pronounciation)
            pronounciation = []
            dictionary[line[0]] = syllables   # creates key and value for words that did not exist in the dictionary
        syllables = []
    return dictionary

# reads a word as an input, determines if it is in the dictionary, then searches words that have the same primary phoneme, phonemes after, and different preceding phoneme to print
def finds_rhyme(dictionary):
    word = input()
    word = word.upper()
    rhymes = []
    if word in dictionary:   # checks if word is in dictionary and assigns its phonemes to a variable
        syllables = dictionary[word]   
        for phonemes in syllables:         # runs through each pronounciation of that word
            for phoneme in phonemes:
                if phoneme.endswith('1'):  # finds primary phoneme before searching through dictionary
                    for k, v in dictionary.items():
                        for pronounciation in v:
                            if phoneme in pronounciation and \
                               phonemes[phonemes.index(phoneme):len(phonemes)]\
                               == pronounciation[pronounciation.index(phoneme):\
                                                 len(pronounciation)] and\
                               phonemes[phonemes.index(phoneme)-1] != \
                               pronounciation[pronounciation.index(phoneme)-1]\
                               and k not in rhymes:   # checks conditions for a perfect rhyme by using primary phoneme as refernence
                                rhymes.append(k)
    for rhyme in rhymes:
        print(rhyme)
    
def main():
    a = makes_dictionary()
    finds_rhyme(a)
main()
#
# Author: Alvin Thai
# Description:
#    The program makes a phylogenic tree from names and genomic sequences in fasta files.  It calculates max similarity between ngram sequences of genes, then uses it to determine proximity of organisms on the tree.
#
from genome import *
from tree import *
import sys

def get_ngrams(seq, n):
    '''From short problems, this makes a list of ngrams from a string sequence at N size'''
    return set([ "".join([seq[i+j] for j in range(0, n)]) for i in range(len(seq)-n+1) ])  # +1 reaches the last index
    # anagrams created from list comprehension                # list created from comprehension to the range of len(seq)-n
    
def seq_sim(seq1, seq2, k):
    '''creates a similarity number from two sequences of strings'''
    set1 = get_ngrams(seq1, k)
    set2 = get_ngrams(seq2, k)
    intersection = []
    union = []
    for seq in set1:
        if seq in set2:
            intersection.append(seq)   # for loop appends similar elements to one list
    for seq in set1:
        union.append(seq)
    for seq in set2:
        if seq not in union:
            union.append(seq)   # union has every different kgram from the sets
    return float(len(intersection))/float(len(union))

def seq_set_sim(seq_set1, seq_set2, k):
    '''finds the max similarity value between two sets of ngrams'''
    max_dist = 0
    for i in seq_set1:
        for j in seq_set2:
            temp = seq_sim(i, j, k)  # finds the Jaccard indices between sets in seq_set1 and seq_set2 and returns the max
            if temp > max_dist:
                max_dist = temp
    return max_dist

def read():
    ''' reads a fasta file to provide names, sequences, and sets of ngrams for each organism in a dictionary, then makes another dictionary with max similarity values between combinations of two organisms'''
    file = input('FASTA file: ')
    try:
        N = int(input('n-gram size: '))
    except ValueError:
        print("ERROR: Bad value for N")
        sys.exit(1)
    try:
        data = open(file, 'r')
    except IOError:
        print("ERROR: could not open file " + file)
        sys.exit(1)
    else:
        x = data.readlines()
        sequence = ""
        name = ""
        genome_list = []
        sequence_dict = {}
        sim_dict = {}
        sequence = ""
        name = ""
        for line in x:
            line = line.rstrip('\n')
            if line == "":
                sequence_dict[name] = get_ngrams(sequence, N)
                sequence = ""
                name = ""          
            elif line.find('>') == 0:
                name = line[1:line.find(" ")]
                sequence_dict[name] = 0
                n = Tree()
            elif line.startswith(" ") != True:
                sequence += line
        for k, v in sequence_dict.items():
            for r, s in sequence_dict.items():
                if k != r:
                    sim_dict["and".join(sorted([k, r]))] = seq_set_sim(v, s, N)

        return sequence_dict, sim_dict
    
def construct_tree(sequence_dict, sim_dict):
    '''constructs a tree by taking names from organisms in sim_dict and linking them as left and right nodes in a binary tree'''
    tree_list = []
    for key, value in sequence_dict.items():
        t = Tree()
        t._name = key
        tree_list.append(t)
        
    while len(tree_list) > 1:
        t0 = Tree()
        t0._left = tree_list[0]
        t0._right = tree_list[1]
        tree_list.remove(tree_list[0])
        tree_list.remove(tree_list[0])
        tree_list = [t0] + tree_list
    return str(tree_list[0])

def branching(t1, t2):
    '''Helper function to connect left and right nodes to t0'''
    t0 = Tree()
    if str(t1) < str(t2):
        t0._left = t1
    elif str(t2) < str(t1):
        t0._left = t2
    return t0

def main():    
    a, b = read()
    print(construct_tree(a, b))
main()
    
    


    

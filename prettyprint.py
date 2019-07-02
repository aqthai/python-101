"""
    File: prettyprint.py
    Author: Saumya Debray
    Purpose: Pretty-print phylogenetic trees

    Interface assumptions:  This code assumes that the Tree class implements
        the following methods.  If your attributes for this class are named
        differently, you can modify this code appropriately.

        tree.is_leaf() : returns True if the root of the tree is a leaf node, 
		False otherwise

        tree.left() : returns the left child of tree

        tree.right() : returns the right child of tree
"""

def pretty_print(tree):
    print("")
    pp = pretty_print_strs(tree)
    for line in pp:
        print(line)

def pretty_print_strs(tree):
    if tree.is_leaf():
        return ['+--- ' + str(tree)]
    else:
        ltree = pretty_print_strs(tree.left())
        rtree = pretty_print_strs(tree.right())
        nltree = len(ltree)
        nrtree = len(rtree)
        adjusted = _adjust_left(ltree, 0, nltree) + ['|'] +  _adjust_right(rtree, 0, nrtree)
        return _shift(adjusted, 0, len(adjusted))

def _shift(strlist, i, n):
    if strlist == []:
        return []
    else:
        if i == n//2:
            sh_str = ['+---' + strlist[0]]
        else:
            sh_str = ['    ' + strlist[0]]

        return sh_str + _shift(strlist[1:], i+1, n)

def _adjust_left(L, i, n):
    if i == n:
        return []
    else:
        if i <= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_left(L, i+1, n)
        

def _adjust_right(L, i, n):
    if i == n:
        return []
    else:
        if i >= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_right(L, i+1, n)
        

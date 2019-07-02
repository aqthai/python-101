#
# Author: Alvin Thai
# Description:  
#     Huffman created prefix coding, or binary encoding that tells a program where to traverse in a binary tree.  All prefix codes are unique.  The program creates a binary tree given preorder and inorder traversals, prints the postorder traversal, and decodes a binary sequence to provide values from leaf nodes.
#
class BinaryTree:
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None
        
    # assigns first element of the preorder list to BinaryTree object, creates preorder and inorder lists for the left and right nodes, and continues assigning values to BinaryTree nodes until the preorder list is empty    
    def make_tree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        else:
            self._value = preorder[0]
            inorder_left = inorder[:inorder.index(preorder[0])]  # takes elements to the left of the root node value in inorder list
            preorder_left = preorder[1:len(inorder_left)+1] # elements from right of the root node value up to length of inorder_left
            inorder_right = inorder[inorder.index(preorder[0])+1:len(inorder)] # remaining elements of inorder list
            preorder_right = preorder[len(preorder_left)+1:len(preorder)] # remaining elements of preorder list
            l = BinaryTree()
            self._left = l.make_tree(preorder_left, inorder_left)
            self._left = l
            r = BinaryTree()
            self._right = r.make_tree(preorder_right, inorder_right)
            self._right = r
        return self
    
    def __str__(self):
        if self._value == None:
            return str("None")
        else:
            return "({} {} {})".format(str(self._value), str(self._left), str(self._right))

# reads file to get preorder, inorder, and encoded binary sequences
def get_orders():
    file_lines = []
    preorder = []
    inorder = []
    file = input('Input file: ')
    try:
        data = open(file)
    except:
        print("ERROR: Could not open file " + file)
    else:
        data = data.readlines()
        for line in data:
            line = line.rstrip('\n').split()
            file_lines.append(line)
        preorder = file_lines[0]
        inorder = file_lines[1]
        
        encoded = str(file_lines[2][0])
        return preorder, inorder, encoded

# recurses through the left and right nodes of the tree, then the root to get postorder sequence
def postorder(tree):
    if tree._value == None:
        return ""
    if tree._left == None and tree._right == None:
        return str(tree._value)
    elif tree._left != None and tree._right != None:
        order =  str(postorder(tree._left) + " " + postorder(tree._right) + " " + tree._value).split()
        order = " ".join(order)   # removes extra spaces from None values
        return order

# returns decoded string from encoded sequence and binary tree
def decoder(tree, encoded):
    ptrhead = tree
    decoded = ""
    for i in range(0, len(encoded)):
        if encoded[i] == "0" and ptrhead._left._value != None:
            ptrhead = ptrhead._left
            if ptrhead._left._value == None and ptrhead._right._value == None:    # values of left and right nodes are checked to see if a leaf node is landed on
                decoded += str(ptrhead._value)
                ptrhead = tree
            continue
        elif encoded[i] == "1" and ptrhead._right._value != None:
            ptrhead = ptrhead._right
            if ptrhead._left._value == None and ptrhead._right._value == None:
                decoded += str(ptrhead._value)
                ptrhead = tree
            continue
        else:
            ptrhead = tree # ptrhead returns to the root of the tree when a 0 or 1 does not traverse tree
    return decoded
    
def main():
    a, b, c = get_orders()
    t = BinaryTree()
    t.make_tree(a, b)
    print(postorder(t))
    print(decoder(t, c))
main()
    

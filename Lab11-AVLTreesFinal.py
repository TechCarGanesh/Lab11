# Name: Ganesh Kumar
# Date: 04/17/2025
# Instructor: Professor Andres Calle
# Lab Week 11 Project Information:
# In this lab, you will create a simple spell checker using an AVL Tree and sets.
# The AVL Tree will serve as your dictionary, storing a list of valid words for quick searching.
# The set will store flagged words (misspelled words) from an input document,
# ensuring each misspelled word appears only once.
# You will implement functionality to check each word in a document against the dictionary,
# flag misspelled words, and display them in alphabetical order.
# This lab will give you hands-on experience with both the efficiency of AVL Trees for search operations
# and the utility of sets for managing unique items.
# You are required to implement a AVL Tree class, import cannot be used.
# Sets can be represented as you like.
#
#
#
# Requirements
# Dictionary AVL Tree Implementation:
#
# Read a dictionary file (a plain text file containing one valid word per line)
# and insert each word into an AVL Tree. Each node in the AVL Tree should contain one word.
# Implement insertion, search, and removal for the AVL Tree with rotation,
# ensuring words are sorted alphabetically.
# You are allowed to simplify, just 15 unique words would be enough.
# Spell Checking:
#
# Read a document (another plain text file containing multiple words and sentences)
# and split it into individual words. Ignore punctuation and treat all words as lowercase.
# For each word in the document, check if it exists in the AVL dictionary.
# If a word is not found in the dictionary, add it to a set of misspelled words (to avoid duplicates).
# Display Misspelled Words and Tree:
#
# Implement functionality to show all misspelled words in the final document.
# Print your tree with inorder traversal, include balance at each node along with the data stored there
import string
# To check file existence
import os
# Import regular expression
import re

# Setting vertical to 1.
VERTICAL = 1
# Setting horizontal to 0.
HORIZONTAL = 0
# Setting maximum height to 16.
MAX_HEIGHT = 16

# AVLNode Class
class AVLNode:
    def __init__(self, word):
        # Word stored in the node
        self.word = word
        # Left child
        self.left = None
        # Right child
        self.right = None
        # Height of the node (starts at 0)
        self.height = 0

# AVLTree Class
class AVLTree:
    def __init__(self):
        self.root = None
        print("AVL Tree const")

    def insert(self, node, word):
        return self.insert_recursive(node, word)
    # Insert a word and balance the tree
    def insert_recursive(self, root, word):
        print("I am in the insert function.")
        if root is None:
            root = AVLNode(word)
            return root
        # If the current node is none, then return the word.
        if not root:
            print("! Root", word)
            return AVLNode(word)
        # If the word is smaller,
        # the function proceeds to insert the word in the left subtree of the current node
        elif word < root.word:
            print("Left subtree", word)
            root.left = self.insert_recursive(root.left, word)
        # If the word is greater,
        # the function recursively calls self.insert_recursive(root.right, word)
        # to insert the word into the right subtree.
        elif word > root.word:
            print("Right subtree", word)
            root.right = self.insert_recursive(root.right, word)
        # If it is a duplicate word, ignore and return the root.
        else:
            print("Return the root.")
            return root

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        print("Height is", root.height)

        # Calculate balance factor
        balance = self.get_balance(root)

        # Balance the tree using rotations
        # Case 1: Left-left rotation
        if balance > 1 and word < root.left.word:
            print("Left-left rotation")
            return self.right_rotate(root)
        # Case 2: Right-right rotation
        if balance < -1 and word > root.right.word:
            print("Right-right rotation")
            return self.left_rotate(root)
        # Case 3: Left-right rotation
        if balance > 1 and word > root.left.word:
            print("Left-right rotation")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case 4: Right-left rotation
        if balance < -1 and word < root.right.word:
            print("Right-left rotation")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return root.
        return root

    # Search for a word in the tree
    def search(self, root, word):
        # If the word is not in the tree, return false.
        if not root:
            return False
        # If the word is in the tree, return true.
        if word == root.word:
            return True
        # If the word being searched for is
        # smaller than the word stored in the current node (root.word),
        # the word is in the left subtree of the current node.
        elif word < root.word:
            return self.search(root.left, word)
        # If the word being searched for is
        # greater than the word stored in the current node (root.word),
        # the word is in the right subtree of the current node.
        else:
            return self.search(root.right, word)

    # Get height of a node
    def get_height(self, node):
        if not node:
            return -1
        return node.height

    # Get balance factor
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Perform a left rotation
    def left_rotate(self, currNode):
        # Assigning the right child of currNode to newRoot.
        newRoot = currNode.right
        # Assigning the left child of newRoot to T2.
        T2 = newRoot.left

        # Making current node of currNode the left child of newRoot.
        newRoot.left = currNode
        # Making current node of T2 the right child of currNode.
        currNode.right = T2

        # Calculating the height of currNode.
        currNode.height = 1 + max(self.get_height(currNode.left), self.get_height(currNode.right))
        # Calculating the height of newRoot.
        newRoot.height = 1 + max(self.get_height(newRoot.left), self.get_height(newRoot.right))

        # Return the new root
        return newRoot

    # Perform a right rotation
    def right_rotate(self, currNode):
        # Assigning the left child of currNode to newRoot.
        newRoot = currNode.left
        # Assigning the right child of newRoot to T3.
        T3 = newRoot.right
        # Making current node of currNode the right child of newRoot.
        newRoot.right = currNode
        # Making current node of T3 the left child of currNode.
        currNode.left = T3

        # Calculating the height of currNode.
        currNode.height = 1 + max(self.get_height(currNode.left), self.get_height(currNode.right))
        # Calculating the height of newRoot.
        newRoot.height = 1 + max(self.get_height(newRoot.left), self.get_height(newRoot.right))

        # Return the new root.
        return newRoot

    # In-order traversal prints nodes in sorted order with balance
    def inorder_traversal(self, root):
        if root:
            # Visit the left child first.
            print("Inorder left:", root.word)
            self.inorder_traversal(root.left)
            # Calculating the balance factor.
            balance = self.get_balance(root)
            # Printing the word stored in the current node along with balance factor.
            print(f"{root.word} (Balance: {balance})")
            # Visit the right child next.
            print("Inorder right:", root.word)
            self.inorder_traversal(root.right)

# process_document function.
def process_document(text):
    # Translator removes punctuation
    translator = str.maketrans('', '', string.punctuation)
    # Makes the letters lowercase and splits it.
    words = text.translate(translator).lower().split()
    # Return the words.
    return words


# load_dictionary function loads dictionary words into AVL tree
def load_dictionary(file_path):
    # Construct an AVL tree object.
    tree = AVLTree()
    # Dictionary AVL Tree
    print("Load dictionary AVL Tree", file_path)
    # Setting the root to none.
    root = None

    # If file does not exist, print that the file is not found.
    if not os.path.exists(file_path):
        # File
        print(f"File '{file_path}' not found!")
        return tree, root

    # Opening the file in reading mode.
    file_path = "C:\\AdvancedPython\\ADVANCEDPYTHON-2025\\dictionary2.txt"
    # with open(file_path, 'r') as f:
    infile = open(file_path, "r")
    # Reads the entire contents of the document into a single string.
    content = infile.readline()
    # Debug content
    print(f"\nRaw contents of '{file_path}':\n{content}\n")
    # Reset pointer to beginning of file
    infile.seek(0)
    for line in infile:
        # Strip the line
        print("Line is", line.strip())
        # Storing a lowercase word in the AVL tree.
        word = line.strip().lower()
        # Printing the word in the dictionary.
        print("Load dictionary", word)
        if word:
            # Insert the word in the AVL tree.
            root = tree.insert(root, word)
    # Returning tree and root.
    return tree, root


# Check spelling of words in a document
def spell_check(word, root, avl_tree):
    return avl_tree.search(root, word)

# Main function.
def main():
    # Stores list of words to spell-check.
    spell_check_words = []
    # Regular expression to remove punctuation.
    match_regexp = r"[?.],".format(re.escape(string.punctuation))
    # Create misspelled set.
    misspelled_set = set()
    # Input file paths (make sure these exist!)
    # Creating dictionary file.
    dictionary_file = "dictionary2.txt"
    # Creating document file.
    document_file = "document2.txt"

    # If dictionary file does not exist, print that the dictionary file is not found and return.
    if not os.path.exists(dictionary_file):
        print(f"Dictionary file not found: {dictionary_file}")
        return
    # If document file does not exist, print that the dictionary file is not found and return.
    if not os.path.exists(document_file):
        print(f"Document file not found: {document_file}")
        return

    print("Files found. Proceeding with load and spell check...\n")

    # Load dictionary into AVL Tree
    avl_tree, root = load_dictionary(dictionary_file)

    # Print the tree (sorted) with balance factors
    print("\n=== In-order Traversal of AVL Tree (with balance): ===")
    # If there is root, perform inorder traversal on the AVL tree.
    if root:
        avl_tree.inorder_traversal(root)
    # Otherwise, print that the AVL tree is empty.
    else:
        print("AVL Tree is empty!")

    # Make a list of spell-check words.
    with open("document2.txt", "r") as doc_file:
        for line in doc_file:
            # Remove the punctuation and replace it with blanks.
            spell_check_words.extend(re.sub(match_regexp, " ", line).lower().split())

        print("Performing spell check.", spell_check_words)
        # Check for each word in the spell_check_words list.
        for word in spell_check_words:
            # If word is not in the dictionary
            if not spell_check(word, root, avl_tree):
                misspelled_set.add(word)
        # Printing the set of misspelled words.
        print("Misspelled words are: ", misspelled_set)

    print("\n=== Misspelled Words Found: ===")
    # If there are misspelled words, print the misspelled word.
    if misspelled_set:
        for word in sorted(misspelled_set):
            print(f"{word}")
    # Otherwise, print that there are no misspelled words.
    else:
        print("No misspelled words found!")

    # Add a loop to ask the user to add new items into dictionary.
    # Ask the user to enter a word to spell-check or exit.
    while True:
        print("Enter 1 to add a new word into dictionary.")
        print("Enter 2 to spell-check.")
        print("Enter 3 to exit.")
        choice = int(input("Please select an option:"))
        if choice == 3:
            print("Goodbye!")
            break
        elif choice == 1:
            word = str(input("Please enter a word into the dictionary."))
            root = avl_tree.insert(root, word)
        elif choice == 2:
            word = str(input("Please enter a word to spell-check."))
            if not spell_check(word, root, avl_tree):
                print("Misspelled word = ", word)

# Calling main function.
if __name__ == "__main__":
    main()
# C:\AdvancedPython\ADVANCEDPYTHON-2025\.venv\Scripts\python.exe C:\AdvancedPython\ADVANCEDPYTHON-2025\Lab11-AVLTrees.py
# Files found. Proceeding with load and spell check...
#
# AVL Tree const
# Load dictionary AVL Tree dictionary2.txt
#
# Raw contents of 'C:\AdvancedPython\ADVANCEDPYTHON-2025\dictionary2.txt':
# elephant
#
#
# Line is elephant
# Load dictionary elephant
# I am in the insert function.
# Line is monkey
# Load dictionary monkey
# I am in the insert function.
# Right subtree monkey
# I am in the insert function.
# Height is 1
# Line is cow
# Load dictionary cow
# I am in the insert function.
# Left subtree cow
# I am in the insert function.
# Height is 1
# Line is dog
# Load dictionary dog
# I am in the insert function.
# Left subtree dog
# I am in the insert function.
# Right subtree dog
# I am in the insert function.
# Height is 1
# Height is 2
# Line is lemur
# Load dictionary lemur
# I am in the insert function.
# Right subtree lemur
# I am in the insert function.
# Left subtree lemur
# I am in the insert function.
# Height is 1
# Height is 2
#
# === In-order Traversal of AVL Tree (with balance): ===
# Inorder left: elephant
# Inorder left: cow
# cow (Balance: -1)
# Inorder right: cow
# Inorder left: dog
# dog (Balance: 0)
# Inorder right: dog
# elephant (Balance: 0)
# Inorder right: elephant
# Inorder left: monkey
# Inorder left: lemur
# lemur (Balance: 0)
# Inorder right: lemur
# monkey (Balance: 1)
# Inorder right: monkey
# Performing spell check. ['elephant', 'big', 'than', 'monkey', 'while', 'limur', 'smaller', 'than', 'caw']
# Misspelled words are:  {'limur', 'smaller', 'big', 'caw', 'while', 'than'}
#
# === Misspelled Words Found: ===
# big
# caw
# limur
# smaller
# than
# while
# Enter 1 to add a new word into dictionary.
# Enter 2 to spell-check.
# Enter 3 to exit.
# Please select an option:1
# Please enter a word into the dictionary.lion
# I am in the insert function.
# Right subtree lion
# I am in the insert function.
# Left subtree lion
# I am in the insert function.
# Right subtree lion
# I am in the insert function.
# Height is 1
# Height is 2
# Left-right rotation
# Height is 2
# Enter 1 to add a new word into dictionary.
# Enter 2 to spell-check.
# Enter 3 to exit.
# Please select an option:2
# Please enter a word to spell-check.leon
# Misspelled word =  leon
# Enter 1 to add a new word into dictionary.
# Enter 2 to spell-check.
# Enter 3 to exit.
# Please select an option:3
# Goodbye!
#
# Process finished with exit code 0

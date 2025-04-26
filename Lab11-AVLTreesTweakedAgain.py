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
class AVLNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Insert with normalization
    def insert(self, root, word):
        word = word.strip().lower()
        if not root:
            return AVLNode(word)

        if word < root.word:
            root.left = self.insert(root.left, word)
        elif word > root.word:
            root.right = self.insert(root.right, word)
        else:
            return root  # duplicate

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left-Left
        if balance > 1 and word < root.left.word:
            return self.right_rotate(root)

        # Right-Right
        if balance < -1 and word > root.right.word:
            return self.left_rotate(root)

        # Left-Right
        if balance > 1 and word > root.left.word:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left
        if balance < -1 and word < root.right.word:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def contains(self, root, word):
        word = word.strip().lower()
        if not root:
            return False
        if word == root.word:
            return True
        elif word < root.word:
            return self.contains(root.left, word)
        else:
            return self.contains(root.right, word)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(f"{node.word} (Balance: {self.get_balance(node)})")
            self.in_order_traversal(node.right)

# === Spell Check Function ===
def spell_check(word, avl_tree, root):
    return avl_tree.contains(root, word)

# === MAIN SCRIPT ===
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Load dictionary
    with open("dictionary.txt", "r") as file:
        for line in file:
            clean_word = line.strip().lower()
            root = avl.insert(root, clean_word)

    print("\n=== In-order Traversal of AVL Tree (with balance factors): ===")
    avl.in_order_traversal(root)

    # Sample words to spell-check
    input_words = ["a", "convertible", "couppe", "driving", "i", "love", "more", "sports", "than"]

    print("\n=== Spell Check Results: ===")
    for word in input_words:
        if not spell_check(word, avl, root):
            print(f"- {word}")

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
            root = avl.insert(root, word)
        elif choice == 2:
            word = str(input("Please enter a word to spell-check."))
            if not spell_check(word, avl, root):
                print("Misspelled word = ", word)
# Result:
# C:\AdvancedPython\ADVANCEDPYTHON-2025\.venv\Scripts\python.exe C:\AdvancedPython\ADVANCEDPYTHON-2025\Lab11-AVLTreesTweakedAgain.py
#
# === In-order Traversal of AVL Tree (with balance factors): ===
# a (Balance: -1)
# buggy (Balance: 0)
# bus (Balance: -1)
# convertible (Balance: 0)
# coupe (Balance: 0)
# dirtbike (Balance: 0)
# driving (Balance: 0)
# electric (Balance: 0)
# hot-rod (Balance: 0)
# hybrid (Balance: 0)
# i (Balance: 0)
# like (Balance: 0)
# love (Balance: 0)
# minivan (Balance: 0)
# more (Balance: 0)
# racecar (Balance: 0)
# sailboat (Balance: 0)
# sedan (Balance: 0)
# sports (Balance: 0)
# suv (Balance: 0)
# than (Balance: -1)
# truck (Balance: -1)
# wagon (Balance: 0)
#
# === Spell Check Results: ===
# - couppe
# Enter 1 to add a new word into dictionary.
# Enter 2 to spell-check.
# Enter 3 to exit.
# Please select an option:1
# Please enter a word into the dictionary.W16
# Enter 1 to add a new word into dictionary.
# Enter 2 to spell-check.
# Enter 3 to exit.
# Please select an option:3
# Goodbye!
#
# Process finished with exit code 0
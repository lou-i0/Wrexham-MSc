# Louis Othen  -  Assessment 7.3.0 - Huffman Coding
#--------------------------------------------------
'''
goal of code is to write an implementation of
Huffman coding in python , as a way to encode and reduce the size
of data.

The Code will :
 - Print out data used before and after the encoding.
 - The output will be printed out as binary code
 - A written description of my approach to the problem
 - Take an input from the user to encode with.

The Approach taken is as follows:
1) create a class that produces a node for the huffman tree
    1.1) Initialise class with the letter in question, the weight (number of times a letter is found), with left and right to represent the children once processed via recursion
    1.2) The ability to return the children from a parent Node, or None if empty/ not populated
    1.3) Once called, to return the object as a string showing the children of the node
    1.4) __lt__ allows the ability for the object to be compared with another object /node in terms of value
2) Create a recursive function to go through all nodes in the tree , and once reached the parent, print the letter associated and the encoded value based on the position in the tree.
3) Create function to encapsulate the above, and perform the encoding of the phrase

NOTE complexity of the logic is believed to be O(n*log(n))
'''
#=================================================
#/////////////////////////////////////////////////
#=================================================
# 0 - Import relevant libraries for assignment
#-------------------------------------------------
from collections import Counter										# Collections library documenting frequency which a letter occurs in phrase given by user
import heapq														# To utilise a heap data structure, useful to raverese an binary tree
encoded_value = {}													# Create empty dictionary to store coded values
#=================================================
# 1 - Create a Node class which be used to form a Binary Huffman Tree
#-------------------------------------------------
class HuffmanNode:
    
    def __init__(self, letter, weight, left = None, right = None):  # Initialising the class
        
        self.letter = letter										# The letter itself
        self.weight = weight										# Frequency (weight) of the letter
        self.left = left											# Placeholder for child/leaf node on left
        self.right = right											# Placeholder for child/leaf node on right
        
        self.logic = ''												# to dictate tree direction (0/1)


    def __lt__(self,next):											# In-built to return when an item is less then whats there? 
        return self.weight < next.weight
#=================================================
# 2 -  Create recusive function to get huffman codes for all letters in huffman tree
#-------------------------------------------------
def printNodes(node, val = ''):										
    
    global encoded_value											# Get dict from user section of code 
    
    newval = val + str(node.logic)									# Value represents the val supplied along with logic of 1 or 0
    
    if(node.left):
        printNodes(node.left,newval)
    if(node.right):
        printNodes(node.right,newval)
        
    if(not node.left and not node.right):							# When Node represents the parent, print out the letter, and its encoded equivelant
        print(f"{node.letter} -> {newval}")
        encoded_value[f'{node.letter}'] = newval
        
    return encoded_value
    
#=================================================
# 2 -  Create fFunction to perform the encoding
#-------------------------------------------------        
def process_huffman_code(phrase_entered):							
    
    # 1 - Display phrase entered back to user before encoding
    #-------------------------------------------------
    print('------------------------------------------')
    print(f"Confirmation that '{phrase_entered}' has been entered.")# Returns entered phrase as output to user
    print('------------------------------------------')
    print('')	
    
    
    # 2 - use Counter to document frequency of characters in phrase
    # -------------------------------------------------
    freq = dict(Counter(phrase_entered))							# Applies Counter Function onto phrase, stores letters & frequency into dictionary
    for i in freq:													# For each letter in phrase, print out letter and number of times it has occurred
        print(f"The letter: '{i}' has been found {freq.get(i)} times.")
        print('')
        
    # 3 - Sort frequency table of phrase entered in descending order
    # -------------------------------------------------
    freq = sorted(freq.items(), key = lambda x: x[1], reverse= True)
    
    
    # 4 - Make the Huffman tree nodes with sorted freq above
    # -------------------------------------------------
    nodes = []														# Create empty list to accept newly created nodes
    
    for entry in freq:												# For each letter and weight in freq
        letter =  entry[0]											# Get letter from list dictionary
        weight = entry[1]											# Get weight from list dictionary
        node = HuffmanNode(letter, weight)							# Create a new node based on the letter and weight
        nodes.append(node)											# add node to nodes list for further processing
       
    # 5 - perform encoding on created tree
    # -------------------------------------------------
    while len(nodes) > 1 :
        #sort all nodes in ascending order
        # based on weight
        left = heapq.heappop(nodes)									# pop out smallest value in nodes into left
        right = heapq.heappop(nodes)								# pop out 2nd smallest value into right
        
        left.logic = '0'											# Assign value of 0 to nodes on the left
        right.logic = '1'											# Assign value of 1 nodes on the right
        
        
        newNode = HuffmanNode(										# Combines 2 smallest nodes to create new node as parent
                                left.letter + right.letter
                                ,left.weight + right.weight
                                ,left
                                ,right
                             )
        
        heapq.heappush(nodes, newNode)								# Place new node back into the heap at highest point
    
    
        
    # 6 - Display encoding of phrase into binary format from huffman tree 
    # -------------------------------------------------
    print('The phrase provided is encoded as follows:')
    print('------------------------------------------')
    
    values_dict =  printNodes(nodes[0])										# Execute printNodes function to display encoded dictionary
    values_list = values_dict.values()										# Return list of values of encoding
    binary_code = ''.join(str(item) for item in values_list)				# Concatenates all values into one
    
    return binary_code  													# Finally, returns joined binary code back to the user 
     #=================================================
#/////////////////////////////////////////////////
#=================================================
# Testing code with inputes from the user
#=================================================
# 
# 1 - Ask user to enter a phrase as input
#-------------------------------------------------
phrase =  str(input('Please enter a phrase to encode: '))			# Prompts user to enter phrase
print('')															# Adds Carriage return to separate outputs
 
# 0 - Perform Huffman Encoding on phrase given
#-------------------------------------------------
encoded_phrase = process_huffman_code(phrase)						# Processes the huffman code and save result to variable				

print(f"The Phrase '{phrase}' has been encoded as '{encoded_phrase}'")
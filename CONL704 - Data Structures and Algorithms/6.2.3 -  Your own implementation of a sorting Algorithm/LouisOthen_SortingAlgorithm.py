#==============================================
# Louis Othen - Create own implementation of sorting algorithm
#==============================================
# Requirements
#----------------------------------------------
# Using linked list data
# must print linkedlist before and after sorting
# explain why I chose this sorting algorithm
# explain complexity
# sort them in descending order (largest to smallest) 
# do the code
#==============================================
#//////////////////////////////////////////////
#==============================================
# 1 - Set up
#===============================================
# 1.1 - Import the linked List Class
# (as replicated from the code provided in assignment 6.2.3)
#----------------------------------------------
import LinkedList_assignment as lla

# 1.2 - Get copy of countries LinkedList, from LinkedList Class
#-----------------------------------------------
count_ll = lla.countries
#==============================================
#//////////////////////////////////////////////
#==============================================
# 2 - Initlise functions required for sort algorithm
#===============================================
# 2.1 - Function to print out countries in Linked List
#-----------------------------------------------
def info_linkedlist(llist):
    print('Countries in Linked List as follows:')
    print('-----------------------------------')# Underline for printed text
    while llist is not None: 					# While the entry is not None
        print(llist.label,': ',llist.value)		# Print current label and value 
        llist = llist.tail						# Assign end of current entry as beginning of next one.
        
# 2.1 - Function to print out linked list size by count of items
#-----------------------------------------------
def count_linkedlist(llist):
    size = 0									# Initialises a count variable
    while llist is not None:
        llist = llist.tail
        size += 1								# Log that entry to the counter
    return print(f'The size of the Linked list is: {size}')


#==============================================
#//////////////////////////////////////////////
#==============================================
# 1. - Implement the sorting Algorithm
#----------------------------------------------
'''
 The Sorting algorithm that has been elected to use is the Merge Sort Algorithm
 One reason for this choice is due to idea of a divide and conquer strategy,
 breaking the sorting task, into smaller sub sorting tasks so that it only passes through data once.
 Additionally, algorithm utilises recursion to handle as needed mentioned above.
 Furthermore, as the data in question is a linked list, this algorithm appears to be more efficient
 compared with others, with the complexity of O(n*log n)
'''

'''
 as part of the merge sort algorithm, the sequence or list would be split into two
 separate lists, ready for the algorithm to be implemented against them.
'''

# 1.1 - Function to find midpoint item in linked list for later splitting
#----------------------------------------------
def midpoint_linklist(llist):
    if llist == None:
        return head
    
    slow = llist								# makes a reference to linked list 
    fast = llist 								# reference to next item in linked list
    while fast.tail != None and fast.tail.tail != None:	# Whilst fast and next item along is not None
        slow = slow.tail						# Move to next item for slow
        fast = fast.tail.tail					# Move two items ahead for fast
    return slow 


# 1.2 - Function to merge array recursively in Merge Sort Algorithm
#----------------------------------------------
def merge_sub_linkedlists(left_llist,right_llist):
    result =  None									# empty area to store the result
    
    if left_llist == None:							# If nothing in left_llist, return right_llist
        return right_llist
    if right_llist == None:							# If nothing in right_llist, return left_llist
        return left_llist

    
    if left_llist.value >= right_llist.value: 		# If the value in the current item of left llist is greater
        result = left_llist							# Then store left_llist into result
        result.tail = merge_sub_linkedlists(left_llist.tail, right_llist)
        
    else:
        result = right_llist
        result.tail = merge_sub_linkedlists(left_llist, right_llist.tail)
        
    return result


# 1.3 -  Function to carry out merge sort algorithm
#----------------------------------------------
def merge_sort_algorithm(llist):
    if llist ==  None or llist.tail == None:  		# If Linked List is empty
        return llist						  		# Return the linked list
    
    midpoint  = midpoint_linklist(llist)			# Establish middle item in linked list
    midpointnxt = midpoint.tail						# see item after midpoint
    
    midpoint.tail = None							# set next after midpoint to none, to break linked list for splitting
    
    left_llist 	= merge_sort_algorithm(llist)		# Apply merge sort algorithm on left linked list
    right_llist = merge_sort_algorithm(midpointnxt)	# Apply merge sort algorithm on right linked list
    
    sorted_list = merge_sub_linkedlists(left_llist,right_llist) # merge sub list back to together in sorted order
    
    return sorted_list
    
#==============================================
#//////////////////////////////////////////////
#==============================================
# 2 - implementation
#==============================================
'''
This last section of the code, actually implements the functions above,
against the linked list brought through. The next steps will:
1) Display the LinkedList in its original state
2) Show count of the number of items found within the Linked List
3) Splits the Linked List into two as an example, based on finding the midddle item
4) Displays the  example split of the Linked List into two with counts for each - optionally commented out
5) Performs the Merge Sort Algoritm (With recursion)
6) Finally, display the Linked List once the sorting algorithm has been applied

'''
# 2.1 - Display Linklist as originally recevied 
#----------------------------------------------
print('========================================') # Line to separate results
print('Showing Original Linked List information')
print('========================================') # Line to separate results
info_linkedlist(count_ll)						# Display LinkedList in original form
print('--------------------------------------') # Line to separate results
count_linkedlist(count_ll)						# Size Count of Linked List 
print('--------------------------------------') # Line to separate results
print(' ')										# New Line to space results


# 2.3 Running the Merge Sort Algorithm 
#----------------------------------------------
llist_sorted = merge_sort_algorithm(count_ll)

# 2.4 Finally, display Linked List once sorting algorithm has been applied
#----------------------------------------------
print('=======================================') # Line to separate results
print('Showing sorted Linked List information')
print('=======================================') # Line to separate results
info_linkedlist(llist_sorted)
print('--------------------------------------') # Line to separate results
count_linkedlist(llist_sorted)
print('--------------------------------------') # Line to separate results
print(' ')										# New Line to space results





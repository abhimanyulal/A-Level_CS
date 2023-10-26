import csv
import pandas as pd
import numpy as nm

data_list = []
def updateDL():                                          #Function to convert Learners.CSV File to a List of Lists named Data_List
    with open("Learners.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)
    n = (len(data_list)) + 1
    return n

n = updateDL()


class LNode:                                            # Create a Node class to create a Node for the Linked List
    def __init__(self, data):
        self.data = data
        self.next = None
 

class LinkedList:                                       # Create a LinkedList class
    def __init__(self):
        self.head = None

    
    def insertAtEnd(self, datak):                       # Method to add a LNode at the end of Linked List
        new_LNode = LNode(datak)                        # This function runs through all the nodes until it finds the last node with data.
        if self.head is None:                           # Once it finds the last nodes, it adds a new node right after it with given data. (Datak is an array defined later)
            self.head = new_LNode
            return
 
        current_LNode = self.head
        while(current_LNode.next):
            current_LNode = current_LNode.next
 
        current_LNode.next = new_LNode
 
    def remove_first_node(self):                        # Function to remove first node. Used in remove_at_index function.
        if(self.head == None):
            return
 
        self.head = self.head.next
 

    def remove_at_index(self, index):                   # Function to delete a specified node. index parameter is assigned later.
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:                           #Linear search to find specified node. Deletes the node using remove_first_node() function
            self.remove_first_node()
            print("Entity removed successfully.")
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Invalid ID. You could try the Search function to find ID")
    
    def updateNode(self, ID):                           # Function to update a specified node.
        
        Valid = False
        Name = input("New Learner Name: ")                                                                  # Prompting user for values of nessaccary fields.
        
        while Valid == False:                                                                               # Loop for format check.
            Grade = input("Grade: ")
            if Grade not in ["A", "AS", "IGCSEL2", "NIOSJr"]:
                print("Invalid Grade. Accepted grades are; 'A', 'AS', 'IGCSEL2' and 'NIOSJr' only.")
            else:
                Valid = True
        
        EmailID = input("EmailID: ")
        phoneNo = input("PhoneNo:  ")
        datak = [ID+1, Name, Grade, EmailID, phoneNo]
        
        current_node = self.head
        position = 0
        if position == ID:                                          # Find and update node with new values defined in the array datak
            current_node.data = datak                               # Uses linear search
            print("Entity updated successfully.")
        else:
            while(current_node != None and position != ID+2):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = datak
            else:
                print("Invalid ID. You could try the Search function to find ID")   
 
    def printLL(self):                                             # Print method for the linked list
        current_LNode = self.head                                  # Loop to print each Node in a new line
        while(current_LNode):
            print(current_LNode.data)
            current_LNode = current_LNode.next
    
llist = LinkedList()

def listToLL():                                                    # Function to convert A list (data_list) into a Linked List by inserting each row as a node in a loop
    for i in range(1,n):
        cur = data_list[i-1]
        llist.insertAtEnd(cur)
    return llist

def SortBy():                                                                                           #Function to prompt user to define how they want the record sorted. Inout is format checked and then converted into an integer
    SortBy = input("Would you like to sort by Name(N), EmailID(E), PhoneNo(P) or Grade(G)?  ")
    Valid = False
    while Valid == False:
        if SortBy == "N":
            Sortint = 1
            Valid = True
        elif SortBy == "E":
            Sortint = 3
            Valid = True
        elif SortBy == "P":
            Sortint = 4
            Valid = True
        elif SortBy == "G":
            Sortint = 2
            Valid = True
        else:
            print("Invalid input. Only 'N', 'E', 'P' or 'G' is accepted")
            SortBy = input("Would you like to sort by Name(N), EmailID(E), PhoneNo(P) or Grade(G)?  ")
    return Sortint                                                                                      #integer returned. The value is used to navigate through data_list

def bubbleSort(data_list):                                                                       #Bubble Sort function
    sort = SortBy()                                                                              #Calls SortBy function
    Valid = False
    swap = False
    for i in range(1, n-1):                                                                      #Outer loop
        for j in range(0, n-i-1):                                                                #Inner Loop
            if data_list[j][sort] > data_list[j+1][sort]:                                        #Compare adjacent values
                swap = True                                                                      #set swap as true if compare was successful
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]                      #Swaps adjacent values
        if not swap:
            return
    print("Sorted record is:")                                                                   #Iterate through data_list and print values
    for i in range(len(data_list)):
        print(data_list[i])

def insertionSort(data_list):                                                                    # Insertion Sort function
    
    sort = SortBy()                                                                              #calls SortBy() function
    
    for step in range(1, n-1):                                                                   #Outer loop   
        key = data_list[step][sort]                                                              #Define key for comparisons
        j = step - 1     
        while j > 0 and key < data_list[j][sort]:                                                #Compares key with next value in a loop
            data_list[j], data_list[j+1] = data_list[j+1], data_list[j]                          #Swap
            j = j - 1                                                                               
        data_list[j+1][sort] = key                                                               #New key to begin insertion loop again
    
    print("Sorted record is:")                                                                   #Print data_list line by line in a loop
    for i in range(1, len(data_list)):
        print(data_list[i])
    
class BNode:                                                   #Defining a Node in the Binary Search Tree
    def __init__(self, value, data):
        self.value = value                                     #Value holds the value being compared to find specified entity as given by the user
        self.data = data                                       # Data holds all the data corresponding to a value. IE Value = Saana then Data = [12,Saana, AS, saana.v@beyond8.net,289374980]
        self.left = None                                       # Pointer left
        self.right = None                                      # Pointer right
    
    def insertBST(self, value, data):                          #Function to insert Value's and data into a Binary Search Tree systematically
                                                               #Recursive if/else statements to find correct position for a recived value and store it along with its data
        if value < self.value:                                 #Compare input value to first value. First Value is the root, which is input later.
            if self.left is None:                              
                self.left = BNode(value, data)                 #Store at empty left node if compare was successful
            else:
                self.left.insertBST(value, data)
        else:
            if self.right is None:
                self.right = BNode(value, data)                #Store at empty right node if compare was unsuccessful
            else:
                self.right.insertBST(value, data)
    
    def binarySearch(self, value):                             #Binary Search function.
        if value < self.value:                                 #Comparing Values to navigate through the binarsy search tree
            if self.left is None:                              
                return False                                   #Returns False if value is not found
            else:
                return self.left.binarySearch(value)           
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.binarySearch(value)
        else:
            return self.data                                   #If Value is found, pulls data from that node which is displayed later

def initialiseBST(data_list):                                                               #Function to initialise a Binary Search Tree, basically using insertBST to input all values in data_list to the tree
    SortBy = input("Would you like to sort by Name(N), EmailID(E) or PhoneNo(P)?  ")  #Format check for input
    Valid = False                                                                      #Converting string input to pre-set integers
    while Valid == False:
        if SortBy == "N":
            Sortint = 1
            Valid = True
        elif SortBy == "E":
            Sortint = 3
            Valid = True
        elif SortBy == "P":
            Sortint = 4
            Valid = True
        else:
            print("Invalid input. Only 'N', 'E' or 'P' is accepted")
            SortBy = input("Would you like to sort by Name(N), EmailID(E) or PhoneNo(P)?  ")
    
    global tree                                         
    for i in range(1,n-1):                                          #Loop to Input each value of data_list into a binary tree named 'tree' one by one
        value = data_list[i][Sortint]                               #Sortint defines what basis the tree is organised on. (Name, Email, or phoneNo)
        valuep = data_list[i]
        if tree is None:
            tree = BNode(value, valuep)
        else:
            tree.insertBST(value, valuep)
    return tree

print("Welcome to Beyond 8 Learners database!")                    
valid = False
while valid == False:                                                           #While loop for format check
    temp = input("Would you like to view the current record(Y/N)?")
    if temp == "Y":                                     
        listToLL()                                                              #calls list to linked list function to convert data_list into a linked list and then prints it using printLL which is defined under LinkedList class
        llist.printLL()
        valid = True
    elif temp == "N":
        valid = True
    else:
        print("Invalid Input. Only 'Y' or 'N' is accepted")

valid = False
while valid == False:                                                           #While loop for format check
    temp = input("Edit(E), Sort(S) or Search(B)?  ")
    if temp == "E":
        while valid == False:                                                                       #While loop for format check
            tempk = input("Add Learner(A), Update Learner(U) or Remove Learner(R)?")
            if tempk == "A":
                Name = input("New Learner Name: ")                                                  #Prompting user for values to be added as new learner. values are added to an array and input to the linked list using insertAtEnd function

                Valid = False
                while Valid == False:                                                               #While loop for format check
                    Grade = input("Grade: ")
                    if Grade not in ["A", "AS", "IGCSEL2", "NIOSJr"]:
                        print("Invalid Grade. Accepted grades are; 'A', 'AS', 'IGCSEL2' and 'NIOSJr' only.")
                    else:
                        Valid = True
                
                EmailID = input("EmailID: ")
                phoneNo = input("PhoneNo:  ")
                ID = n-2
                datak = [ID, Name, Grade, EmailID, phoneNo]

                llist.insertAtEnd(datak)
                llist.printLL()

                valid = True
            elif tempk == "U":                                                              #Calls updateNode and prints updated linkedList
                ID = int(input("Please enter ID of Learner to be updated:  ")) - 1
                llist.updateNode(ID)
                llist.printLL()                
                valid = True
            elif tempk == "R":                                                              #Calls remove node at prints updated LinkedList
                ID = int(input("Please enter ID of learner to be removed:  ")) - 1
                llist.remove_at_index(ID)
                llist.printLL()
                valid = True
            else:
                print("Invalid Input. Only 'A', 'U' or 'R' is accepted")
        
        valid = True
    
    elif temp == "S":
        valid = False
        while valid == False:                                                       #While loop for format check
            tempk = input("Bubble Sort(B) or Insertion Sort(I)?  ")
            if tempk == "B":
                bubbleSort(data_list)                                               #Calls bubble sort function to bubble sort the list
                valid = True
            elif tempk == "I":
                insertionSort(data_list)                                            #calls insertion sort to insertion sort the list
                valid = True
            else:
                print("Invalid Input. Only 'B' or 'I' is accepted")
        valid = True
    elif temp == "B":                                                               #Calls BinarySearch to first create a binary tree with data_list as input
        tree = None                                                                 #Then prompts user for item to be searched for
        initialiseBST(data_list)            
        value = input("What would you like to search for?")
        printval = tree.binarySearch(value)                                         #Searches through the binary tree for item given by user
        print(printval)
        valid = True

    else:
        print("Invalid Input. Only 'E', 'S' or 'B' is accepted")


        





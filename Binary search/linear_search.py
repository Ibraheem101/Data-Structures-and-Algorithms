# -*- coding: utf-8 -*-

"""
QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.

"""

# def search(L, n):
#     for i in range(len(L)):
#         if L[i] == n:
#             return i
       
# print(search([], 9))
    
def search(L, n):
    position = 0
    while position < len(L):
        if L[position] == n:
            return position
        position += 1

print(search([9], 9))

# def locate_card(cards, query):
#     # Create a variable position with the value 0
#     position = 0
    
#     # Set up a loop for repetition
#     while True:
        
#         # Check if element at the current position matche the query
#         if cards[position] == query:
            
#             # Answer found! Return and exit..
#             return position
#         position += 1

# print(locate_card([], 7))
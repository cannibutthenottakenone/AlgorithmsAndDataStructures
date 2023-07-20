#
# A Supermarket simulation
#

import sys
sys.path.append("..")

from LinearStructures import Queue
import random


# A Customer has an ID and a random number of items
class Customer:
    def __init__(self, number, max_items):
        self.id = number
        # generate a random number of item between 1 and max_items
        self.items = # TODO


# A cash desk has and ID, a queue of clients and can serve one Customer at a time
class Cashdesk:
    def __init__(self, number):
        self.id = number
        self.queue = Queue()
        self.tot_customers_served = 0
        self.current_customer = None

    # Method to enqueue a new Customer c
    def addCustomer(self, c):

        # TODO


    # Method for check out
    #
    # if current_customer = None and queue not empty, then dequeue a Customer that becomes the current_customer
    #
    # if current_customer != None check the number of items:
    #     if it is zero: print a message with the cash desk and Customer ids, reset current_customer to None
    #                    and increase the tot_customers_served counter
    #     else: decrease the number of items of current_customer by 1
    #
    # Example of message: "Cash desk 1 served Customer number 2"
    #
    def checkOut(self):

        # TODO


# A Supermarket has a number of check desks specified by user
class Supermarket:
    def __init__(self, num_checdesks):
        # Initialize a list of check decks with dimension num_checdesks
        self.cashdesks_list =  # TODO

    # Return True if all the check desks are empty, False otherwise
    def isEmpty(self):

        # TODO

    # Add a new Customer to the check desk with the shortest queue
    def newCustomer(self, new_customer):

        # TODO

    # Execute the method checkOut for each check desks
    def run(self):

        # TODO

    # Print the total number of customers served by each check desks
    #
    # E.g.: Cash deck 1 served 2426 clients
    #       Cash deck 2 served 2361 clients
    #       ...
    #
    def printRecap(self):

        # TODO


# Test code
if __name__ == "__main__":
    num_checkdesks = 5    # number of check desks
    max_num_items = 20    # max number of items for each Customer
    num_customers = 10000 # total number of customers

    # Create an object Supermarket
    mySupermarket = Supermarket(num_checkdesks)
    # Create a list of Customer objects
    customers_list = [Customer(i, max_num_items) for i in range(num_customers, 0, -1)]

    #
    # Loop until all the customers are entered and served (i.e. both customer_list and all the queues are empty
    # A new Customer enters in the Supermarket with probability of 30% (use random function)
    # The function run is always called at each iteration
    #
    # TODO
    #


    # Print the total number of customers served by each check desk
    mySupermarket.printRecap()

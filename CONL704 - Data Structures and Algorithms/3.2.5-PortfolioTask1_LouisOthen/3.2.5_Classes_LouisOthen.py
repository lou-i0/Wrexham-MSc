#===========================================
# 1. Creating Class for Customer
#===========================================
import itertools #used to create an incremental ID
from datetime import datetime as dti # for datetime operations

class Customer:
    '''
    Creates a new customer on the online shopping system.
    '''
    newCustID  = itertools.count(100)
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName  = lastName
        self.customerID = next(self.newCustID)
        self.loginID = firstName[:1].lower() + lastName.lower() + str(self.customerID)[:2]
        
    def setAddress(self, address):
        self.__address = address
        return print(f'Confirmation that address for {self.firstName} {self.lastName} has been updated.')

        
    def setEmailAddress(self, emailAddress):
        self.__emailAddress = emailAddress
        return print(f'Confirmation that email address for {self.firstName} {self.lastName} has been updated.')
    
    def setContactNumber(self,contactNumber):
        self.__contactNumber = contactNumber
        return print(f'Confirmation that contact number for {self.firstName} {self.lastName} has been updated.')
    
    def customerDetails(self):
        
        print('Current details are as follows:')
        print(f'First Name: {self.firstName}')
        print(f'Last Name: {self.lastName}')
        print(f'CustomerID: {self.customerID}')
        print(f'loginID: {self.loginID}')
        custDetails = [self.firstName, self.lastName, self.customerID, self.loginID]
        
        return custDetails
    
    def fullName(self):
        fullName = f'{self.firstName} {self.lastName}'
        
        return fullName
    
#===========================================
# //////////////////////////////////////////
#===========================================
#===========================================
# 2. Creating Class for Account
#===========================================
class Account(Customer):
    '''
    Creates an Account that is aligned to the previously created Customer.
    '''
    def __init__(self, loginID):
        self.loginID = loginID
        self.__password = None
        
        return print(f'Account {self.loginID} has been created.')
        
    def getLogin(self):
        print('Your loginID is as follows:')
        return self.loginID
        
    def setPassword(self):
        self.__password = input('Please create a new password for your loginID: ')
        return print(f'Confirmation that your password for {self.loginID} has now been updated.')
    #===========================================
# //////////////////////////////////////////
#===========================================
#===========================================
# 3. Creating Class for Item
#===========================================
class Item:
    newItemID  = itertools.count(5001)
    def __init__(self, itemName,itemStock,itemPrice):
        self.itemID = next(self.newItemID)
        self.itemName = itemName
        self.itemStock = itemStock
        self.itemPrice = itemPrice
        return print(f'New item added {self.itemName} with ID {self.itemID}')
    
    def inStock(self):
        if self.itemStock > 0:
            print(f'{self.itemID}: {self.itemName} are in stock with quantity of {self.itemStock}')
        elif self.itemStock <= 0:
            print(f'{self.itemID}: {self.itemName} are currently out of stock')
            
    def updateStock(self, itemStock):
        self.itemStock = itemStock
        return print(f'Confirmation that {self.itemID}: {self.itemName} has a stock of {self.itemStock}')

#===========================================
# //////////////////////////////////////////
#===========================================
#===========================================
# 4. Creating Class for Item Category
#===========================================
class ItemCategory(Item):
    def __init__(self, itemID,itemCategory):
        self.itemCategory = itemCategory
        self.itemID = itemID
        return print(f'ItemID {self.itemID} has been assigned to category: {self.itemCategory}')
#===========================================
# //////////////////////////////////////////
#===========================================
#===========================================
# 5. Creating Class for Order
#===========================================
class Order(Customer, Item):
    '''
     Ability for a customer to create an order based on the items to purchase
    '''
    newOrderId  = itertools.count(10001)
    def __init__(self, customerID, orderItems,itemPrice):
        self.orderID = next(self.newOrderId)
        self.orderDate = dti.now().date()
        self.orderStatus = 'Initialised'
        self.orderItems = orderItems
        self.orderItemPrice = itemPrice
        self.orderTotal = sum(itemPrice)
        self.customerID = customerID
        return print(f'Order {self.orderID} has been created') 
        
    def checkOrder(self):
        print('Current order details are as follows:')
        print(f'OrderID: {self.orderID}')
        print(f'Date Ordered: {self.orderDate}')
        print(f'CustomerID: {self.customerID}')
        print(f'Item(s) ordered: {self.orderItems}')
        print(f'Total Cost: £{self.orderTotal}')
        
        orderDetails = [self.orderID, self.orderDate, self.customerID,self.orderItems,self.orderTotal]
        
        return orderDetails
    
    def updateOrderStatus(self, status):
        self.orderStatus = status
        return print(f'Order status of {self.orderID} is now {self.orderStatus}.')
    
    def removeItem(self, itemID):
        try:
            if itemID in self.orderItems:
                index_pos = self.orderItems.index(itemID)
                self.orderItems.remove(itemID)
                self.orderItemPrice.pop(index_pos)
                self.orderTotal = sum(self.orderItemPrice)
            else:
                print('That item does not exist on this order.')
        except ValueError:
            print('That item does not exist on the order.')
#===========================================
# //////////////////////////////////////////
#===========================================
#===========================================
# 5. Creating Class for Payment
#===========================================
class Payment(Order):
    newPayID = itertools.count(25001)
    def __init__(self, orderID, paymentStatus = 'onhold'):
        self.paymentID = next(self.newPayID)
        self.orderID = orderID
        self.paymentDate = None
        self.paymentStatus = paymentStatus
        return print(f'Payment {self.paymentID} for order {orderID} has been logged awaiting confirmation.')
    
    def getPaymentInfo(self):
        print('Current payment details are as follows:')
        print(f'Payment ID: {self.paymentID}')
        print(f'OrderID: {self.orderID}')
        print(f'Date paid: {self.paymentDate}')
        print(f'Payment Status: {self.paymentStatus}')
        
    def updatePaymentStatus(self,status):
        self.paymentStatus =  status
        if status  == 'paid':
            self.paymentDate == dti.now().date()
        return print(f'Status for payment {self.paymentID} has now been updated')

#===========================================
#1 Testing Customer Class
#===========================================
print('======================')
print('Create a Customer')
print('----------------------')
louis = Customer('Louis','Othen')
louis.setAddress('21 Southcliff Road, Southampton, SO14 6GE')
louis.setEmailAddress('s21002027@mail.glyndwr.ac.uk')
louis.setContactNumber('07378347694')
print(louis.fullName())
#print(louis.address) # this should not work as it is private
print(louis.lastName) # this however, should
print(louis.customerDetails())
print('======================')
print('//////////////////////')
#===========================================
#//////////////////////////////////////////
#===========================================
#===========================================
#2 Testing Account Class
#===========================================
print('======================')
print('Create an account')
print('----------------------')
louis_account = Account(loginID = louis.loginID)
print(louis_account.getLogin())
louis_account.setPassword()
print('======================')
#===========================================
#//////////////////////////////////////////
#===========================================
#===========================================
#3 Testing Item Class
#===========================================
print('======================')
print('Creating Items')
print('----------------------')
test_item_1 = Item('Mobile Phone',52,500)
test_item_2 = Item('Tablet',100,115)
test_item_3 = Item('Headphones',0,100)
print('----------------------')
Item.inStock(test_item_1)
Item.inStock(test_item_3)
print('----------------------')
Item.updateStock(test_item_3,50)
Item.inStock(test_item_3)
print('======================')
#===========================================
#//////////////////////////////////////////
#===========================================
#===========================================
#4 Testing Item Category Class
#===========================================
print('======================')
print('Creating an Item Category')
print('----------------------')
item_cat_1 = ItemCategory(test_item_1.itemID, 'Communications')
item_cat_2 = ItemCategory(test_item_2.itemID, 'Communications')
item_cat_3 = ItemCategory(test_item_3.itemID, 'Audio')
print('======================')
#===========================================
#//////////////////////////////////////////
#===========================================
#===========================================
#5 Testing Order Class 
#===========================================
print('======================')
print('Create an order')
print('----------------------')
louis_order = Order(louis.customerID,[test_item_1.itemID,test_item_2.itemID],[test_item_1.itemPrice,test_item_2.itemPrice])
print('----------------------')
Order.checkOrder(louis_order)
print('----------------------')
Order.updateOrderStatus(louis_order,'Awaiting Payment')
print('----------------------')
Order.removeItem(louis_order,test_item_2.itemID)
print('----------------------')
Order.checkOrder(louis_order)
print('======================')
#===========================================
#//////////////////////////////////////////
#===========================================
#===========================================
#6 Testing Payment Class 
#===========================================
print('======================')
print('Create an Payment Record')
print('----------------------')
louis_payment = Payment(louis_order.orderID, 'onhold')
print('----------------------')
Payment.getPaymentInfo(louis_payment)
print('----------------------')
Payment.updatePaymentStatus(louis_payment,'paid')
print('----------------------')
Payment.getPaymentInfo(louis_payment)
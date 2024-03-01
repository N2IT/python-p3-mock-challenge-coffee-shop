from many_to_many import Coffee
from many_to_many import Customer
from many_to_many import Order

customer = Customer("Johnny")
customer1 = Customer("Bodi")
customer2 = Customer("War Child")
customer3 = Customer("Xaviman")

coffee = Coffee("Americano")
coffee1 = Coffee("Cafe Latte")
coffee2 = Coffee("Cordito Esspresso")
coffee3 =  Coffee("Cafe Mocha")

order1 = Order(customer, coffee1, 4.99)

print(order1)
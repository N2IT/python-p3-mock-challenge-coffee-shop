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
order2 = Order(customer, coffee, 3.49)
order3 = Order(customer1, coffee3, 5.99)
order4 = Order(customer3, coffee2, 2.99)
order5 = Order(customer2, coffee1, 4.99)
order6 = Order(customer2, coffee2, 2.99)
order7 = Order(customer1, coffee, 3.49)

print(Coffee.num_orders(coffee3))
# print(f'coffee1 customer: {coffee1._customers}')
# print(f'coffee2 customer: {coffee2._customers}')
# print(f'coffee3 customer: {coffee3._customers}')
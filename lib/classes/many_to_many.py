class Coffee:
    def __init__(self, name):
        self._name = name

        # attribute for Customers
        self._customers = []

        # attribute for Order
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and len(name) > 3:
                self._name = name

    def orders(self):
        return [ order for order in Order.all if order.coffee == self ]
    
    def customers(self):
        coffee_customers = []
        for order in Order.all:
            if order.coffee == self:
                if order.customer not in coffee_customers:
                    coffee_customers.append(order.customer)
        return coffee_customers
    
    def num_orders(self):
        coffee_tracker = {}
        for order in Order.all:
            if order.coffee not in coffee_tracker:
                coffee_tracker[self] = 0
            else:
                coffee_tracker[self] += 1

        return coffee_tracker[self]
    
    def average_price(self):
        coffee_orders = []
        # order_value = sum(coffee_orders)
        # order_count = len(coffee_orders)
        for order in Order.all:
            if order.coffee == self:
                coffee_orders.append(order.price)
        order_value = sum(coffee_orders)
        order_count = len(coffee_orders)
        return order_value / order_count

    def __repr__(self):
        return f"{self.name}"

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

        # attritute for Coffee
        self._coffees = []

        # attribute for Orders
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance (name, str) and 1 < len(name) < 15:
            self._name = name
        
    def orders(self):
        return [ order for order in Order.all if order.customer == self ]
    
    def coffees(self):
        coffees_ordered = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in coffees_ordered:
                    coffees_ordered.append(order.coffee)
        return coffees_ordered
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        if isinstance(order, Order):
            return order

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spend = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spend:
                    customer_spend[order.customer] = order.price
                else:
                    customer_spend[order.customer] += order.price
        return max(customer_spend, key = customer_spend.get)

    # iterate through each order within the Order.all list
    # append 


    def __repr__(self):
        return f"{self.name}"

    
class Order:
    
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

        # connect to Coffee
        self.coffee._customers.append(self.customer)
        self.coffee._orders.append(self)

        #connect to Customer
        self.customer._coffees.append(self.coffee)
        self.customer._orders.append(self)
    
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not hasattr(self, "price"):
            if isinstance(price, float) and 1.0 < price < 10.0:
                self._price = price


    def __repr__(self):
        return f"Coffee: {self.coffee}\nCustomer: {self.customer}\nPrice: {self.price}"
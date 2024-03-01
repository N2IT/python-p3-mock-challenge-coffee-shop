class Coffee:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and len(name) > 3:
                self._name = name
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, cust_name):
        self.cust_name = cust_name

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if isinstance (name, str) and 1 < len(name) < 15:
    #         self._name = name
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
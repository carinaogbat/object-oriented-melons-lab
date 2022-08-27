"""Classes for melon orders."""
import datetime
# now = datetime.datetime.timestamp()
# print(now)
weekday = datetime.datetime.today().weekday()
#monday is 0, sunday is 6
print(weekday)
now = datetime.datetime.now()
current_time = now.time()
time_in_string = current_time.strftime("%H")

print(current_time)
print(time_in_string)

class AbstractMelonOrder():
    order_type = None
    tax = None 
    def __init__(self, species, qty):
        
        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_base_price(self):
        import datetime
        weekday = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        current_time = now.time()
        time_in_string = current_time.strftime("%H")
        import random
        base_price = range(5,10)
        base_price = random.choice(base_price)
        return base_price
       
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == 'Christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total + 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0

    passed_inspection = False


    def mark_inspection(self):
        self.passed_inspection = True
    
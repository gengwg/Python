import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternative constructor
    @classmethod
    def today(cls): # the first parameter is the class itself
        # This alternative constructor uses the current date
        # to create an instance of Date.
        # It allows you to create instances without needing to pass parameters.
        # It is a factory method that returns an instance of Date.
        today = time.localtime()
        return cls(today.tm_year, today.tm_mon, today.tm_mday)

    # __new__ method is used to create an uninitialized instance    
    @classmethod
    def today2(cls):
        # This alternative constructor uses __new__ to create an uninitialized instance
        # and then initializes it with the current date.
        # Note: This is not a common practice and should be used with caution.
        # It is generally better to use the primary constructor or factory methods.
        d = cls.__new__(cls)  # Create an uninitialized instance
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

if __name__ == "__main__":
    # Using the primary constructor
    date1 = Date(2023, 10, 5)
    print(f"Date1: {date1.year}-{date1.month}-{date1.day}")

    # Using the alternative constructor
    date2 = Date.today()
    print(f"Date2: {date2.year}-{date2.month}-{date2.day}")

    # Demonstrating __new__ method
    print("Demonstrating __new__ method:")
    # Creating an uninitialized instance
    # This is useful for custom initialization logic
    # or when you want to set attributes after creation.
    # Note: This is not a common practice and should be used with caution.
    print("Creating an uninitialized Date instance:")
    d = Date.__new__(Date)
    print(f"New Date instance: {d}")
    try:
        d.year
    except AttributeError as e:
        print(f"Error accessing year on uninitialized instance: {e}")

    data = {'year': 2023, 'month': 10, 'day': 5}
    for key, value in data.items():
        setattr(d, key, value)
    print(f"Initialized Date instance: {d.year}-{d.month}-{d.day}")

    # Using the alternative constructor with __new__
    print(f"Using __new__ alternative constructor:")
    date3 = Date.today2()
    print(f"Date3: {date3.year}-{date3.month}-{date3.day}")
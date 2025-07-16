from datetime import datetime

class Birthday:

    # Some data for this object
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Basic constructor
    def __init__(self, month, day):
        # Protect month value
        if month >= 1 and month <= 12:
            self.__month = month
        else:
            # if garbage, I, the developer, call the month
            self.__month = 1
        # At this point we have a legit month value 1-12.
        # Protect day value; use -1 in array to synchronize months
        if day >= 1 and day <= Birthday.days_in_month[month - 1]:
            self.__day = day
        else:
            # if garbage, we call the day too
            self.__day = 1

    # Mutator for __day
    def set_day(self, day):
        if day > 0 and day <= Birthday.days_in_month[self.__month-1]:
            self.__day = day

    # Accessor for __month
    def get_month(self):
        return self.__month

    # Accessor for __day
    def get_day(self):
        return self.__day

    # Compute days to birthday
    def days_until(self):
        # obtain today's date
        # extract month and day
        # subtract from birthday
        # return # of days
        today = datetime.today()
        
    def day_in_year(self, month, day):
        count = 0
        for i in range(month-1):
            count += Birthday.days_in_month[i]
        return count + day

    def __str__(self):
        return f"[ {self.get_month()}/{self.get_day()} ]"
    
    
    def is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



if __name__ == "__main__":
    leo = Birthday(6, 28)
    # leo.month = 6
    leo.set_day(29)
    print(leo)
    print(leo.day_in_year(6,29))

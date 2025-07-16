from datetime import date

class Person:

    # define state: what are the variables of the object
    # The best way to show an object's variables (aka attributes or fields)
    # is to show how an object is instantiated.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._ssn = -1 # private please
        self._dob = None

    # define behavior: what are the method the object offers?
    def introduce(self):
        print(f"\nHello, my name is {self.first_name} and I am {self.get_age()} years old.")

    def set_ssn(self, ssn: int) -> None:
        # simple rule: SSNs cannot have all-0s in any of their parts. For example,
        # 000-GG-SSSS, AAA-00-SSSS, and AAA-GG-0000 are illegal values. The method
        # should not allow such values. If SSN security number is to be represented
        # as an integer, then 000-GG-SSSS becomes GGS,SSS whose greatest value is
        # 999,999. So any SSN has to have an int value > 999,999, etc. We wont 
        # worry about the other restrictions for now because, really, SSN, should be
        # an object itself, not an int variable.
        if ssn < 1_000_000:
            raise ValueError("SSN cannot start with 000")
        else:
            self._ssn = ssn
    
    
    def set_dob(self, year, month, day):
        self._dob = date(year, month, day)
    
    def get_age(self):
        age = -1
        if self._dob:
            today = date.today()
            age = today.year-self._dob.year
            if (today.month, today.day) < (self._dob.month, self._dob.day):
                age -= 1
        return age
    
    def get_name(self):
        return self.first_name
    
    def __str__(self):
        return f"[ {self.first_name} {self.last_name}]"
    
    def __lt__(self, other):
        return self.get_age() < other.get_age()
    #def __gt__(self, other):
    #    return self.get_age() > other.get_age()
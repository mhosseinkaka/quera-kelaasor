
class Person:
    '''
    This class takes a name and an age,
    calls the birthday method and and returns the output as a number.
    '''
    def __init__(self, name: str, age: int):
        '''
        Creates an object by taking a name and age.
        '''
        assert type(name) == str, "enetr yor currect name"
        assert type(age) == int, "enter your age as a number"
        self.name = name
        self.age = age

    
    def birthday(self) -> int: 
        '''
        The birthday method takes a number as input, adds one to it, and returns the new number.
        '''
        self.age += 1
        return self.age




# test_case_1
# p = Person("Alice", 25)  
# p.birthday() 
# print(p.age)
    

# test_case_2
# p = Person("kiomars", 18)  
# p.birthday() 
# print(p.age)
    
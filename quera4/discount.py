class Discount:
    '''
    This class determines the discount amount based on the input it receives and determines the final payment amount.
    '''
    def __init__(self, discount_value) -> None:
        '''
        This function creates a discount object and specifies whether the entered amount should be deducted directly from the total amount or applied to the total amount after calculating the discount.
        '''
        self.discount_value = discount_value
        if isinstance(discount_value, (int, float)):
            self.type_dis = "fix"
            self.discount_value = float(discount_value)
        else:
            discount_value = discount_value.strip()
            self.type_dis = "flex"
            self.discount_value = float(discount_value[:-1]) / 100

    def __call__(self, price: float) -> float:
        '''
        This function calculates the final cost after taking the type of discount applied and the total amount.
        '''
        assert isinstance(price, (int, float)), "enter price as a number"
        if self.type_dis == "flex":
            return price * (1 - self.discount_value)
        else:
            return price - self.discount_value
        


# test_case_1
d1 = Discount(20) # fixed -20 dollar discount 
print(d1(100)) # prints 80
print(d1(200)) # prints 180

# test_case_2
d2 = Discount("20%") # 20 percent discount
print(d2(100)) # prints 80
print(d2(200)) # prints 160
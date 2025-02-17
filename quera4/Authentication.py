
from __future__ import annotations
import hashlib
class User:
    '''
    This class creates a user.
    Performs encryption operations.
    Performs comparison operations of encrypted passwords.
    '''
    def __init__(self, username, password):
        '''
        A user object is created with username and password properties.
        '''
        self.username = username
        self.password = self.hash_password(password)
        
    def get_username(self) -> str:
        return self.username
    
    def set_username(self, username: str) -> None:
        self.username = username

    def hash_password(self, password):
        '''
        Encrypts user input password
        '''  
        return hashlib.sha256(password.encode()).hexdigest()
       
    def authenticate(self, password: str) -> bool:
        '''
        Encrypts the new password and matches it with the old password.
        '''
        return self.password == self.hash_password(password)

class Authentication:
    '''
    This class performs authentication operations using its methods.
    '''
    def __init__(self):
        '''
        Creates a list of users.
        '''
        self.user_list = []

    def add_user(self, username: str, password: str) -> None:
        '''
        By calling the User class, a new user is created and added to the list.
        '''
        new_user = User(username, password)
        self.user_list.append(new_user)

    def user_exists(self, username: str) -> bool:
        '''
        Checks if this username exists in the user list.
        '''
        return any(user.get_username() == username for user in self.user_list)

    def check_username(self, username: str) -> bool:
        '''
        Checks which username this matches in the user list.
        '''
        return self.user_exists(username)

    def check_password(self, username: str, password: str) -> bool:
        '''
        It takes the password and verifies the password by calling the authentication method of the User class with the old encrypted password.
        '''
        user = next((user for user in self.user_list if user.get_username() == username), None)
        if user is None:
            return False  
        return user.authenticate(password)

    def authenticate_user(self, username: str, password: str) -> bool:
        '''
        A username and password are given and each authentication step is performed by calling its method and returning the result.
        '''
        user_exists = self.user_exists(username)
        username_correct = self.check_username(username)
        password_correct = self.check_password(username, password)

        return user_exists, username_correct, password_correct

# test_case:
user_Authentication = Authentication() 
user_Authentication.add_user("Faezeh", "123456")
user_Authentication.add_user("Fariborz", "ffborz")
user_Authentication.add_user("Hamed", "kelaasor")


print(user_Authentication.authenticate_user("Mohammad", "123456")) 

print(user_Authentication.authenticate_user("Fariborz", "ffborze")) 

print(user_Authentication.authenticate_user("Hamed", "kelaasor")) 


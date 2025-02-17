
from __future__ import annotations
import hashlib
class User:
    '''
    این کلاس یک کاربر ایجاد میکند.
    عملیت رمزنگاری را انجام میدهد.
    عملیات مقایسه پسوردهای رمزنگاری شده را انجام میدهد
    '''
    def __init__(self, username, password):
        '''
        یک ابجکت یوزر با ویژگی های نام کاربری و پسورد ساخته می شود
        '''
        self.username = username
        self.password = self.hash_password(password)
        
    def get_username(self) -> str:
        return self.username
    
    def set_username(self, username: str) -> None:
        self.username = username

    def hash_password(self, password):
        '''
        پسورد وردی کاربر را رمزنگاری میکند
        '''  
        return hashlib.sha256(password.encode()).hexdigest()
       
    def authenticate(self, password: str) -> bool:
        '''
        پسورد جدید را رمزنگاری کرده و با پسورد قدیم مطابقت میدهد
        '''
        return self.password == self.hash_password(password)

class Authentication:
    '''
    این کلاس با استفاده از متدهایی که دارد، عملیات احراز هویت را انجام میدهد
    '''
    def __init__(self):
        '''
        لیست کاربران را ایجاد میکند
        '''
        self.user_list = []

    def add_user(self, username: str, password: str) -> None:
        '''
        با فراخوانی کلاس یوزر، یک کاربر جدید ایجاد شده و به لیست اضافه میگردد.
        '''
        new_user = User(username, password)
        self.user_list.append(new_user)

    def user_exists(self, username: str) -> bool:
        '''
        بررسی میکند این نام کاربری در لیست کاربران وجود دارد یا خیر
        '''
        return any(user.get_username() == username for user in self.user_list)

    def check_username(self, username: str) -> bool:
        '''
        بررسی میکند این نام کاربری با کدام نام کاربری در لیست کاربران مطابقت دارد.
        '''
        return self.user_exists(username)

    def check_password(self, username: str, password: str) -> bool:
        '''
        رمز عبور را میگیرد و بافراخوانی متد احراز هویت کلاس یوزر با پسورد رمزنگاری شده قدیم، صحبت پسورد را تایید میکند.
        '''
        user = next((user for user in self.user_list if user.get_username() == username), None)
        if user is None:
            return False  
        return user.authenticate(password)

    def authenticate_user(self, username: str, password: str) -> bool:
        '''
        نام کاربری و پسورد داده می شود و هر مرحله احراز هویت را با فراخوانی متد آن انجام میدهد و نتیجه را برمیگرداند
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


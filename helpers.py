import random
import string
from random import randint, choice
from datetime import datetime, timedelta

class RandomDataGenerator:
    CYRILLIC_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    SPECIAL_CHARS = ' .,-()№#!?;:"' + string.digits
    LENGTHS = {
        'name': (3, 10),
        'last_name': (5, 15),
        'address': (15, 20),
        'comment': (20, 50)
    }

    @staticmethod
    def _generate_random_string(length, use_special_chars=False):
        chars = RandomDataGenerator.CYRILLIC_LETTERS
        if use_special_chars:
            chars += RandomDataGenerator.SPECIAL_CHARS
        
        return ''.join(choice(chars) for _ in range(length))
    
    @staticmethod
    def get_random_phone():
        return f"9{randint(9000000000, 9999999999)}"
    
    @staticmethod
    def get_random_name():
        length = randint(*RandomDataGenerator.LENGTHS['name'])
        return RandomDataGenerator._generate_random_string(length).capitalize()
    
    @staticmethod
    def get_random_last_name():
        length = randint(*RandomDataGenerator.LENGTHS['last_name'])
        return RandomDataGenerator._generate_random_string(length).capitalize()
    
    @staticmethod
    def get_random_address():
        address_parts = [
            f"ул. {RandomDataGenerator._generate_random_string(randint(5, 12)).capitalize()}",
            f"д. {randint(1, 150)}"
        ]
        return ', '.join(address_parts)
    
    @staticmethod
    def get_random_comment():
        base_length = randint(*RandomDataGenerator.LENGTHS['comment'])
        return RandomDataGenerator._generate_random_string(base_length, use_special_chars=True)
    
    @staticmethod
    def get_random_date():
        today = datetime.now()
        end_of_year = datetime(today.year, 12, 31)
        days_remaining = (end_of_year - today).days
        random_days = random.randint(1, days_remaining)
        future_date = today + timedelta(days=random_days)
        return future_date.strftime("%d.%m.%Y")

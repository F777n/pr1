import json
from datetime import datetime

user = [
    { 'username': 'Петя', 
    'password': '12345',
     'role': 'user', 
     'history': [], 
     'created_at': str(datetime.now())}
]
medicines = [
    {'name':'Парацетамол', 'price': 100, 'quantity': 10, 'rating': 4.5},
    {'name':'Цитрамон', 'price': 150, 'quantity': 5, 'rating': 4.8}, 
    {'name':'Супрастин', 'price': 200, 'quantity': 10, 'rating': 4.7},
    {'name':'Омега', 'price': 300, 'quantity': 3, 'reting': 5.0},
    {'name':'Мезим', 'price': 350, 'quantity': 15, 'rating': 4.5},
    {'name':'Звездочка','price': 100, 'quantity': 20, 'rating': 5.0}, 
    {'name':'Аскорбинка', 'price': 5000, 'quantity': 100, 'rating':5.0},
    {'name':'Ёд','price': 100, 'quantity': 50, 'rating': 4.9},
    {'name':'Пластырь', 'price': 500, 'quantity': 100, 'rating':4.2},
    {'name':'АЦЦ', 'price': 800, 'quantity':6, 'rating': 4.4},
    {'name':'Снуп', 'price': 1000, 'quantity': 7, 'rating':4.6}
]

def authenticate(username, password):
    for user in users:
        if user ['username'] == username and user ['password'] == password:
            return user
            return None 

def view_medecines():
    print("\nДоступные лекарства:")
    for index, medicine in enumerate(medicines):
        print(f"{index + 1}"). {medicine['name']} - {medicine['price']} 


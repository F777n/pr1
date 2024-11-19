import json
from functools import reduce


users = [
    {'username': 'Петя', 'password': '1234', 'role': 'user', 'history': [], 'basket': []},
    {'username': 'admin', 'password': '1234', 'role': 'admin'}
]

medicines = [
    {'name': 'Парацетамол', 'price': 100, 'quantity': 10, 'rating': 4.5, 'category': 'обезболивающее'},
    {'name': 'Цитрамон', 'price': 150, 'quantity': 5, 'rating': 4.8, 'category': 'обезболивающее'},
    {'name': 'Супрастин', 'price': 200, 'quantity': 10, 'rating': 4.7, 'category': 'антигистаминное'},
    {'name': 'Омега', 'price': 300, 'quantity': 3, 'rating': 5.0, 'category': 'витамины'},
    {'name': 'Мезим', 'price': 350, 'quantity': 15, 'rating': 4.5, 'category': 'ферменты'},
    {'name': 'Звездочка', 'price': 100, 'quantity': 20, 'rating': 5.0, 'category': 'противопростудное'},
    {'name': 'Аскорбинка', 'price': 5000, 'quantity': 100, 'rating': 5.0, 'category': 'витамины'},
    {'name': 'Йод', 'price': 100, 'quantity': 50, 'rating': 4.9, 'category': "другие"},
    {'name': 'Пластырь', 'price': 500, 'quantity': 100, 'rating': 4.2, 'category': "другие"},
    {'name':'АЦЦ', "price":800,"quantity":6,"rating":4.4,"category":"обезболивающее"},
    {'name':'Снуп', "price":1000,"quantity":7,"rating":4.6,"category":"противопростудное"},
    {'name':'Таблетки от горла','price':200,'quantity':30,'rating':4.0,'category':'таблетки от горла'},
    {'name':'Леденцы для горла','price':150,'quantity':50,'rating':3.5,'category':'таблетки от горла'}
]


def authorize():
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль.")
    return None


def user_menu(user):
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть товары")
        print("2. Купить товар")
        print("3. Посмотреть историю покупок")
        print("4. Посмотреть корзину")
        print("5. Добавить в корзину")
        print("6. Удалить из корзины")
        print("7. Сортировать товары по цене")
        print("8. Фильтровать товары по количеству")
        print("9. Поиск товара по названию")
        print("10. Посмотреть категории лекарств")
        print("11. Посмотреть лекарства по рейтингу")
        print("12. Посчитать стоимость товаров в корзине")
        print("13. Выйти")

        choice = input("Ваш выбор: ")
        
        try:
            if choice == "1":
                view_products()
            elif choice == "2":
                buy_product(user)
            elif choice == "3":
                view_history(user)
            elif choice == "4":
                view_basket(user)
            elif choice == "5":
                add_to_basket(user)
            elif choice == "6":
                remove_from_basket(user)
            elif choice == "7":
                sort_products_by_price()
            elif choice == "8":
                filter_products_by_quantity()
            elif choice == "9":
                search_product()
            elif choice == "10":
                view_categories()
            elif choice == "11":
                view_products_by_rating()
            elif choice == "12":
                calculate_basket_total(user)
            elif choice == "13":
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def view_products():
    print("\nДоступные товары:")
    for product in medicines:
        print(f"{product['name']} - {product['price']} руб. (в наличии: {product['quantity']}, категория: {product['category']}, рейтинг: {product['rating']})")

def buy_product(user):
    product_name = input("Введите название товара для покупки: ")
    for product in medicines:
        if product['name'] == product_name and product['quantity'] > 0:
            product['quantity'] -= 1
            user['history'].append(product_name)
            print(f"Вы купили {product_name}.")
            return
    print("Товар недоступен.")

def view_history(user):
    print("\nВаша история покупок:")
    if not user['history']:
        print("История покупок пуста.")
    else:
        for item in user['history']:
            print(item)

def add_to_basket(user):
    product_name = input("Введите название товара для добавления в корзину: ")
    for product in medicines:
        if product['name'] == product_name and product['quantity'] > 0:
            user['basket'].append(product_name)
            print(f"{product_name} добавлен в корзину.")
            return
    print("Товар недоступен.")

def remove_from_basket(user):
    product_name = input("Введите название товара для удаления из корзины: ")
    if product_name in user['basket']:
        user['basket'].remove(product_name)
        print(f"{product_name} удален из корзины.")
    else:
        print(f"{product_name} не найден в корзине.")

def view_basket(user):
    print("\nВаша корзина:")
    if not user['basket']:
        print("Корзина пуста.")
    else:
        for item in user['basket']:
            print(item)

def calculate_basket_total(user):
    try:
        total_price = reduce(lambda acc, item: acc + next((prod['price'] for prod in medicines if prod['name'] == item), 0), user['basket'], 0)
        
        if total_price > 0:
            print(f"Общая стоимость товаров в корзине: {total_price} руб.")
        else:
            print("Ваша корзина пуста или товары недоступны.")
    
    except Exception as e:
        print(f"Произошла ошибка при подсчете общей стоимости: {e}")

def sort_products_by_price():
    sorted_products = sorted(medicines, key=lambda x: x['price'])
    print("\nТовары отсортированы по цене:")
    for product in sorted_products:
        print(f"{product['name']} - {product['price']} руб.")

def filter_products_by_quantity():
    threshold = int(input("Введите минимальное количество товара для фильтрации: "))
    
    filtered_products = list(filter(lambda x: x['quantity'] >= threshold, medicines))
    
    if filtered_products:
        print("\nТовары с количеством больше или равным", threshold)
        for product in filtered_products:
            print(f"{product['name']} - {product['price']} руб.")
    else:
        print("Нет товаров, соответствующих критериям фильтрации.")

def search_product():
    search_term = input("Введите название товара для поиска: ").lower()
    
    found_products = list(filter(lambda x: search_term in x['name'].lower(), medicines))
    
    if found_products:
        print("\nНайденные товары:")
        for product in found_products:
            print(f"{product['name']} - {product['price']} руб.")
    else:
        print("Товары не найдены.")

def view_categories():
    categories = set(product['category'] for product in medicines)
    
    print("\nДоступные категории лекарств:")
    for category in categories:
        print(f"- {category}")

def view_products_by_rating():
    sorted_products = sorted(medicines, key=lambda x: x['rating'], reverse=True)
    
    print("\nЛекарства отсортированы по рейтингу:")
    for product in sorted_products:
        print(f"{product['name']} - {product['price']} руб.")


def admin_menu(admin):
   while True:
       print("\nВыберите действие:")
       print("1. Просмотреть товары")
       print("2. Добавить товар")
       print("3. Удалить товар")
       print("4. Редактировать товар")
       print("5. Управление пользователями")
       print("6. Выйти")

       choice = input("Ваш выбор: ")
       
       try:
           if choice == "1":
               view_products()
           elif choice == "2":
               add_product()
           elif choice == "3":
               remove_product()
           elif choice == "4":
               edit_product()
           elif choice == "5":
               manage_users()
           elif choice == "6":
               break
           else:
               print("Неверный выбор.")
       except Exception as e:
           print(f"Произошла ошибка: {e}")

def add_product():
   name = input("Введите название товара: ")
   price = float(input("Введите цену товара: "))
   quantity = int(input("Введите количество товара: "))
   rating = float(input("Введите рейтинг товара (от 3 до 5): "))
   
   
   if rating < 3 or rating > 5:
       print("Рейтинг должен быть от 3 до 5.")
       return
   
   category = input("Введите категорию товара: ")
   medicines.append({'name': name,
                     'price': price,
                     'quantity': quantity,
                     'rating': rating,
                     'category' : category})
   print(f"Товар {name} добавлен.")

def remove_product():
   name = input("Введите название товара для удаления: ")
   global medicines
   medicines = [product for product in medicines if product['name'] != name]
   print(f"Товар {name} удален.")

def edit_product():
   name = input("Введите название товара для редактирования: ")
   for product in medicines:
       if product['name'] == name:
           new_price = float(input(f"Введите новую цену для {name} (текущая цена: {product['price']}): "))
           new_quantity = int(input(f"Введите новое количество для {name} (текущее количество: {product['quantity']}): "))
           new_rating = float(input(f"Введите новый рейтинг для {name} (текущий рейтинг: {product['rating']}): "))
           
         
           if new_rating < 3 or new_rating > 5:
               print("Рейтинг должен быть от 3 до 5.")
               return
           
           new_category = input(f"Введите новую категорию для {name} (текущая категория: {product['category']}): ")
           
           product['price'] = new_price
           product['quantity'] = new_quantity
           product['rating'] = new_rating
           product['category'] = new_category
           
          
           log_changes(name)
           
           print(f"Товар {name} обновлен.")
           return
   
   print(f"Товар с названием {name} не найден.")


def log_changes(product_name):
   with open('changes_log.txt', mode='a') as log_file:
       log_file.write(f"Изменен товар: {product_name}\n")

def manage_users():
   while True:
       print("\nУправление пользователями:")
       print("1. Просмотреть пользователей")
       print("2. Добавить пользователя")
       print("3. Удалить пользователя")
       print("4. Выйти")

       choice = input("Ваш выбор: ")
       
       try:
           if choice == "1":
               view_users()
           elif choice == "2":
               add_user()
           elif choice == "3":
               remove_user()
           elif choice == "4":
               break
           else:
               print("Неверный выбор.")
       except Exception as e:
           print(f"Произошла ошибка: {e}")

def view_users():
   if not users:
       print("\nНет зарегистрированных пользователей.")
   else:
       
       for user in users:
           role = user['role']
           username = user['username']
           history_count = len(user['history'])
           
          
           print(f"Имя: {username}, Роль: {role}, История покупок: {history_count} записей")

def add_user():
   username = input("Введите имя нового пользователя: ")
   
   
   if any(user['username'] == username for user in users):
       
       print(f"Пользователь с именем {username} уже существует.")
       return
   
   password = input("Введите пароль нового пользователя: ")
   
   new_user = {
       'username' : username,
        
       'password' : password,
       'role' : 'user',
       'history' : [],
       'basket' : []
   }
   
   users.append(new_user) 
   
   
   log_user_action(username, action="добавлен") 
   
   
   print(f"Пользователь {username} добавлен.")


def log_user_action(username, action):
   with open('user_actions_log.txt', mode='a') as log_file:
       log_file.write(f"Пользователь '{username}' был {action}\n")

def remove_user():
   username = input("Введите имя пользователя для удаления:")
   
   global users 
   
   
   users_to_remove = [user for user in users if user['username'] != username]
   
   if len(users) != len(users_to_remove):
      users.remove(next(user for user in users if user["username"]==username))
      log_user_action(username, action="удален") 
      
      print(f"Пользователь {username} удален.")
      
   else:
      
      print(f"Пользователь с именем '{username}' не найден.") 

def main():
   while True:
       user = authorize()
       
       if user:
           if user['role'] == 'admin':
               admin_menu(user)
           else:
               user_menu(user)

if __name__ == "__main__":
   main()
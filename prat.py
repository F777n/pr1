import json

# Данные пользователей и товаров
users = [
    {'username': 'Петя', 'password': '1234', 'role': 'user', 'history': []},
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
    {'name': 'Ёд', 'price': 100, 'quantity': 50, 'rating': 4.9, 'category': "другие"},
    {'name': 'Пластырь', 'price': 500, 'quantity': 100, 'rating': 4.2, 'category': "другие"},
    {'name':'АЦЦ', "price":800,"quantity":6,"rating":4.4,"category":"обезболивающее"},
    {'name':'Снуп', "price":1000,"quantity":7,"rating":4.6,"category":"противопростудное"},
    # Новые таблетки от горла
    {'name':'Таблетки от горла','price':200,'quantity':30,'rating':4.0,'category':'таблетки от горла'},
    {'name':'Леденцы для горла','price':150,'quantity':50,'rating':3.5,'category':'таблетки от горла'}
]

# Функция для авторизации
def authorize():
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль.")
    return None

# Функции для пользователя
def user_menu(user):
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть товары")
        print("2. Купить товар")
        print("3. Посмотреть историю покупок")
        print("4. Сортировать товары по цене")
        print("5. Фильтровать товары по количеству")
        print("6. Поиск товара по названию")
        print("7. Посмотреть категории лекарств")
        print("8. Посмотреть лекарства по рейтингу") 
        print("9. Выйти")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            view_products()
        elif choice == "2":
            buy_product(user)
        elif choice == "3":
            view_history(user)
        elif choice == "4":
            sort_products_by_price()
        elif choice == "5":
            filter_products_by_quantity()
        elif choice == "6":
            search_product()
        elif choice == "7":
            view_categories()
        elif choice == "8":
            view_products_by_rating() 
        elif choice == "9":
            break
        else:
           print("Неверный выбор.")
        def  view_products_by_rating():
            sorted_product = sorted(medicines, key=lambda x: x['rating'], reverse=True)
            print("\nЛекарства отсортированы по рейтингу:")
            for product in sorted_product:
                print((f"{product['name']} - {product['price']} руб. (в наличии: {product['quantity']}, категория: {product['category']}, рейтинг: {product['rating']})"))  


        def view_categories():
            categories = set(product['category'] for product in medicines)
            print("\nДоступные категории лекарств:")
            for category in categories:
                print(f"- {category}")


        def view_products():
            print("\nДоступные товары:")
            for product in medicines:
                    print (f"{product['name']} - {product['price']} руб. (в наличии: {product['quantity']}, категория: {product['category']}, рейтинг: {product['rating']})")


        def buy_product():
            product_name = input("Введите название товара для покупки:")
            for roducts in medicines:
                for product in medicines:
                    if product['name'] == product_name and product['quantity'] > 0:
                            product ['quantity'] -= 1
                            user['history'].append(product_name)
                            print(f"\nВы купили {product_name}.")
                            return
                    print("Товар недоступен.")

        def view_history(user):
            print("\nВаша история покупок:")
            if not user['history']:
                print("История покупок пуста.")
            else:
                for item in user ['history']:
                    print(item)

        def sort_products_by_price():
            sorted_products = sorted(medicines, key =lambda x: x['price'])
            print("\nТовары отсортированы по цене:")
            for product in sorted_products:
              print(f"{product['name']} - {product['price']} руб.(в наличии: {product['quantity']}, категория: {product['category']}, рейтинг:{product['rating']})")

        def filter_products_by_quantity():
            threshold = int(input("Введите минимальное число товара для фильтрации:"))
            filter_products = [product for product in medicines if product['quantity'] >= threshold]
            if filter_products:
                print("\nТовары с количеством больше или равным", threshold)
                for product in filter_products: 
                     print(f"{product['name']} - {product['price']} руб.(в наличии: {product['quantity']}, категория: {product['category']}, рейтинг:{product['rating']})")
            else:
                print("Нет товаров, соответсвующих критерям фильтрации.")

        def search_product():
                
            search_term = input("Введите название товара для поиска:").lower()
            found_products = [product for product in medicines if search_term in product ['name'].lower()]
            if found_products:
                print("\nНайденные товары")
                for product in found_products:
                    print(f"{product['name']} - {product['price']} руб.(в наличии: {product['quantity']}, категория: {product['category']}, рейтинг:{product['rating']})")
            else:
                print("Товары не найдены.")

        def admin_menu(admin):
            while True:
                print("\nВЫберите действие:")
                print("1. Просмотеть товары")
                print("2. Добавить товар")
                print("3. Уадлить товар")
                print("4. Редактировать товар")
                print("5. Управление пользователями")
                print("6. Выйти")
                choice = input("Ваш выбор:")
            
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
        def add_product():
            name = input("Введите название товара:")
            price = float(input("Введите цену товара:"))
            quntity = int(input("Введите количество товар:"))
            rating = float(input("Введите рейтинг товара(от 3 до 5):"))
            if rating < 3 or rating > 5:
                print("Рейтинг должен быть от 3 до 5.")
                return
            category = input("Введите категорию товара:")
            medicines.append({'name': name, 'price': price, 'quantity': quntity, 'rating': rating, 'category': category})
            print(f"Товар {name} добавлен.")
            
        def remove_product():
                name = input("Введите нахвание товара для удаления:")
                global medicines 
                medicines = [product for product in medicines if product ['name'] != name]
                print(f"Товар {name} удален.")

        def edit_product():

                name = input("Введите название товара для редактирования:")
                for product in medicines:
                    if product['name'] == name:
                        new_price = float(input(f"Введите новую цену для{name}(текущая цена{product['price']}):"))
                        new_quantity = int(input(f"Введите новое количество для {name}(текущее количество:{product['quantity']}):"))
                        new_rating = float(input(f"Введите новое имя для {name}(текущий рейтинг: {product['rating']}:"))
                        if new_rating < 3 or new_rating > 5:
                            print("Рейтинг должен быть от 3 до 5.")
                            return
                        new_category = input(f"Введите новую категорию для{name}(текущая категоря: {product['category']})")
                        product['price'] = new_price
                        product['quantity'] = new_quantity
                        product['rating'] = new_rating
                        product['category'] = new_category
                        print(f"Товар{name} обновлен") 
                        return

                        
                    print(f"Товар с названием {name} не найден.")

        def manage_users(): 
            while True: 
                print("\n Управления пользователями:")
                print("1. Просмореть пользоватлей")
                print("2. Добавить пользователя")
                print("3. Удалить пользователя")
                print("4. Выйти")

                choice = input("Ваш выбор:")
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
        def add_product():
            name = input("Введите название товара:")
            price = float(input("Введите цену товара"))
            quantity = int(input("Введите количество товара"))
            rating = float(input("Введите рейтинг товара(от 3 до 5):"))
            if rating < 3 or rating > 5:
                print("Рейтинг должен быть от 3 до 5.")
                return
            category = input("Введите категорию товара:")
            medicines.append({'name': name, 'price': price, 'quantity': quantity, 'rating': rating, 'category': category})
            print(f"Товар{name} добавлен.")
        def edit_product():
            name = input("Введите название товара для редактирования:")
            for product in medicines:
                if product['name'] == name:
                    new_price = float(input(f"Введите нову цену для {name} (текущая цена: {product['price']}):"))
                    new_quantiy = int(input(f"Введите новое количество для {name} (текущая количество: {product['quantity']}):"))
                    new_rating = float(input(f"Введите новый руйтинг для {name} (текущая рейтинг: {product['rating']}):"))
                    if new_rating < 3 or new_rating > 5:
                        print("Рейтинг должен быть от 3 до 5.")
                        return

                    new_category = input(f"Введите новую категорию для {name} (текущая категория: {product['category']}):")
                    product['price'] = new_price
                    product['quantity'] = new_quantiy
                    product['rating'] = new_rating
                    product['category'] = new_category
                    print(f"Товар {name} обновлен.")
                    return
                print(f"Товар с названием {name} не найден.")

    def manage_users(): 
        while True:
            print("\n Управление пользователями^")
            print("1.Просмотреть пользоватлей")
            print("2.Добавить пользователя")
            print("3.Удалить пользователя")
            print("4. Выйти")
            choice = input("Ваш выбор:")
            if choice == "1":
                view_users()
            elif choice == "2":
                add_user()
            elif choice == "3":
                remove_user()
            elif choice == "4":
                break
            else: 
                print("Нверный выбор")
    
def view_user():
    if not users:
        print("\n Нет зарегестрированных пользователей")
    else:
        for user in users:
            role = user['role']
            username = user['username']
            history_count = len(user['history'])

            print(f"Имя: {username}, Роль: {role}, Истоория покупок:{history_count} записей")
def add_user():
    username = input("Введите имя нового пользователя:")
    if any()



            




            




                
















            




        
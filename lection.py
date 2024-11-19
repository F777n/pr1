# def correct_sorted(text, sorted_elements):
#     print(text)
#     for i in sorted_elements:
#         for key, value in i.items():
#             print(key,value, end=" ")
#         if key == 'available_seats':
#             print()
from functools import reduce 

movies = [{'title': 'Интерстеллар', 'genre': 'Sci-Fi', 'rating': 18.6, 'price': 10.0, 'available_seats': 15},
          {'title': 'Побег из Шоушенка', 'genre': 'Drama', 'rating': 9.3, 'price': 8.0, 'available_seats': 20},
          {'title': 'Начало', 'genre': 'Sci-Fi', 'rating': 8.8, 'price': 12.0, 'available_seats': 10},
          {'title': 'Темный рыцарь', 'genre': 'Action', 'rating': 9.0, 'price': 11.0, 'available_seats': 5},
          {'title': 'Крёстный отец', 'genre': 'Crime', 'rating': 9.2, 'price': 10.5, 'available_seats': 8},
          {'title': 'Список Шиндлера', 'genre': 'Biography', 'rating': 8.9, 'price': 9.5, 'available_seats': 12},
          {'title': 'Форрест Гамп', 'genre': 'Drama', 'rating': 8.8, 'price': 10.0, 'available_seats': 18},
          {'title': 'Зеленая миля', 'genre': 'Drama', 'rating': 8.6, 'price': 10.0, 'available_seats': 7},
          {'title': 'Пятый элемент', 'genre': 'Sci-Fi', 'rating': 7.7, 'price': 9.0, 'available_seats': 20},
          {'title': 'Матрица', 'genre': 'Sci-Fi', 'rating': 8.7, 'price': 10.0, 'available_seats': 11},
          {'title': 'Джокер', 'genre': 'Drama', 'rating': 8.5, 'price': 12.0, 'available_seats': 9}]

# titles = [movie["title"] for movie in movies]
# ratings = [movie["rating"] for movie in movies]

# for title, rating in zip(titles, ratings):
#     print(f"{title}: {rating}")
#     movie_rating = dict(zip(titles, ratings ))
#     print(movie_rating)

#     for title,  genre, seats in zip(
#         [movie["title"] for movie in movies],
#         [movie["genre"] for movie in movies],
#         [movie["available_seats"] for movie in movies]
#     ):
#         print(f"{title} ({genre}) - {seats} мест")
# print(reduce(lambda x, y: x + y["price"], movies, 100)) 
# correct_sorted(text= "Отсортированные фильмы:",
#                sorted_elements=list(filter(lambda movie: movie["rating"] > 9 and  movie ["price"] > 10,
#                                             movies )))


# # correct_sorted(text="Отсортированные фильмы(от меньшего к большему)", 
# #                sorted_elements=sorted(movies, key=lambda movie: movie["rating"]))

# # correct_sorted(text="Отсортированные фильмы(от большего  к меньшему)", 
# #                sorted_elements=sorted(movies, key=lambda movie: movie["rating"], reverse=True))

# !!! map(function, iterable )
# def multiply_by_two(x):
#     return x * 2
# numbers =[1, 2, 3, 4, 5]
# numbers1 = [6, 7, 8, 9, 10]
# print(list(map(lambda x, y: x * y, numbers, numbers1)))
# #print(list(map(multiply_by_two, numbers)))
# print(list(map(lambda x: x*2, numbers)))
# print(list(map(float, numbers)))

# # names = ["петя", "вася", "коля"]
# # print(list(map(str.upper, names)))


# #!! filter (function, iterable) фильтрация  
# numbers =[1, 2, 3, 4, 5]
# print(list(filter(lambda x: x % 2 != 0, numbers)))



# from functools import reduce 

# #!!! reduce(function, iterable)
# numbers =[1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x + y, numbers))

# print(reduce(lambda x, y: x if x > y else y, numbers ))



# names = ["Пет", "Вася", "Коля"]
# ages = [10 ,12 ,13]
# print(list(zip(names, ages)))   

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
    
#     print(fact(5))
# try:
#     a = int(input("Введите число"))
#     result = 2 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Нельзя делить на 0!!")
# except ValueError:
#     print("Введите только число!!")

try:
    a = int(input("Введите число"))
    result = a / 0
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(e)
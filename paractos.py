import random

# Игрок и его инвентарь
player_inventory = []
completed_tasks = set()

# Уровни игры
levels = {
    1: {
        "description": "Вы находитесь в офисном комплексе. Найдите оружие и спасите заложников.",
        "puzzle": "Чтобы открыть дверь в следующий кабинет, вам нужен код.",
        "code": "1234",
        "weapon": "пистолет",
        "enemies": ["охранник"]
    },
    2: {
        "description": "Вы в подземном гараже. Здесь много машин и укрытий.",
        "puzzle": "Найдите ключ от машины, чтобы сбежать.",
        "key": "ключ от машины",
        "enemies": ["террорист"]
    },
    3: {
        "description": "Вы на крыше здания. Вам нужно победить босса террористов.",
        "puzzle": "Используйте гранату, чтобы победить босса.",
        "boss_defeated": False,
        "enemies": ["босс террористов"]
    }
}

def display_level(level):
    print(levels[level]["description"])
    print(levels[level]["puzzle"])
    if 'enemies' in levels[level]:
        print(f"Противники на уровне: {', '.join(levels[level]['enemies'])}")

# Функция для обработки команд
def process_command(command, level):
    global completed_tasks
    
    if command == "взять пистолет" and level == 1:
        player_inventory.append(levels[level]["weapon"])
        print("Вы взяли пистолет.")
    
    elif command == "использовать код" and level == 1:
        user_code = input("Введите код: ")
        if user_code == levels[level]["code"]:
            print("Дверь открыта! Вы переходите на следующий уровень.")
            completed_tasks.add("door_opened")
            return True
        else:
            print("Неправильный код.")
    
    elif command == "взять ключ" and level == 2:
        player_inventory.append(levels[level]["key"])
        print("Вы взяли ключ от машины.")
    
    elif command == "использовать ключ" and level == 2:
        if levels[level]["key"] in player_inventory:
            print("Вы сбежали на машине! Переходите на следующий уровень.")
            completed_tasks.add("car_escape")
            return True
        else:
            print("У вас нет ключа от машины.")
    
    elif command == "использовать гранату" and level == 3:
        if "граната" in player_inventory:
            levels[level]["boss_defeated"] = True
            print("Вы победили босса террористов! Поздравляем!")
            return True
        else:
            print("У вас нет гранаты.")
    
    elif command == "взять гранату" and level == 3:
        player_inventory.append("граната")
        print("Вы взяли гранату.")
    
    elif command.startswith("атаковать") and level in [2, 3]:
        enemy = random.choice(levels[level]["enemies"])
        if enemy in player_inventory:
            print(f"Вы атаковали {enemy} и победили его!")
            levels[level]["enemies"].remove(enemy)
            if not levels[level]["enemies"]:
                print("Все противники побеждены!")
                return True
        else:
            print(f"У вас нет нужного предмета для атаки на {enemy}.")
    
    elif command == "посмотреть инвентарь":
        if player_inventory:
            print(f"Ваш инвентарь: {', '.join(player_inventory)}")
        else:
            print("Ваш инвентарь пуст.")
    
    elif command == "исследовать":
        found_item = random.choice(["граната", None])
        if found_item and found_item not in player_inventory:
            player_inventory.append(found_item)
            print(f"Вы нашли {found_item}!")
        else:
            print("Вы ничего не нашли.")

    else:
        print("Команда не распознана.")

# Основной игровой цикл
def main():
    current_level = 1
    
    while current_level <= len(levels):
        display_level(current_level)
        
        if current_level == 1 and "door_opened" in completed_tasks:
            current_level += 1
            completed_tasks.remove("door_opened")
            continue
        
        if current_level == 2 and "car_escape" in completed_tasks:
            current_level += 1
            completed_tasks.remove("car_escape")
            continue
        
        command = input("Введите команду: ").strip().lower()
        
        if process_command(command, current_level):
            current_level += 1
            
    print("Вы прошли все уровни! Спасибо за игру!")

if __name__ == "__main__":
    main()
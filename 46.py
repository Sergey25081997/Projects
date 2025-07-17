# Задание
"""
Спроектируйте и напишите класс UserService, который при создании принимает путь к json файлу. Имеет метод который прочитает список словарей из джейсона и вернет их в струтуре

list[UserData]

@dataclass
class UserData:
    username: str
    fullname: str
    rating: int (11, 12, 15)
Так же создайте метод, который вернет один Экземпляр UserData по конкретному username из файла И сделайте метод который примет UserData и допишет его в json
"""
# Домашнее задание 17
# Если мы добавляем пользователя и такой username уже есть в json, тогда мы ничего не добавляем и функция добавления возвращает False, если же проблем нет тогда добавляем в json и возвращаем True


from dataclasses import dataclass
import json
from typing import Any


@dataclass
class UserData:  # Класс, описывающий пользователя.
    username: str
    fullname: str
    rating: int


class UserService:  # Класс для работы с пользователями, хранящимися в JSON-файле.
    def __init__(self, path="./files/userdata.json"):
        """
        Инициализация сервиса пользователей.

        Аргументы:
            path (str): Путь к JSON-файлу, где хранятся данные пользователей.
        """
        self.path = path

    def _get_dicts_user_data(self) -> list[dict[str, Any]]:
        """
        Служебный метод: читает JSON-файл и возвращает данные пользователей в виде списка словарей.

        Возвращает:
            list[dict[str, Any]]: Список пользователей в виде словарей.
        """
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_users_data(self) -> list[UserData]:
        """
        Возвращает список всех пользователей из файла в виде объектов UserData.

        Возвращает:
            list[UserData]: Список объектов UserData.
        """
        user_dicts = self._get_dicts_user_data()
        result = []
        for user_data in user_dicts:
            result.append(UserData(**user_data))  # Распаковываем словарь в UserData
        return result

    def get_by_username(self, username: str) -> UserData | None:
        """
        Ищет пользователя по username.

        Аргументы:
            username (str): Имя пользователя, которого нужно найти.

        Возвращает:
            UserData или None: Объект UserData, если найден, иначе None.
        """
        user_dicts = self._get_dicts_user_data()
        for user_dict in user_dicts:
            if user_dict.get("username") == username:
                return UserData(**user_dict)
        return None  # Явно возвращаем None, если пользователь не найден

    def add_user_data(self, user_data: UserData) -> bool:
        """
        Добавляет пользователя в JSON файл, если такого username еще нет.
        
        Аргументы:
            user_data (UserData): Новый пользователь для добавления.

        Возвращает:
            bool: True если пользователь успешно добавлен, 
                  False если пользователь с таким username уже существует
        """
        user_dicts = self._get_dicts_user_data()
        # Проверяем, существует ли уже пользователь с таким username
        for existing_user in user_dicts:
            if existing_user.get("username") == user_data.username:
                return False  # Пользователь уже существует, ничего не добавляем
        user_dicts.append(user_data.__dict__)   # Добавляем нового пользователя
        with open(self.path, "w", encoding="utf-8") as f:   # Записываем обновленные данные обратно в файл
            json.dump(user_dicts, f, ensure_ascii=False, indent=2)
        return True  # Пользоветель успешно добавлен


service = UserService()
print("search", service.get_by_username("sasha2"))  # search None
print(service.get_users_data())
user_data = UserData("sasha2", "Аlexandr", 13)  
service.add_user_data(user_data)  #  [UserData(username='test', fullname='TEST TEST', rating=15), UserData(username='sasha', fullname='Aleksand', rating=12)]


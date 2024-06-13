import random

import pyodbc

from database.bd import cursor

displayed_gift_ids = []


class GiftResponse:
    def __init__(self, total_count, gifts):
        self.TotalCount = total_count
        self.Gifts = gifts


def get_gifts(user_answers):
    recipient = user_answers["Кому хотите подарить подарок?"]
    holiday = user_answers["Какой категории вам необходим подарок?"]

    try:
        # Формирование SQL-запроса
        query = """
            SELECT Наименование, Ссылка, Изображение, ПодаркиId, Цена
            FROM Подарки
            WHERE Жанр LIKE ? OR Получатель LIKE ?
        """

        # Выполнение запроса
        cursor.execute(query, (f"%{holiday}%", f"%{recipient}%"))

        # Получение результатов
        gifts = cursor.fetchall()

        # Фильтрация уникальных подарков
        unique_gifts = [g for g in gifts if g[3] not in displayed_gift_ids]

        if len(unique_gifts) > 3:
            # Выбор 3 случайных подарков
            selected_gifts = random.sample(unique_gifts, 3)
            displayed_gift_ids.extend(g[3] for g in selected_gifts)
            response = GiftResponse(len(unique_gifts), selected_gifts)
        else:
            response = GiftResponse(len(unique_gifts), unique_gifts)

        return response

    except pyodbc.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return GiftResponse(0, [])
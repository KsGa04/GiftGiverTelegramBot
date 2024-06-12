import pyodbc

from database.bd import cursor


def search_gifts(search_term):
    """
    Метод для поиска подарков по названию, получателю или жанру.

    Args:
        search_term (str): Строка для поиска.

    Returns:
        list: Список найденных подарков.
    """
    try:

        # Формирование SQL-запроса
        query = """
            SELECT Наименование, Цена, Ссылка, Изображение, ПодаркиID
            FROM Подарки
            WHERE Наименование LIKE ? 
                OR Получатель LIKE ? 
                OR Жанр LIKE ?
        """

        # Выполнение запроса
        cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

        # Получение результатов
        gifts = cursor.fetchall()

        # Возвращение списка найденных подарков
        return gifts

    except pyodbc.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []
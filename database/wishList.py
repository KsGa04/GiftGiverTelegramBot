import pyodbc
from database.bd import cursor, conn


def get_user_wishlist(user_id):
    try:
        # Выполнение запроса для получения списка желаемого пользователя
        query = """
            SELECT p.Наименование, p.Цена, p.Ссылка, w.ЖелаемоеID, p.Изображение
            FROM Желаемое w
            JOIN Подарки p ON w.ПодаркиID = p.ПодаркиID
            WHERE w.ПользовательID = ?
        """
        cursor.execute(query, (user_id,))

        # Получение результатов запроса
        wishlist = cursor.fetchall()

        # Возвращение списка желаемого
        return wishlist

    except pyodbc.Error as e:
        print(f"Ошибка при получении списка желаемого: {e}")
        return None


def delete_from_wishlist(user_id, item_id):
    try:
        # Выполнение запроса для удаления подарка из списка желаемого
        query = "DELETE FROM Желаемое WHERE ПользовательID = ? AND ЖелаемоеID = ?"
        cursor.execute(query, (user_id, item_id))
        conn.commit()
        return True
    except pyodbc.Error as e:
        print(f"Ошибка при удалении подарка из списка желаемого: {e}")
        return False

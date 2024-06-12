import pyodbc
from database.bd import cursor, CurrentUser


def authenticate_user(username, password):
    """
    Функция для аутентификации пользователя.

    Args:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.

    Returns:
        bool: True, если пользователь успешно аутентифицирован, False в противном случае.
    """
    try:
        cursor.execute("SELECT * FROM Пользователь WHERE Логин = ? AND Пароль = ?", (username, password))
        user = cursor.fetchone()
        user_id = user[0]
        CurrentUser.CurrentId = user_id
        # Проверка, найден ли пользователь
        return user is not None

    except pyodbc.Error as e:
        return False

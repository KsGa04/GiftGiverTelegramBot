import pyodbc

# Строка подключения
conn_str = (
    r'Driver={SQL Server};'
    r'Server=DESKTOP-4GCEH3I;'
    r'Database=giftgiver;'
)

# Создание соединения
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


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
        # Проверка, найден ли пользователь
        return user is not None

    except pyodbc.Error as e:
        return False


def register_user(login, password, fio, email):
    try:
        # Проверяем, есть ли уже пользователь с таким логином
        cursor.execute("SELECT COUNT(*) FROM Пользователь WHERE Логин = ?", login)
        count = cursor.fetchone()[0]
        if count > 0:
            return "Пользователь с таким логином уже существует."

        # Вставляем нового пользователя в базу данных
        cursor.execute(
            "INSERT INTO users (Логин, Пароль, ФИО, Email, РолиId) VALUES (?, ?, ?, ?, ?)",
            (login, password, fio, email, 1)
        )
        conn.commit()
        return "Регистрация прошла успешно."
    except pyodbc.Error as e:
        conn.rollback()
        return f"Ошибка при регистрации: {e}"

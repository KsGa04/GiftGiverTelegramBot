import pyodbc

from database.bd import cursor, conn


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

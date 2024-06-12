import pyodbc


class CurrentUser:
    CurrentId: int = 0


# Строка подключения
conn_str = (
    r'Driver={SQL Server};'
    r'Server=DESKTOP-4GCEH3I;'
    r'Database=giftgiver;'
)

# Создание соединения
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('courses.db')
cursor = conn.cursor()

# Обновляем структуру таблицы courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description_short TEXT NOT NULL,
        description TEXT NOT NULL,
        image TEXT NOT NULL
    )
''')

# Заполняем данными
courses_data = [
    ("Фитнес для начинающих", 2999.00, "Основной курс для новичков.", "Этот курс включает базовые упражнения, предназначенные для новичков в фитнесе. Включены советы по технике и питанию.", "1.jpg"),
    ("Продвинутый фитнес", 4999.00, "Углубленный курс для развития силы и выносливости.", "Для тех, кто уже имеет опыт. Курс содержит сложные упражнения, тренировки на выносливость и рекомендации по оптимизации прогресса.", "2.jpg"),
    ("Силовая тренировка", 3999.00, "Силовые тренировки для наращивания мышц.", "Курс включает упражнения для укрепления мышц, повышения тонуса и наращивания массы с правильной техникой.", "3.jpg")
]

cursor.executemany("INSERT INTO courses (name, price, description_short, description, image) VALUES (?, ?, ?, ?, ?)", courses_data)

# Сохраняем изменения
conn.commit()
conn.close()

print("База данных обновлена и заполнена.")

import sqlite3
import os


def init_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schedule(
    id_group INTEGER PRIMARY KEY,
    auditorium TEXT,
    beginLesson TEXT,
    endLesson TEXT,
    building TEXT,
    date TEXT,
    dayOfWeek INTEGER,
    dayOfWeekString TEXT,
    discipline TEXT,
    kindOfWork TEXT,
    lecturer TEXT,
    lecturer_title TEXT,
    subGroup TEXT
    )
    ''')
    connection.commit()
    connection.close()


def database(data, db_name, group_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for item in data:
        cursor.execute('''
                INSERT INTO Schedule (
                    id_group, auditorium, beginLesson, endLesson, building,
                    date, dayOfWeek, dayOfWeekString, discipline, kindOfWork, 
                    lecturer, lecturer_title, subGroup
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (
                           group_id, item.get('auditorium'), item.get('beginLesson'),
                           item.get('endLesson'), item.get('building'), item.get('date'),
                           item.get('dayOfWeek'), item.get('dayOfWeekString'), item.get('discipline'),
                           item.get('kindOfWork'), item.get('lecturer'), item.get('lecturer_title'),
                           item.get('subGroup')
                       )
                       )
    conn.commit()
    conn.close()


def delete_database(db_name):
    if os.path.exists(db_name):
        try:
            os.remove(db_name)
            print(f"'{db_name}' успешно удалена.")
            return True
        except Exception as e:
            print(f'Ошибка при удалении базы данных: {e}')
            return False
    else:
        print(f"Файл '{db_name}' не найден.")
        return False

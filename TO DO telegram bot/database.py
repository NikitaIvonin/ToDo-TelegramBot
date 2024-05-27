import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user='postgres'
# пароль, который указали при установке PostgreSQL
password=''

def create_database():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_database = 'create database todo_database'
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def connect_database():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def create_table():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        # Создайте курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE TODO
                            (TASKS   TEXT            ); '''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def insert_table(task):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        cursor = connection.cursor()
        # Выполнение SQL-запроса для вставки данных в таблицу
        insert_query = (""" INSERT INTO TODO (TASKS) VALUES ( '%s' )""" % (task))
        cursor.execute(insert_query)
        connection.commit()
        print("1 запись успешно вставлена")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")



def check_table():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        cursor = connection.cursor()

        # Получить количество строк
        cursor.execute("SELECT COUNT(tasks) from TODO")
        nums = cursor.fetchall()
        nums = nums[0][-1]
        # Получить результат
        cursor.execute("SELECT * from TODO")
        record = cursor.fetchall()
        n = []
        for i in range(nums):
            n.append(record[i][-1])
        return n

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")



def delete_task(tasks):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        cursor = connection.cursor()

        # Удалить задачу
        cursor.execute("DELETE FROM TODO WHERE tasks='%s'"% tasks)
        connection.commit()


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")



def delete_all():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=user,
                                    password=password,
                                    host="127.0.0.1",
                                    port="5432",
                                    database="todo_database")

        cursor = connection.cursor()

        # Удалить задачу
        cursor.execute("TRUNCATE TODO")
        connection.commit()


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


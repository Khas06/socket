import psycopg2

cars = [(1, 'Audi', 52642),
        (2, 'Mercedes', 57127),
        (3, 'Skoda', 9000),
        (4, 'Volvo', 29000),
        (5, 'Bentley', 350000),
        ]

try:
    with psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='1234',
            database='cars_db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
        car_id serial PRIMARY KEY,
        model TEXT,
        price INTEGER
        )''')
        cursor.executemany('''INSERT INTO cars VALUES(%s, %s, %s)''', cars)

        # for car in cars:
        #     cursor.execute('''INSERT INTO cars VALUES(%s, %s, %s)''', car)

    # cursor.commit()
    # cursor.close()


except Exception as ex:
    print(ex)
    cursor.close()

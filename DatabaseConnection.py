from mysql.connector import connect, Error


def add_data(temp, month, day, hour, minute):
    data = (temp, month, day, hour, minute)

    # connects to local database
    try:
        with connect(
                    host="localhost",
                    user="root",
                    password="Toxicity01!!",
                    database="weather"
        ) as connection:
            # creates query to insert data into database
            add_query = ("INSERT INTO temperature_tracker "
                         "(temp, month, day, hour, minute) "
                         "VALUES (%s, %s, %s, %s, %s)")
            with connection.cursor() as cursor:
                # commits new data to database
                cursor.execute(add_query, data)
                connection.commit()
    except Error as e:
        print(e)

import psycopg2
import configparser
import datetime


def insert_exercise(exercise, duration, instrument):
    """ log your finished exercise to the database """
    today = datetime.date.today()

    sql = """INSERT INTO music_practice (date,exercise,duration, instrument)
VALUES ( %s, %s, %s , %s) RETURNING exercise;"""
    connection = None
    record = None
    try:
        # read database configuration
        config = configparser.ConfigParser()

        config.read('config.ini')

        # Create a connection credentials to the PostgreSQL database

        connection = psycopg2.connect(
            config['DEFAULT']['uri']
        )

        cur = connection.cursor()
        # execute the INSERT statement
        cur.execute(sql, (today, exercise, '%s minutes' %
                          duration, instrument,))
        # get the generated id back
        record = cur.fetchone()[0]
        # commit the changes to the database
        connection.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('     Logged to database')

    return record


# insert_exercise('something', 40)

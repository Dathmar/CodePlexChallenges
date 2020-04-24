import sqlite3
from random import randint


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)

        return c
    except Error as e:
        print(e)


def create_question_table_if_needed(conn):
    sql = 'CREATE TABLE if not exists questions (question TEXT, resonse TEXT)'
    execute_sql(conn, sql)
    conn.commit()


if __name__ == '__main__':
    db_file = 'questions.db'
    conn = create_connection(db_file)
    create_question_table_if_needed(conn)

    question = input('What is your question?\n')

    print(question)

    sql = 'Select * FROM questions where question = "{0}"'.format(question)
    c = execute_sql(conn, sql)
    previous_answers = c.fetchone()

    if not isinstance(previous_answers, type(None)):
        print(previous_answers[1])
    else:
        answer = str(randint(0,1))
        answer = 'yes' if answer == '1' else 'no'

        print(answer)

        sql = 'insert into questions values ("{0}", "{1}")'.format(question, answer)
        execute_sql(conn, sql)
        conn.commit()
"""
    sql = 'insert into questions VALUES ("1","yes")'
    c = execute_sql(conn, sql)
    conn.commit()
"""




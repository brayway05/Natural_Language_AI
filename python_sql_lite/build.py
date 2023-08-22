import os

from db import create_table, create_connection
from schema import *


def select_all_from_menu(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_menu(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
        INSERT INTO menu VALUES
        (1, 'Green Tea', '1', 50),
        (2, 'Thai Tea', '1', 50),
        (3, 'Jasmine Tea', '1', 50),
        (4, 'Espresso', '2',55),
        (5, 'Cappucino', '2',55),
        (6, 'Latte', '2',55),
        (7, 'Mocha', '2',55),
        (8, 'Passion Fruit', '3',60),
        (9, 'Mango Juice', '3',60),
        (10,'Orange Juice', '3',60);
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_categories(conn):

    sql = """
        INSERT INTO categories VALUES
	    (1, 'tea'),
        (2, 'coffee'),
        (3, 'juice');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_customers(conn):

    sql = """
        INSERT INTO customers VALUES
	    (1, 'Mark', 'Lee','Bangkok'),
        (2, 'Johnny', 'Suh', 'Phuket'),
        (3, 'Jennie', 'Kim', 'Chiangmai'),
        (4, 'Jeno', 'Lee', 'Bangkok'),
        (5, 'Karina', 'Yoo', 'Chiangmai');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_employees(conn):
    sql = """
         INSERT INTO employee VALUES
	        (1, 'Nicolene', 'Jones','2020-09-01','Bangkok'),
            (2, 'Anna', 'Smith', '2021-12-01', 'Phuket'),
            (3, 'Jessica', 'Brown', '2020-08-01', 'Chiangmai');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_orders(conn):

    sql = """
        INSERT INTO Orders VALUES
	    (1, '2022-08-01',1,1,4,'Grabfood',1),
        (2, '2022-08-01',6,2,1,'Lineman',1),
	    (3, '2022-08-02',2,2,2,'Robinhood',2),
	    (4, '2022-08-03',3,1,5,'Grabfood',3),
	    (5, '2022-08-04',1,1,2,'Robinhood',2),
	    (6, '2022-08-05',6,1,4,'Grabfood',1),
	    (7, '2022-08-05',10,1,3,'Grabfood',3),
	    (8, '2022-08-09',3,2,4,'Grabfood',1),
	    (9, '2022-08-13',5,3,1,'Lineman',1),
	    (10, '2022-08-13',6,1,2,'Robinhood',2),
	    (11, '2022-08-13',7,1,5,'Lineman',3),
	    (12, '2022-08-14',4,1,5,'Grabfood',3),
	    (13, '2022-08-15',5,2,3,'Grabfood',3),
	    (14, '2022-08-15',10,1,2,'Robinhood',2),
	    (15, '2022-08-18',5,2,1,'Lineman',1),
	    (16, '2022-08-20',6,1,2,'Robinhood',2),
	    (17, '2022-08-21',4,2,1,'Lineman',1),
	    (18, '2022-08-25',5,1,5,'Grabfood',3),
	    (19, '2022-08-26',5,3,3,'Grabfood',3),
	    (20, '2022-08-29',6,2,4,'Grabfood',1);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_category_table)
    insert_to_categories(conn)
    create_table(conn, sql_create_menu_table)
    insert_to_menu(conn)
    create_table(conn, sql_create_customers_table)
    insert_to_customers(conn)
    create_table(conn, sql_create_employee_table)
    insert_to_employees(conn)
    create_table(conn, sql_create_orders_table)
    insert_to_orders(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()



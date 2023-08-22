sql_create_category_table = """
    CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name TEXT
    );
"""

sql_create_menu_table = """
    CREATE TABLE menu (
        menu_id INT PRIMARY KEY ,
        menu_name TEXT,
        category_id INT,
        unit_price REAL,
        FOREIGN KEY (category_id) references categories(category_id)
    );
"""

sql_create_customers_table = """
    CREATE TABLE customers (
    customer_id INT PRIMARY KEY ,
    firstname TEXT,
    Lastname TEXT,
    city TEXT
);
"""

sql_create_employee_table = """
    CREATE TABLE employee (
        emp_id INT PRIMARY KEY ,
        firstname TEXT,
        Lastname TEXT,
        hiredate TEXT,
        branch TEXT );
"""

sql_create_orders_table = """
    CREATE TABLE Orders(
        orderid INT,
        orderdate TEXT,
        menu_id INT,
        quantity INT DEFAULT 0,
        customer_id INT,
        delivery_platform TEXT,
        emp_id INT,
        FOREIGN KEY (menu_id) references menu(menu_id)
        FOREIGN KEY (customer_id) references customers(customer_id)
        FOREIGN KEY (emp_id) references employee(emp_id)
    );
"""

def get_schema():
    schema = f"{sql_create_category_table}{sql_create_menu_table}{sql_create_customers_table}{sql_create_employee_table}{sql_create_orders_table}"
    return schema

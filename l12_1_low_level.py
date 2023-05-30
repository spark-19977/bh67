import psycopg2

conn = psycopg2.connect(database='belhard',
                        user='belhard',
                        password='belhard',
                        host='localhost',
                        port=5432)

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS shop(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        address VARCHAR(128) UNIQUE NOT NULL
        )
        ''')

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS category(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(64) UNIQUE NOT NULL,
        slug VARCHAR(64) UNIQUE NOT NULL,
        parent_id INT NULL,
        FOREIGN KEY (parent_id) REFERENCES category (id)
        )
        ''')

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS product(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(64) UNIQUE NOT NULL,
        description VARCHAR(256),
        slug VARCHAR(64) UNIQUE NOT NULL,
        category_id INT NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        image VARCHAR(64),
        FOREIGN KEY (category_id) REFERENCES category (id)
        )
        ''')

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS shopproduct(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        product_id INT NOT NULL,
        shop_id INT NOT NULL,
        count INT,
        UNIQUE (product_id, shop_id),
        FOREIGN KEY (product_id) REFERENCES product (id),
        FOREIGN KEY (shop_id) REFERENCES shop (id)
        )
        ''')

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS role(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(64) UNIQUE NOT NULL
        )
        ''')

with conn:
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS customer(
        id SERIAL PRIMARY KEY UNIQUE NOT NULL,
        username VARCHAR(64) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE,
        role_id INT NOT NULL,
        referrer_id INT,
        points INT DEFAULT(0),
        FOREIGN KEY (role_id) REFERENCES role (id),
        FOREIGN KEY (referrer_id) REFERENCES customer (id)
        )
        ''')

conn.close()

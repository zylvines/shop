import psycopg2


connection = psycopg2.connect(
    database='nt',
    user='postgres',
    password=1,
    host='localhost',
    port=5432
)

cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS person(
    id serial primary key,
    full_name varchar(100),
    age int check(age > 0)
);
""")

cursor.execute('''
insert into person(full_name,age)
values('John Doe',25),
('Ali Aliyev',30);

''')

#
# def create_table():
#     pass
#
#
# create_table()
# cursor.execute('''select * from person;''')
#
# for user in cursor.fetchall():
#     print(user)
#
# cursor.execute('''select * from person where id = 2;''')
# print(cursor.fetchone())
#
# connection.commit()
# cursor.close()
# connection.close()
#
# print('Table created successfully!')
#

full_name = input("full_name kiriting:")
age = input("age kiriting:")

connection = None
cursor = None
try:
    connection = psycopg2.connect(
        database='shop',
        user='postgres',
        password=123,
        host='localhost',
        port=5432
    )
    cursor = connection.cursor()

except psycopg2.DatabaseError as e:
    print(e)

else:
    cursor.execute('''insert into person(full_name,age)
    values ('asd',25);
    ''')
    connection.commit()
    print(cursor.fetchall())

finally:
    if full_name:
        print(f"sizning full_name ingiz {full_name}")
    elif age:
        print(f"sizning age ingiz {age}")
    if connection:
        cursor.close()
        connection.close()

import sqlite3

conn = sqlite3.connect('for login.db')
cursor = conn.cursor()
def work_db(log, pas):

    [log] = cursor.execute("SELECT * FROM Login WHERE Username = ? AND Password = ? ",(log, pas))
    return log
def create_new_db(log,pas):
    cursor.execute("INSERT INTO Login VALUES (?,?,?)", (log, pas,'false'))
    conn.commit()
def all_users():

    for row in cursor.execute("SELECT  * FROM Login"):
        print(row)
def menu():
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    for row in cur.execute("SELECT  * FROM All_food WHERE Fromm = 'Pizza'"):
        print(row)
def pizza_name():
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    pizza_nam = []
    for name in cur.execute("SELECT Name FROM All_food WHERE Fromm = 'Pizza'"):
        pizza_nam.append(name)
    return pizza_nam
def drinks_name():
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    drink_nam = []
    for name in cur.execute("SELECT Name FROM All_food WHERE Fromm = 'Drinks'"):
        drink_nam.append(name)
    return drink_nam
def desserts_name():
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    dess_nam = []
    for name in cur.execute("SELECT Name FROM All_food WHERE Fromm = 'Dessert'"):
        dess_nam.append(name)
    return dess_nam

def sides_name():
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    side_nam = []
    for name in cur.execute("SELECT Name FROM All_food WHERE Fromm = 'Sides'"):
        side_nam.append(name)
    return side_nam
def for_picture(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    [name_for_pict] = cur.execute("""SELECT Pic
                                    FROM All_food
                                    WHERE Name = (?)""", (name,))
    [pict] = cur.execute("""SELECT Fromm
                                FROM All_food
                                    WHERE Name = (?)""", (name,))
    return name_for_pict
def for_picture_dis(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    [pict] = cur.execute("""SELECT Fromm
                                    FROM All_food
                                        WHERE Name = (?)""", (name,))
    return pict
def for_ingedients(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    [ing] = cur.execute('''SELECT Ing FROM All_food WHERE Name = (?)''',(name,))
    return ing
def for_price(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    [price] = cur.execute('''SELECT Price From All_food Where Name = (?)''',(name,))
    return price
def remove_from_sum(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    [remove] = cur.execute("SELECT Price From All_food WHERE Name = (?)", (name,))
    return remove
def for_e_mail(name):
    connect = sqlite3.connect('menu.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO E_mail VALUES (?)", (name,))
    connect.commit()

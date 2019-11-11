import sqlite3


def main():
    while True:
        select_menu = input('メニューは?(登録: r ､閲覧: s ､削除: d ､終了: q ) > ')
        # select_menu = 'd'

        if select_menu == 'r':
            name = input('名前は? > ')
            weight = input('体重は? > ')
            register_user(name, weight)

        elif select_menu == 's':
            users = find_all_users()

            for user in users:
                print(f'name: {user[0]}, weight: {user[1]}')

        elif select_menu == 'd':
            users = find_all_users()

            for user in users:
                print(f'name: {user[0]}, weight: {user[1]}')

            delete_name = input('削除したい名前は? > ')

            delete_user(delete_name)

        elif select_menu == 'q':
            break


        else:
            print('正しい値を入力して下さい')


def register_user(name, weight):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"INSERT INTO users (name,weight) VALUES(?,?)"
    cursor.execute(sql, (name, weight))
    connection.commit()
    connection.close()


def find_all_users():
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()
    connection.close()
    return users


def delete_user(delete_name):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users  WHERE name = ?"
    cursor.execute(sql, (delete_name,))
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()

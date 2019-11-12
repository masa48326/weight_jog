import sqlite3


def main():
    while True:
        select_menu = input('メニューは?\n(登録: r ､閲覧: s ､削除: d ､更新: u ､終了: q ) > ')
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

        elif select_menu == 'u':
            users = find_all_users()

            for user in users:
                print(f'name: {user[0]}, weight: {user[1]}')

            update_name = input('更新したい名前は? > ')
            update_weight = input('更新後の体重は? > ')

            update_user(update_name, update_weight)

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


def update_user(update_name, update_weight):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"UPDATE users SET weight ='{update_weight}' WHERE name = '{update_name}'"
    cursor.execute(sql)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()

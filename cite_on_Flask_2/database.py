import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

def init_db():
	conn = psycopg2.connect(
		user=user,
		password=password,
		host=host,
		port=port
	)

	cur = conn.cursor()

	try:
		cur.execute('''
			CREATE TABLE IF NOT EXISTS users (
				id SERIAL PRIMARY KEY,
				nickname VARCHAR(15) UNIQUE NOT NULL CHECK (username !~ '[[:punct:]]'),
				password VARCHAR(32) NOT NULL
			);
			''')

		conn.commit()

		cur.close()
		conn.close()
		print('База инициализирована!')
	except Exception as e:
		print(e)
		cur.close()
		conn.close()


def add_user(nickname: str, password: str) -> str:
	conn = psycopg2.connect(
		user=user,
		password=password,
		host=host,
		port=port
	)

	cur = conn.cursor()

	try:
		cur.execute("SELECT * from users")
		print("Результат", cur.fetchall())

		cur.execute('INSERT INTO users (nickname, password) VALUES (%s, %s)', (nickname, password))
		conn.commit()

		cur.execute("SELECT * from users")
		print("Результат", cur.fetchall())

		cur.close()
		conn.close()
		return f'Успешно создан аккаунт с ником {nickname}!'
	except Exception as e:
		cur.close()
		conn.close()
		return f'{e}'


def get_users() -> list:
	conn = psycopg2.connect(
		user=user,
		password=password,
		host=host,
		port=port
	)

	cur = conn.cursor()

	try:
		cur.execute('SELECT * from users')

		conn.commit()
		table = cur.fetchall()

		cur.close()
		conn.close()
		return table
	except Exception as e:
		cur.close()
		conn.close()
		return [e]


def update_user(new_nickname: str, new_password: str, number_of_choice: int) -> str:
	conn = psycopg2.connect(
		user=user,
		password=password,
		host=host,
		port=port
	)

	cur = conn.cursor()

	try:
		cur.execute("SELECT * from users")
		table = cur.fetchall()

		if number_of_choice == 1:
			cur.execute(f'Update users set password = %s where nickname = %s', (new_password, old_nickname))
			return 'Пароль изменён!'
		elif number_of_choice == 2:
			cur.execute(f'Update users set nickname = %s where nickname = %s',
						(new_nickname, old_nickname))
			cur.close()
			conn.close()
			return 'Никнейм изменён!'
		elif number_of_choice == 3:
			cur.execute("UPDATE users SET nickname = %s, password = %s WHERE nickname = %s, password = %s",
						(new_nickname, new_password, old_nickname, old_password))

			conn.commit()

			cur.execute("SELECT * from users")
			print("Результат", cur.fetchall())

			cur.close()
			conn.close()
			return 'Никнейм и пароль изменён!'
	except Exception as e:
		cur.close()
		conn.close()
		return f"{e}"


init_db()
# print(get_users())
# print(add_user('Rickk', 'password'))
print(update_user())

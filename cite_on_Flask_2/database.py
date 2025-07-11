import psycopg2


def init_db():
	conn = psycopg2.connect(
		user="postgres",
		password="1111",
		host="127.0.0.1",
		port="5432"
	)

	cur = conn.cursor()

	cur.execute('''
		CREATE TABLE IF NOT EXISTS users (
			id SERIAL PRIMARY KEY,
			nickname VARCHAR(15) NOT NULL,
			password VARCHAR(32) NOT NULL
		);
		''')

	conn.commit()

	cur.close()
	conn.close()


init_db()

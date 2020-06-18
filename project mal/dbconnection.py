import psycopg2

conn = psycopg2.connect(
    'host=192.168.99.100 port=5432 dbname=postgres user=postgres password=DefaultPassword')
cur = conn.cursor()

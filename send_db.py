import sqlite3
import pymysql

# 1. SQLite 데이터베이스 연결 및 데이터 읽기
sqlite_conn = sqlite3.connect('my_database.db')
sqlite_cursor = sqlite_conn.cursor()

# SQLite 테이블에서 name과 age 데이터를 가져오기
sqlite_cursor.execute("SELECT name, age FROM my_table")
sqlite_data = sqlite_cursor.fetchall()

# SQLite 연결 닫기
sqlite_conn.close()

# 2. MySQL 데이터베이스에 연결하고 SQLite 데이터를 전송
mysql_conn = pymysql.connect(
    host='114.200.119.90',  # MySQL 서버 IP
    user='ras_aoddudwo',    # MySQL 사용자
    password='msh0314',     # MySQL 비밀번호
    database='test_db'      # 데이터베이스 이름
)

try:
    with mysql_conn.cursor() as mysql_cursor:
        # SQLite에서 가져온 데이터를 MySQL로 삽입
        for row in sqlite_data:
            sql = "INSERT INTO your_table (name, age) VALUES (%s, %s)"
            mysql_cursor.execute(sql, row)

    # 변경 사항 저장
    mysql_conn.commit()

finally:
    # MySQL 연결 닫기
    mysql_conn.close()

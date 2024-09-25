import pymysql

# MySQL에 연결
connection = pymysql.connect(
    host='114.200.119.90',  # MySQL 서버가 설치된 PC의 IP 주소
    user='ras_aoddudwo',           # MySQL 사용자
    password='msh0314',   # MySQL 비밀번호
    database='test_db'  # 사용할 데이터베이스 이름
)

try:
    with connection.cursor() as cursor:
        # SQL 쿼리 작성
        sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
        cursor.execute(sql, ('data1', 'data2'))
    
    # 변경 사항 커밋
    connection.commit()

finally:
    connection.close()


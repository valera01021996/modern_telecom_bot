from database.utils import connect_to_database


connection, cursor = connect_to_database()
def insert_to_table(ip_address, pool_id=2):
    cursor.execute("""INSERT INTO ips (ip_address, pool_id)
        VALUES(
            %s, %s
        )
        ON DUPLICATE KEY UPDATE
            pool_id = VALUES(pool_id)
    """, (ip_address, pool_id))

for i in range(255):
    ip_address = f"109.207.241.{i}"
    insert_to_table(ip_address)
    connection.commit()
    print(f"Добавлен {ip_address} в таблицу.")
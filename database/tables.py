from database.utils import connect_to_database


class InitDB:
    def __init__(self):
        self.connection, self.cursor = connect_to_database()

    def __create_pools_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pools(
            id INT AUTO_INCREMENT PRIMARY KEY,
            network VARCHAR(255) NOT NULL
        )""")

    def __create_ips_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ips(
            id INT AUTO_INCREMENT PRIMARY KEY,
            pool_id INT,
            ip_address VARCHAR(45) UNIQUE,
            is_allocated BOOLEAN DEFAULT FALSE,
            FOREIGN KEY(pool_id) REFERENCES pools(id)
        )""")

    def init(self):
        self.__create_pools_table()
        self.__create_ips_table()


if __name__ == "__main__":
    InitDB().init()

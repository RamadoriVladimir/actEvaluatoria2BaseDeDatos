import mysql.connector

class ClienteManager:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def add_cliente(self, nombre, email):
        query = "INSERT INTO clientes (nombre, email) VALUES (%s, %s)"
        self.cursor.execute(query, (nombre, email))
        self.conn.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(f'ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}')

    def close(self):
        self.cursor.close()
        self.conn.close()

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'clientes_db'
}

manager = ClienteManager(db_config)
manager.add_cliente('Juan Perez', 'juanperez@gmail.com')
manager.listar_clientes()
manager.close()

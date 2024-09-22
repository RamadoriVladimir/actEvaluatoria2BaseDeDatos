from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///clientes.db')
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_cliente = Cliente(nombre="Juan Perez", email="juanperez@gmail.com")
session.add(nuevo_cliente)
session.commit()

clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'ID: {cliente.id}, Nombre: {cliente.nombre}, Email: {cliente.email}')

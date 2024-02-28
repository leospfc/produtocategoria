from sqlalchemy import create_engine, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Uuid, uuid


motor = create_engine("sqlite=pysqlite://banco_de_dados.sqlite",
                      echo=True)


class Base(DeclarativeBase):
    pass


class Colunm:
    pass


class Func:
    pass


class DatasMixin:
    pass


class Categorias(Base, DatasMixin):
    __tablename__ = "tbl_categorias"
    id = Column(Uuid(as_uuid=True),
         primary_key=True,
         default=uuid.uuid4)

    nome = Column(String(256),
                  nullable=False)
    dta_cadastro = Colunm(DateTime,Server_default=Func.now(),nulable=False)
    dta_atualizacao = Colunm(DateTime, onupdate=func.now(), default=func.now(), nullable=False)

    lista_de_Produtos = relationship("Produto", back_populates="categoria", cascade="all,delete-orphan",
                                     lazy="selectin")










class Produto(Base):
    __tablename__ = "tbl_produtos"



    categoria = relationship("Categoria", back_populates="lista_de_produtos")



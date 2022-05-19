# TRECHO NESSESÁRIO PARA CRIAR O BANCO DE DADOS #
from sqlalchemy import create_engine, Column, Integer, String   
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         binds=engine))

Base = declarative_base()
Base.query = db_session.query_property()
# TRECHO NESSESÁRIO PARA CRIAR O BANCO DE DADOS #

#Criar a tabales #
class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index= True)
    idade = Column(Integer)
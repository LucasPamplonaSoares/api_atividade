# TRECHO NESSESÁRIO PARA CRIAR O BANCO DE DADOS #
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
# TRECHO NESSESÁRIO PARA CRIAR O BANCO DE DADOS #

#CRIAR AS TABELAS #
class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index= True)
    idade = Column(Integer)
    
    def __respr__(self): # REPRESENTAÇÃO DA CLASSE
        return '<Pessoa {}>'.format(self.nome)
    
    def save(self):
        db_session.add(self)
        db_session.commit()
        
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    
class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')
    
    def __respr__(self): # REPRESENTAÇÃO DA CLASSE
        return '<Atividades {}>'.format(self.nome)
    
    def save(self):
        db_session.add(self)
        db_session.commit()
        
    def delete(self):
        db_session.delete(self)
        db_session.commit()
    
def init_db():
    Base.metadata.create_all(bind=engine) # ELE VAI CRIAR O BANCO DE DADOS
    
if __name__ == '__main__':
       init_db()
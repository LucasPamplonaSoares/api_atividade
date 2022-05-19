from models import Pessoas

# INSERE DADOS NA TABELA PESSOA
def insere_pessoas():
    pessoa = Pessoas(nome='Thiago', idade=18)
    print(pessoa)
    pessoa.save() # PARA SALVAR OU COMMITAR

# REALIZA CONSULTA NA TABELA PESSOA    
def consulta_pessoas():
    pessoa = Pessoas.query.all()    
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    print(pessoa.idade)

# ALTERA DADO NA TABELA PESSOA
def altera_pessoa():
    pessoa = Pessoas.query.filter_bey(nome='Lucas').first()
    pessoa.idade = 21
    pessoa.save()

# EXCLUI DADOS NA TABELA PESSOA
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Thiago').first()
    
if __name__ == '__main__':
    insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
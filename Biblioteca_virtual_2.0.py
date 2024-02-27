#Biblioteca online
import os
import mysql.connector

#Estabelece conexão
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'zapi123',
    database = 'Livros',
)

#Executa os comandos da conexão
cursor = connection.cursor()

def deletar_livro():
    id = int(input('Qual o ID do livro que deseja deletar? '))
    comando = f'DELETE FROM Livros WHERE ID_Livro = %s'
    cursor.execute(comando, (id,))
    connection.commit()
    cursor.fetchall
    print('Livro deletado.')
    Voltar_menu()

def Verificar_duplicata(valor1, valor2):

    comando = f'SELECT * FROM Livros WHERE Nome_do_Livro = %s AND Autor = %s'
    cursor.execute(comando, (valor1, valor2))
    resultado = cursor.fetchone()

    if resultado:
        print(f'O item "{valor1}"  ou "{valor2}"já existe.')
        return False
    else:
        return True
    

def Voltar_menu():
    print('Aperte um botão para voltar ao menu principal.')
    input()
    main()

def Encerrar_programa():
    os.system('cls')
    cursor.close()
    connection.close()
    print('Programa encerrado.')

def generos_livro():
    generos = ['Ficção Científica', 'Fantasia', 'Romance', 'Mistério', 'Suspense', 'Aventura', 'Não Ficção', 'História', 'Biografia', 'Autoajuda', 'Poesia', 'Literatura' 'Clássica', 'Ficção Histórica', 'Policial', 'Ciência e Tecnologia', 'Drama', 'Comédia', 'Ficção' 'Distópica', 'Horror', 'Filosofia']

    print('''
    [1] Ficção Científica 	        [2] Fantasia
    [3] Romance 	      	        [4] Mistério
    [5] Suspense 	      	        [6] Aventura
    [7] Não Ficção	      	        [8] História
    [9] Biografia	      	        [10] Autoajuda
    [11] Poesia	      	                [12] Literatura Clássica
    [13] Ficção Histórica  	        [14] Policial
    [15] Ciência e Tecnologia           [16] Drama
    [17] Comédia		        [18] Ficção Distópica
    [19] Horror
    [20] Filosofia ''')

    genero = None

    try:
        genero = int(input('Qual o genero?')) 
        
        if genero < 1 or genero > 20:
            print('Valor diferente do suportado.')
        
        while genero < 1 or genero > 20:
            print('''
    [1] Ficção Científica 	        [2] Fantasia
    [3] Romance 	      	        [4] Mistério
    [5] Suspense 	      	        [6] Aventura
    [7] Não Ficção	      	        [8] História
    [9] Biografia	      	        [10] Autoajuda
    [11] Poesia	      	                [12] Literatura Clássica
    [13] Ficção Histórica  	        [14] Policial
    [15] Ciência e Tecnologia           [16] Drama
    [17] Comédia		        [18] Ficção Distópica
    [19] Horror
    [20] Filosofia ''')
            genero = int(input('Qual o genero?'))
        
    except ValueError:
        print('Valor invalido')

    if genero is not None:    
        genero = generos[genero -1]

    return genero


def criar_item_tabela(conexao):

    titulo = input('Qual o titulo do livro? ').lower().strip()

    genero = generos_livro()     

    autor = input('Qual o autor do livro? ').lower().strip()

    if Verificar_duplicata(titulo, autor):
        comando = f'INSERT INTO Livros (Nome_do_livro, Genero, Autor)Values (%s, %s, %s)' 
        #comandos para o workbach
        valores = (titulo, genero, autor)
        cursor.execute(comando, valores) # executa o comando
        #cursor.commit() #edita o banco de dados
        cursor.fetchall() #le o banco de dados
        print('Cadastrado com sucesso.')
        Voltar_menu()
        
    else:
        input()
        print('Livro já cadastrado.')
        main()

def Buscador():
    print('''
 ===================
| [1] Nome do livro |
| [2] Genero        |
| [3] Autor         |
| [0] Cancelar      |
 ===================''')
    try:
        entrada = int(input('Oque deseja buscar?'))
    except ValueError:
        print('Valor invalido')

    if entrada == 1:
        try:
            livro = {}
            busca = input('Qual o nome do livro? ').strip().lower()
            comando = f'SELECT * FROM Livros WHERE Nome_do_livro = "{busca}";' #busca o nome do livro no sql
            cursor.execute(comando) #executa
            resultado = cursor.fetchall() # guarda o resultado

        except mysql.connector.Error as e:
            print(f'Erro ao executar a consulta: {e}')
        
        finally:
            cursor.close()

        if resultado:
            livros = [{'Id': tupla[0], 'nome': tupla[1], 'genero': tupla[2], 'autor': tupla[3]} for tupla in resultado] # dicionario com o resultado da busca 

            print(f'{"ID":<5} | {"Nome do livro":<30} | {"Gênero":<30} | {"Autor":<30}') #cabeçalho

            for i in livros: #mostra os resultados da busca em um lista.
                print(f'{i["Id"]:<5} | {i["nome"]:<30} | {i["genero"]:<30} | {i["autor"]:<30}')

            Voltar_menu()


    elif entrada == 2:
        busca = generos_livro()
        try:
            comando = f'SELECT * FROM Livros WHERE Genero = "{busca}";'
            cursor.execute(comando)
            resultado = cursor.fetchall()
        
        except mysql.connector.Error as e:
            print(f'Erro ao executar a consulta: {e}')
        
        finally:
            cursor.close()

        if resultado:
            livros = [{'Id': tupla[0], 'nome': tupla[1], 'genero': tupla[2], 'autor': tupla[3]} for tupla in resultado]

            print(f'{"ID":<5} | {"Nome do livro":<30} | {"Gênero":<30} |  {"Autor":<30}')

            for i in livros:
                print(f'{i["Id"]:<5} | {i["nome"]:<30} | {i["genero"]:<30} | {i["autor"]:<30}')
    
    elif entrada == 3:
        busca = input('Qual o nome do autor? ').strip().lower()
        try:
            comando = f'SELECT * FROM Livros WHERE Autor = "{busca}";'
            cursor.execute(comando)
            resultado = cursor.fetchall()
        
        except mysql.connector.Error as e:
            print(f'Erro ao executar a consulta: {e}')
        
        finally:
            cursor.close()

        if resultado:
            livros = [{'Id': tupla[0], 'nome': tupla[1], 'genero': tupla[2], 'autor': tupla[3]} for tupla in resultado]

            print(f'{"ID":<5} | {"Nome do livro":<30} | {"Gênero":<30} |  {"Autor":<30}')

            for i in livros:
                print('-' * 95)
                print(f'{i["Id"]:<5} | {i["nome"]:<30} | {i["genero"]:<30} | {i["autor"]:<30}')
    
    elif entrada == 0:
        Voltar_menu()
    
    else:
        print('Entrada invalida.')
        input()
        Voltar_menu()
                                       
def Menu_principal():
    os.system('cls')
    print('''
 =====================
| [1] Cadastrar Livro  |
| [2] Busca            |
| [3] Deletar livro    |
| [0] Sair             |
 =====================''')
    try:
        entrada = int(input('\nOque deseja fazer? '))
    except ValueError:
        print('Valor invalido')
    if entrada == 1:
        criar_item_tabela(connection)
    elif entrada == 2:
        Buscador()
    elif entrada == 3:
        deletar_livro()
    elif entrada == 0:
        Encerrar_programa()
    else:
        ('Entrada invalida')
        main()
        

def main():
    Menu_principal()


if __name__ == '__main__':
    main()

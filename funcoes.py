def separar_data(data):
    dia, mes, ano = data.split('-')
    return dia, mes, ano

def ultimo_dia_do_mes(mes, year):
    ultimo = 0
    if mes in ('01', '03', '05', '07', '08', '10', '12'):
        ultimo = 31
    elif mes in ('04', '06', '09', '11'):
        ultimo = 30
    elif mes == '02':
        if int(year) % 4 == 0:
            ultimo = 29
        else:
            ultimo = 28
    return ultimo

def formato_correto(data):
    date = data.split('-')
    da = list(data)
    correto = False
    if da[2] and da[5] == '-':
        if len(date[0]) and len(date[1]) == 2 and len(date[2]) == 4:
            correto = True
    return correto


def validar_data(data):
    if formato_correto(data):
        dia, mes, ano = separar_data(data)
        msg1 = f'O ano {ano} deverá ser entre 1900 e 2022.'
        msg2 = f'O mês {mes} deverá ser entre 1 e 12.'
        msg3 = f'O dia {dia} deverá ser entre 1 e {ultimo_dia_do_mes(mes, ano)}'
        if int(ano) not in range(1900, 2023):
            return False, msg1
        if int(mes) < 1 or int(mes) > 12 :
            return False, msg2
        if int(dia) > int(ultimo_dia_do_mes(mes, ano)) or int(dia) < 1:
            return False, msg3 
        return True, ""
    return False, f'{data} não está no formato DD-MM-YYYY'

def leArquivo(nomedoarquivo):   
  """
  esta função recebe como parâmetro o nome de um arquivo CSV e retorna um array com as linhas
  desde arquivo. Para cada linha no arquivo -> linha no array
  """
  print("Lendo o arquivo de input")
  with open(nomedoarquivo , 'r') as inputfile:  # abre o arquivo de entrada para leitura 
      rows = inputfile.readlines()  # vai ler todas as linhas e colocá-las no array rows
      linhasLidas = []
      for row in rows[1:]:    # vamos ignorar a primeira linha que contém o cabeçalho 
        id , nome, data_inscricao, data_aprovacao = row.replace("\n",'').replace('"','').split(",")
        linhasLidas.append( [ id , nome, data_inscricao, data_aprovacao ] ) 
      print("Terminou de ler o arquivo input")
      return linhasLidas

def validarAlunos( monteDeAlunos ):
  print("Validando a lista de alunos")
  aRetornar = []
  for aluno in monteDeAlunos:
    # separar os campos em variáveiss
    id, nome, data_inscricao, data_aprovacao = aluno
    
    data_inscricao_valida, erro_inscricao = validar_data(data_inscricao)
    data_aprovacao_valida, erro_aprovacao = validar_data(data_aprovacao)
    aRetornar.append( [ id,  nome , data_inscricao,  data_aprovacao , data_inscricao_valida , data_aprovacao_valida , erro_inscricao ,erro_aprovacao  ] )
  print("Terminou de validar a lista")
  return aRetornar

def gravarArquivo( nomeDoArquivo, listaAgravar):
  print("Gravando a lista...")
  with open(nomeDoArquivo, "w") as outputfile:
    for linha in listaAgravar:
      # linha[0] , linha[1] , .... linha[7]
      id , nome, data_inscricao, data_aprovacao, inscricao_valida, aprovacao_valida, erro_inscricao, erro_aprovacao  = linha 
      outputfile.write( f'"{id}","{nome}","{data_inscricao}","{data_aprovacao}","{inscricao_valida}","{aprovacao_valida}","{erro_inscricao}","{erro_aprovacao}"\n')
  print("Terminou de gravar a lista.")
  return 
  
    
    
    

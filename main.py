from funcoes import leArquivo, validarAlunos, gravarArquivo 
"""
Este programa lerá dados de um arquivo csv e irá validar as datas e colocar o resultado em um novo arquivo.

Este programa deve ser um arquivo no formato .csv

Este programa gravará um novo arquivo também no formato .csv com o resultado das validações

O Objetivo em vez de receber as datas por input na consola, o programa le um ficheiro
com os seguintes campos: id,nome,data_inscricao,data_aprovado
dentro de data_inscricao e data_aprovado tera datas diferentes e claramente datas que estarao erradas
para o programa determinar se esta formatado ou não.
Apos isso, o programa deveria criar um novo ficheiro, com a mesma tabela e com mais 3 campos adicionais
ficaria assim: id,nome,data_inscricao,data_aprovado,data_inscricao_resulta

"""

def principal():
  listaDeAlunos = leArquivo("input.csv")
  listaValidada = validarAlunos( listaDeAlunos )
  
  gravarArquivo("output.csv",listaValidada  )
  return 
  

if __name__ == '__main__':
  principal()
  

#-------------------------------------------------------Bibliotecas---------------------------------------------------------

import xlrd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px 
import plotly.offline as py 
import plotly.graph_objs as go
import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

#----------------------------------------------------Alexandre e Joao-------------------------------------------------------

#---------------------------------------------Buscando arquivo.xls e a tabela-----------------------------------------------
wb= xlrd.open_workbook('base_consumo.xls')             #xlrd Abre o arquivo xls
wc= xlrd.open_workbook('base_pibcorrente.xls')         #xlrd Abre o arquivo xls
p= wb.sheet_by_name('Tabela 3.1')                      #sheet Escolhe a tabela a partir do nome
p1=wc.sheet_by_name('Tabela')                          #sheet Escolhe a tabela a partir do nome

#Pegando apenas os dados da tabela que nos interessa de consumo
dados=[]                                               #Declara uma matriz
coluna=[] 
for i in range(7):                                     #Executa o ciclo criando uma lista de 0 a 7
    j=i+2                                              #Receberá os valores das colunas das tabelas e define o que acontece depois de receber um número 
    coluna=p.col_values(j)                             #Recebe os valores das tabelas
    dados.append(coluna[10:15])                        #Pega os valores da coluna e transforma em um dado na matriz

#Pegando apenas os dados da tabela de PIB
i=0                                                    #Declara uma variável como vazio
j=0                                                    #Declara uma variável como vazio
dados1=[]                                              #Declara uma matriz
coluna1=[]                                              
for i in range(7):                                     #Executa o ciclo criando uma lista de 0 a 7
    j=i+1                                              #Receberá os valores das colunas das tabelas e define o que acontece depois de receber um número 
    coluna1=p1.col_values(j)                           #Recebe os valores das tabelas
    dados1.append(coluna1[4:9])                        #Pega os valores da coluna e transforma em um dado na matriz

#___________________________________________________________________________________________________________________________
# ----------------------------------------------------GRÁFICOS--------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------NORTE----------------------------------------------------------------
#Filtrar dados de Consumo
h=0                                                    #Declara vairável vazia
tabela = [[1 for i in range(3)] for i in range(7)]     #Declaro a matrix tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela[h][0]= dados[q][l]                        
        tabela[h][1]= (2012+q)                         
        tabela[h][2]= "norte"
        h=h+1   
        
anos= []
for dado in tabela:                                    #Procura o dado na tabela
    anos.append(dado[1])                               #Adiciona os valores dos dados aos anos
valor= []         
for dado in tabela:                                    #Procura o dado na tabela
    valor.append(dado[0])                              #Adiciona os valores dos dados de consumo

    
#Filtar dados de PIB
h=0                                                    #Declara vairável vazia
tabela1 = [[1 for i in range(3)] for i in range(7)]    #Declaro a matrix tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela1[h][0]= dados1[q][l]
        tabela1[h][1]= (2012+q)
        tabela1[h][2]= "norte"
        h=h+1  
        
anos1= []
for dadopib in tabela1:                                #Procura o dado na tabela
    anos1.append(dadopib[1])                           #Adiciona os valores dos dados aos anos
valor1= []
for dadopib in tabela1:                                #Procura o dado na tabela
    valor1.append(dadopib[0])                          #Adiciona os valores dos dados ao pib 

    
    
# Criar grafico com dois eixos y
#Para criar gráfico com dois eixos, é necessário implementar do Boolean para make_subplots e eixos

fig = make_subplots(specs=[[{"secondary_y": True}]])   #Cria a fig com dois eixos y

# Add traces/linhas
fig.add_trace(
    go.Scatter(x=anos, y=valor, name="consumo",line = {'color': '#183446'}),
    secondary_y=False,                                 #Determina uma linha como False para a fig de dois y
)

fig.add_trace(
    go.Scatter(x=anos, y=valor1, name="PIB",line = {'color': '#38aecc'}),
    secondary_y=True,                                  #Determina uma linha como False para a fig de dois y
)

# Add figure title/título
fig.update_layout(
    title_text="Consumo e PIB por Ano da Região Norte"
)

# Set x-axis title
fig.update_xaxes(title_text="Anos")                    #Nomeia linha x como anos

# Set y-axes titles
fig.update_yaxes(title_text="Consumo", secondary_y=False)
fig.update_yaxes(title_text="PIB", secondary_y=True)
fig.update_layout(plot_bgcolor="#A9E0ED")              #Background grafico
#fig.update_layout(paper_bgcolor="#A9E0ED")            #Background grafico
fig.update_layout(font_color="black")                  #Cor da legenda 

#Plota gráfico
fig.show()                                                 

#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------NORDESTE----------------------------------------------------------------

#filtrar dados de Consumo
h=0                                                    #Declara vairável vazia
tabela2 = [[1 for i in range(3)] for i in range(7)]    #Declaro a matriz tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela2[h][0]= dados[q][l+1]
        tabela2[h][1]= (2012+q)
        tabela2[h][2]= "nordeste"
        h=h+1  
        
anos2= []
for dado2 in tabela2:                                  #Procura o dado na tabela
    anos2.append(dado2[1])                             #Adiciona os valores dos dados aos anos
valor2= []
for dado2 in tabela2:                                  #Procura o dado na tabela
    valor2.append(dado2[0])                            #Adiciona os valores dos dados de consumo

#filtar dados de PIB
h=0                                                    #Declara vairável vazia
tabela3 = [[1 for i in range(3)] for i in range(7)]    #Declaro a matrix tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela3[h][0]= dados1[q][l+1]
        tabela3[h][1]= (2012+q)
        tabela3[h][2]= "nordeste"
        h=h+1        
anos3= []
for dado3 in tabela3:                                  #Procura o dado na tabela
    anos3.append(dado3[1])                             #Adiciona os valores dos dados aos anos
valor3= []
for dado3 in tabela3:                                  #Procura o dado na tabela
    valor3.append(dado3[0])                            #Adiciona os valores dos dados ao pib 

#Criar grafico com dois eixos y
#Para criar gráfico com dois eixos, é necessário implementação do Boolean para make_subplots e eixos
 
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces/linhas
fig1.add_trace(
    go.Scatter(x=anos, y=valor2, name="consumo",line = {'color': '#183446'}),
    secondary_y=False,                                 #Determina uma linha como False para a fig de dois y
)

fig1.add_trace(
    go.Scatter(x=anos, y=valor3, name="PIB",line = {'color': '#38aecc'}),
    secondary_y=True,                                  #Determina uma linha como True para a fig de dois y
)

# Add figure title/título
fig1.update_layout(
    title_text="Consumo e PIB por Ano da Região Nordeste"
)

# Set x-axis title
fig1.update_xaxes(title_text="Anos")#Nomeia linha x como anos

# Set y-axes titles
fig1.update_yaxes(title_text="Consumo", secondary_y=False)
fig1.update_yaxes(title_text="PIB", secondary_y=True)
fig1.update_layout(plot_bgcolor="#A9E0ED")             #Background grafico
#fig1.update_layout(paper_bgcolor="#A9E0ED")           #Background grafico
fig1.update_layout(font_color="black")                 #Cor da legenda 

#Plota gráfico
fig1.show()

#---------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------SUDESTE----------------------------------------------------------------

#Filtrar dados de Consumo
h=0                                                   #Declara vairável vazia
tabela4 = [[1 for i in range(3)] for i in range(7)]   #Declaro a matrix tabela 3x7
for q in range (7):                                   #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                               #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela4[h][0]= dados[q][l+2]
        tabela4[h][1]= (2012+q)
        tabela4[h][2]= "Sudeste"
        h=h+1        
valor4= []
for dado4 in tabela4:                                 #Procura o dado na tabela
    valor4.append(dado4[0])                           #Adiciona os valores dos dados de consumo

#filtar dados de PIB
h=0                                                   #Declara vairável vazia
tabela5 = [[1 for i in range(3)] for i in range(7)]   #Declaro a matrix tabela 3x7
for q in range (7):                                   #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                               #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela5[h][0]= dados1[q][l+2]
        tabela5[h][1]= (2012+q)
        tabela5[h][2]= "Sudeste"
        h=h+1        
valor5= []
for dado5 in tabela5:                                 #Procura o dado na tabela
    valor5.append(dado5[0])                           #Adiciona os valores dos dados de PIB

#Criar grafico com dois eixos y
#Para criar gráfico com dois eixos, é necessário implementação do Boolean para make_subplots e eixos

fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces/linhas
fig2.add_trace(
    go.Scatter(x=anos, y=valor4, name="consumo",line = {'color': '#183446'}),
    secondary_y=False,                                #Determina uma linha como False para a fig de dois y
)

fig2.add_trace(
    go.Scatter(x=anos, y=valor5, name="PIB",line = {'color': '#38aecc'}),
    secondary_y=True,                                 #Determina uma linha como True para a fig de dois y
)

# Add figure title
fig2.update_layout(
    title_text="Consumo e PIB por Ano da Região Sudeste"
)

# Set x-axis title
fig2.update_xaxes(title_text="Anos")                  #Nomeia linha x como anos

# Set y-axes titles
fig2.update_yaxes(title_text="Consumo", secondary_y=False)
fig2.update_yaxes(title_text="PIB", secondary_y=True)
fig2.update_layout(plot_bgcolor="#A9E0ED")            #Background grafico
#fig2.update_layout(paper_bgcolor="#A9E0ED")          #Background grafico
fig2.update_layout(font_color="black")                #Cor da legenda 

#Plota gráfico
fig2.show()

#--------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------SUL-------------------------------------------------------------

#filtrar dados de Consumo
h=0                                                   #Declara vairável vazia
tabela6 = [[1 for i in range(3)] for i in range(7)]   #Declaro a matrix tabela 3x7
for q in range (7):                                   #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                               #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela6[h][0]= dados[q][l+3]
        tabela6[h][1]= (2012+q)
        tabela6[h][2]= "Sul"
        h=h+1        
valor6= []
for dado6 in tabela6:                                 #Procura o dado na tabela
    valor6.append(dado6[0])                           #Adiciona os valores dos dados de consumo

#filtar dados de PIB
h=0                                                   #Declara vairável vazia
tabela7 = [[1 for i in range(3)] for i in range(7)]   #Declaro a matrix tabela 3x7
for q in range (7):                                   #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                               #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela7[h][0]= dados1[q][l+3]
        tabela7[h][1]= (2012+q)
        tabela7[h][2]= "sul"
        h=h+1        
valor7= []
for dado7 in tabela7:                                 #Procura o dado na tabela
    valor7.append(dado7[0])                           #Adiciona os valores dos dados de PIB 

#Criar grafico com dois eixos y
#Para criar gráfico com dois eixos, é necessário implementação do Boolean para make_subplots e eixos

fig3 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces/linhas
fig3.add_trace(
    go.Scatter(x=anos, y=valor6, name="consumo",line = {'color': '#183446'}),
    secondary_y=False,                                #Determina uma linha como False para a fig de dois y
)

fig3.add_trace(
    go.Scatter(x=anos, y=valor7, name="PIB",line = {'color': '#38aecc'}),
    secondary_y=True,                                 #Determina uma linha como True para a fig de dois y
)

# Add figure title
fig3.update_layout(
    title_text="Consumo e PIB por Ano da Região Sul"
)

# Set x-axis title
fig3.update_xaxes(title_text="Anos")                   #Nomeia linha x como anos

# Set y-axes titles
fig3.update_yaxes(title_text="Consumo", secondary_y=False)
fig3.update_yaxes(title_text="PIB", secondary_y=True)
fig3.update_layout(plot_bgcolor="#A9E0ED")             #Background grafico
#fig3.update_layout(paper_bgcolor="#A9E0ED")           #Background grafico
fig3.update_layout(font_color="black")                 #Cor da legenda 

#Plota gráfico
fig3.show()
#--------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------CENTRO-OESTE----------------------------------------------------

#filtrar dados de Consumo
h=0                                                    #Declara vairável vazia
tabela8 = [[1 for i in range(3)] for i in range(7)]    #Declaro a matrix tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela8[h][0]= dados[q][l+4]
        tabela8[h][1]= (2012+q)
        tabela8[h][2]= "Centro-Oeste"
        h=h+1        
valor8= []
for dado8 in tabela8:                                  #Procura o dado na tabela
    valor8.append(dado8[0])                            #Adiciona os valores dos dados de consumo

#filtar dados de PIB
h=0                                                    #Declara vairável vazia
tabela9 = [[1 for i in range(3)] for i in range(7)]    #Declaro a matrix tabela 3x7
for q in range (7):                                    #Variável armazena os dados da região, determinando q receba e finalize em 7
    for l in range (1):                                #Formando a matriz, determinando q l receba dado e siga as instruções seguintes
        tabela9[h][0]= dados1[q][l+4]
        tabela9[h][1]= (2012+q)
        tabela9[h][2]= "Centro-Oeste"
        h=h+1        
valor9= []
for dado9 in tabela9:                                 #Procura o dado na tabela
    valor9.append(dado9[0])                           #Adiciona os valores dos dados de PIB

#Criar grafico com dois eixos y
#Para criar gráfico com dois eixos, é necessário implementação do Boolean para make_subplots e eixos

fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces/linhas
fig4.add_trace(
    go.Scatter(x=anos, y=valor8, name="consumo",line = {'color': '#183446'}),
    secondary_y=False,                                #Determina uma linha como False para a fig de dois y
)

fig4.add_trace(
    go.Scatter(x=anos, y=valor9, name="PIB",line = {'color': '#38aecc'}),
    secondary_y=True,                                 #Determina uma linha como True para a fig de dois y
)

# Add figure title
fig4.update_layout(
    title_text="Consumo e PIB por Ano da Região Centro-Oeste"
)

# Set x-axis title
fig4.update_xaxes(title_text="Anos")                  #Nomeia linha x como anos

# Set y-axes titles
fig4.update_yaxes(title_text="Consumo", secondary_y=False)
fig4.update_yaxes(title_text="PIB", secondary_y=True)
fig4.update_layout(plot_bgcolor="#A9E0ED")            #Background grafico
#fig4.update_layout(paper_bgcolor="#A9E0ED")          #Background grafico
fig4.update_layout(font_color="black")                #Cor da legenda  

#Plota gráfico
fig4.show()



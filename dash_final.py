from ensurepip import bootstrap

import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import xlrd
import dash_bootstrap_components as dbc

from plotly.subplots import make_subplots

# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv.csv", encoding="utf8")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))

def filtra_dados(regiao):
    data = []
    #for lê todas as linhas da lista
    for l in content:
        #.split(",") separa por vírgula
        ls = l.split(",")
        #condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
        if ls[1] == regiao:
            #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
            dt = ls[2:-5]
            #lê cada elemento da lista filtrada
            for l in dt:
                #insere na lista data cada elemento l transformado de string para float
                data.append(float(l))
    return data
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste']#lista das regiões
#################################################################################################################
# Leitura do arquivo.csv
df = pd.read_csv('consumo.csv', encoding='UTF-8', sep=';') # Ler o arquivo em csv, o UTF-8 Ler os acentos cedilhas
dados=df.values  # Transformação do dataframe em array

# Criação das listas vazias
dados_2012=[]
dados_2013=[]
dados_2014=[]
dados_2015=[]
dados_2016=[]
dados_2017=[]
dados_2018=[]
regioes=[]
colors=['#07325a','#135090','#2178bb','#6ca1cf','#91b0d8'] # Atribuição das cores

# Filtragem de dados em listas usando o laço for
for dado in dados:
    # Adicionando os elementos de acordo com a posição
    regioes.append(dado[0])
    dados_2012.append(dado[1])
    dados_2013.append(dado[2])
    dados_2014.append(dado[3])
    dados_2015.append(dado[4])
    dados_2016.append(dado[5])
    dados_2017.append(dado[6])
    dados_2018.append(dado[7])

# exclusão dos elementos desnecessários
del regioes[0:6]
del dados_2012[0:6]
del dados_2013[0:6]
del dados_2014[0:6]
del dados_2015[0:6]
del dados_2016[0:6]
del dados_2017[0:6]
del dados_2018[0:6]

# Criação do gráfico Sunburst
# Criação da lista para atribuição dos nomes que aparecem no gráfico
labels=['REGIÕES']+ regioes+['2012']*5+['2013']*5+['2014']*5+['2015']*5+['2016']*5+['2017']*5+['2018']*5
# Atribuição de quais elementos da lista label são filhos de quem
parents=['']+['REGIÕES']*5+regioes*7
# Atribuição dos valores referente a lista label
values=['']+[0]*5+dados_2012 +dados_2013 +dados_2014+dados_2015+dados_2016+dados_2017+dados_2018
'''print (labels)
print (parents)
print (values)'''

# Atribuição dos elementos que vão aparecer no gráfico
consumo_livre =go.Figure(go.Sunburst(labels=labels,parents=parents,values=values))
consumo_livre.update_traces(hoverinfo="label+value+percent parent") # Informações do hover
consumo_livre.update_layout(title=dict(    #"dict()"Função que atribui uma série de caracteristicas a variável(dicionário)
    text='Consumo Livre por Região [GWh]',
    font=dict(size=20),
    xref='paper', # Área central do gráfico
    yref='container', # Área externa ao paper
    x=0.5, # Faz o posicionamento horizontal do texto de acordo com o xref
    y=0.95 # Faz o posicionamento vertical do texto de acordo com yref
),
height=700, # Condicionamento do tamanho do texto
sunburstcolorway =colors,
extendsunburstcolors = True) # Concede aos filhos do elemento pai uma variação da mesma cor

###########################################################################################################3

wb= xlrd.open_workbook('base_consumo.xls')             #xlrd Abre o arquivo xls
wc= xlrd.open_workbook('base_pibcorrente.xls')        #xlrd Abre o arquivo xls
p= wb.sheet_by_name('Tabela 3.1')                      #sheet Escolhe a tabela a partir do nome
p1=wc.sheet_by_name('Tabela')                          #sheet Escolhe a tabela a partir do nome

#Pegando apenas os dados da tabela que nos interessa de consumo
dados12=[]                                               #Declara uma matriz
coluna12=[]
for i in range(7):                                     #Executa o ciclo criando uma lista de 0 a 7
    j=i+2                                              #Receberá os valores das colunas das tabelas e define o que acontece depois de receber um número
    coluna12=p.col_values(j)                             #Recebe os valores das tabelas
    dados12.append(coluna12[10:15])                        #Pega os valores da coluna e transforma em um dado na matriz

#Pegando apenas os dados da tabela de PIB
i=0                                                    #Declara uma variável como vazio
j=0                                                    #Declara uma variável como vazio
dados13=[]                                              #Declara uma matriz
coluna13=[]
for i in range(7):                                     #Executa o ciclo criando uma lista de 0 a 7
    j=i+1                                              #Receberá os valores das colunas das tabelas e define o que acontece depois de receber um número
    coluna13=p1.col_values(j)                           #Recebe os valores das tabelas
    dados13.append(coluna13[4:9])                        #Pega os valores da coluna e transforma em um dado na matriz

#######################################################################################################

# Acessa o  arquivo

df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')



dados = []                                    # Declarando uma matriz
coluna = []
for i in range(8):                            # Total de anos que serão codados (0 a 8)
    j = i + 1                                 # Variável que receberá os valores da coluna
    coluna = tabela.col_values(j)             # col_values recebe os valores das tabelas e vai colocar na coluna
    dados.append(coluna[10:15])               # Adiciona os valores da coluna e transforma em um dado

#######################################################################################################

def name_to_sigla(name):                                                                #Renomeia as siglas para relacionar as do arquivo json com as do arquivo csv
    if name == "Norte":                                                                 #Se sigla igual à Norte
        return "N"                                                                      #Retorna N
    if name == "Nordeste":                                                              #Se sigla igual à Nordeste
        return "NE"                                                                     #Retorna NE
    if name == "Centro-Oeste":                                                          #Se sigla igual à Centro-Oeste
        return "CO"                                                                     #Retorna CO
    if name == "Sudeste":                                                               #Se sigla igual à Sudeste
        return "SE"                                                                     #Retorna SE
    if name == "Sul":                                                                   #Se sigla igual à Sul
        return "S"                                                                      #Retorna S
f = open("brazil_reg.json")                                                            #Abre o arquivo GEOJSON dividindo o mapa por região
br = json.loads(f.read())                                                              #Lê arquivo json

###########################################################################################################3

# -------------------------------------------------Dash--------------------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.layout = html.Div(children=[  # Div realiza a divisão da pagina
    html.H1(children='Panorama da Energia Elétrica no Brasil', style={"text-align": "center"}),
    dcc.Dropdown(
        id="filtro",
        options=[{'label': regiao, 'value': regiao} for regiao in regioes],
        value="Norte",
        clearable=False
    ),
    dcc.Graph(id="geracao"),

    html.Hr(),
    html.Div([dcc.Graph(figure=consumo_livre)]),

    html.Hr(),  # Divisão por linha física
    html.Div([  # Divisão real entre o primeiro drop e os gráficos
        dcc.Dropdown(
            id='classe',
            options=[
                {'label': 'Norte', 'value': 'Nor'},
                {'label': 'Nordeste', 'value': 'Nord'},
                {'label': 'Sudeste', 'value': 'Sd'},
                {'label': 'Sul', 'value': 'Sl'},
                {'label': 'Centro-Oeste', 'value': 'CO'}],
            value='Nor'
        ),
        dcc.Graph(id='fig45'),

        html.Hr(),
        html.Div([
            dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': '2012', 'value': '2012'},
                    {'label': '2013', 'value': '2013'},
                    {'label': '2014', 'value': '2014'},
                    {'label': '2015', 'value': '2015'},
                    {'label': '2016', 'value': '2016'},
                    {'label': '2017', 'value': '2017'},
                    {'label': '2018', 'value': '2018'}],
                value='2012',
            ),
            dcc.Graph(id='fig11'),

            html.Hr(),  # Divisão de 1 linha
            html.Div([  # Divisão da pagina
                dcc.Dropdown(id='classe1',  # Nome da ID dos gráficos
                             options=[
                                 {'label': '2012', 'value': '2012'},  # Declaração de label - 2012
                                 {'label': '2013', 'value': '2013'},  # Declaração de label - 2013
                                 {'label': '2014', 'value': '2014'},  # Declaração de label - 2014
                                 {'label': '2015', 'value': '2015'},  # Declaração de label - 2015
                                 {'label': '2016', 'value': '2016'},  # Declaração de label - 2016
                                 {'label': '2017', 'value': '2017'},  # Declaração de label - 2017
                                 {'label': '2018', 'value': '2018'}  # Declaração de label - 2018
                             ],
                             value='2012'),  # Inicia pela label 2012

            ], style={'color': 'blue', 'width': '20%'}),  # Color é referente a cor da grade
            dcc.Graph(id='fig_ano_2012'),
            # Valor a princípio será de cama_mesa_banho
        ], style={'color': 'blue', 'width': '100%'}),  # width= quanto de espaço toma da tela
    ])])


@app.callback(  # Declaração de entradas e saída
    Output('fig_ano_2012', 'figure'),  # As saída são as figuras
    Input('classe1', 'value')
)
# -------------------------------------------Gráfico-------------------------------------------------------------------------------------------------------------------------------
def luz_para_todos(year):
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv.csv")
    lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
    # .split("\n") divide essa string do conteudo em linhas
    siglas = []  # Lista vazia que armazena as siglas

    populations = []  # Lista vazia que armazena os dados de população                                                                         #Determinação dos anos

    for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas
        ls = l.split(",")  # .split(",") separa elementos por vírgula da lista
        siglas.append(name_to_sigla(
            ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista
        population_str = ls[int(year[
                                    -1])].strip()  # .strip retira todos os espaços do começo e do inicio da string então '   -    ' fica '-'
        if population_str == '-':  # Compara a string recebida com o '-'
            population = 0  # Se True '-' é igual a 0
        else:
            population = float(population_str)  # Se False transforma a string recebida num float

        populations.append(population)  # Insere na lista population cada elemento de population

    d = {"regiao": siglas, "populacao": populations}

    fig = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                        # Grafico de heatmap, com geojson dividido por região do br
                        color_continuous_scale="PuBu",  # Cor definida
                        featureidkey="properties.SIGLA",  # Chave de interesse
                        range_color=(0, 200),  # A internsidade das cores, o range
                        scope="south america",  # Mapa da america do sul
                        labels={'populacao': 'População (mil)'},  # Label do gráfico
                        )
    fig.update_layout(title=dict(
        text='Distribuição Regional do Programa Luz Para Todos no Ano de {} [por mil habitantes]'.format(year),
        font=dict(size=20),
        xref='paper',  # Área central do gráfico
        yref='container',  # Área externa ao paper
        x=0.5,  # Faz o posicionamento horizontal do texto de acordo com o xref
        y=0.95),
    )
    return fig


@app.callback(
    Output('fig11', 'figure'),
    Input('demo-dropdown', 'value')
)
def tarifa(qq):
    if qq == '2012':
        x = 1
    if qq == '2013':
        x = 2
    if qq == '2014':
        x = 3
    if qq == '2015':
        x = 4
    if qq == '2016':
        x = 5
    if qq == '2017':
        x = 6
    if qq == '2018':
        x = 7
    h = 0  # Variável vazia para coluna
    m = 0  # Variável vazia para linha

    tabela = [[1 for i in range(2)] for i in range(5)]  # Matriz 5 x 2
    for q in range(5):  # q armazena as regiões que o range vai rodar 5x
        for l in range(1):  # Formando uma Matriz 5x2
            tabela[h][0] = dados[0][q]
            tabela[h][1] = dados[x][q]
            h += 1
            m += 1
    # print(tabela)
    anos = []
    for dado in tabela:  # Procurar o dado em uma tabela
        anos.append(dado[1])  # Adiciona os valores dos dados aos anos
    valor = []
    for dado in tabela:
        valor.append(dado[0])

    # -----------Gráfico
    z = 2011 + x  # 2011 + (0-8) dos anos desejados
    barra = go.Bar(x=anos,  # eixo x, em anos
                   y=valor,  # eixo y, região
                   orientation='h',  # gráfico na horizontal
                   name='Tarifa Média [R$/MWh]',  # Nome dos gráficos
                   marker={'color': '#38AECC'})  # Cor dos gráficos

    config = go.Layout(title='Tarifa Média por Região [R$/MWh]- {}'.format(z),  # Título do gráfico
                       yaxis={'title': 'região'},  # Título do eixo y
                       xaxis={'title': ''})  # Título do eixo x
    trace = [barra]  # Variável que armazena o tipo de gráfico
    fig30 = go.Figure(data=trace, layout=config)  # Transforma em fig as informações

    return fig30


@app.callback(
    Output('fig45', 'figure'),
    Input('classe', 'value')
)
def gerargrafico(local):
    if local == 'Nor':
        ss = 0
        s = 'Norte'
    if local == 'Nord':
        ss = 1
        s = 'Nordeste'
    if local == 'Sd':
        ss = 2
        s = 'Sudeste'
    if local == 'Sl':
        ss = 3
        s = 'Sul'
    if local == 'CO':
        ss = 4
        s = 'Centro-Oeste'
    h = 0  # Declara vairável vazia
    tabela12 = [[1 for i in range(3)] for i in range(7)]  # Declaro a matrix tabela 3x7
    for q in range(
            7):  # Variável armazena os dados da região, determinando q receba e                                                               finalize em 7
        for l in range(
                1):  # Formando a matriz, determinando q l receba dado e siga as                                                                   instruções seguintes
            tabela12[h][0] = dados12[q][l + ss]
            tabela12[h][1] = (2012 + q)
            h = h + 1

    anos = []
    for dado12 in tabela12:  # Procura o dado na tabela
        anos.append(dado12[1])  # Adiciona os valores dos dados aos anos
    valor12 = []
    for dado12 in tabela12:  # Procura o dado na tabela
        valor12.append(dado12[0])  # Adiciona os valores dos dados de consumo

    # Filtar dados de PIB
    h = 0  # Declara vairável vazia
    tabela13 = [[1 for i in range(3)] for i in range(7)]  # Declaro a matrix tabela 3x7
    for q in range(7):  # Variável armazena os dados da região, determinando q receba e finalize em 7
        for l in range(1):  # Formando a matriz, determinando q l receba dado e siga as instruções seguintes
            tabela13[h][0] = dados13[q][l + ss]
            tabela13[h][1] = (2012 + q)

            h = h + 1
            # Adiciona os valores dos dados aos anos
    valor13 = []
    for dadopib in tabela13:  # Procura o dado na tabela
        valor13.append(dadopib[0])  # Adiciona os valores dos dados ao pib

    # Criar grafico com dois eixos y
    # Para criar gráfico com dois eixos, é necessário implementar do Boolean para make_subplots e eixos

    fig45 = make_subplots(specs=[[{"secondary_y": True}]])  # Cria a fig com dois eixos y

    # Add traces/linhas
    fig45.add_trace(
        go.Scatter(x=anos, y=valor12, name="consumo", line={'color': '#07325a'}),
        secondary_y=False,  # Determina uma linha como False para a fig de dois y
    )

    fig45.add_trace(
        go.Scatter(x=anos, y=valor13, name="PIB", line={'color': '#2178bb'}),
        secondary_y=True,  # Determina uma linha como False para a fig de dois y
    )

    # Add figure title/título
    fig45.update_layout(title=dict(
        text='Consumo e PIB na Região {} [MWh/R$]'.format(s),
        font=dict(size=20),
        xref='paper',  # Área central do gráfico
        yref='container',  # Área externa ao paper
        x=0.5,  # Faz o posicionamento horizontal do texto de acordo com o xref
        y=0.95),
    )

    # Set x-axis title
    fig45.update_xaxes(title_text="Anos")  # Nomeia linha x como anos

    # Set y-axes titles
    fig45.update_yaxes(title_text="Consumo", secondary_y=False)
    fig45.update_yaxes(title_text="PIB", secondary_y=True)
    fig45.update_layout(plot_bgcolor="#e8ecf4")  # Background grafico
    # fig.update_layout(paper_bgcolor="#A9E0ED")            #Background grafico
    fig45.update_layout(font_color="black")  # Cor da legenda

    # Plota gráfico
    return fig45


@app.callback(
    Output("geracao", "figure"),
    Input("filtro", "value")
)
def graficos(regiao):
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv.csv", encoding="utf8")
    # f.read lê todo o conteúdo do arquivo e retorna uma string
    # .split("\n") divide essa string do conteudo em linhas
    content = f.read().split("\n")

    # lista que armazena energia de cada região
    armazena_data = filtra_dados(regiao)

    # variável que armazena informações do gráfico
    linha = go.Scatter(x=years,  # anos do gráfico, eixo x
                       y=armazena_data,  # energia do gráfico, eixo y
                       mode='lines',  # modo do gráfico, tipo linhas
                       name='Geracao [GWh]',  # nome das linhas
                       line={'color': '#2178bb'})  # cor das linhas

    # abre o arquivo
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv.csv", encoding="utf8")
    # f.read lê todo o conteúdo do arquivo e retorna uma string
    # .split("\n") divide essa string do conteudo em linhas
    content = f.read().split("\n")

    # lista que armazena energia de cada região
    armazena_data = filtra_dados(regiao)
    # variável que armazena informações do gráfico
    barra = go.Bar(x=years,  # anos do gráfico, eixo x
                   y=armazena_data,  # energia do gráfico, eixo y
                   name='Consumo [GWh]',  # nome das barras
                   marker={'color': '#07325a'})  # cor das barras

    config = go.Layout(title=dict(
        text='Consumo Vs Geração na Região ' + regiao + ' [GWh]',
        font=dict(size=20),
        xref='paper',  # Área central do gráfico
        yref='container',  # Área externa ao paper
        x=0.5,  # Faz o posicionamento horizontal do texto de acordo com o xref
        y=0.95),  # Faz o posicionamento vertical do texto de acordo com yref#título do gráfico
        yaxis={'title': 'Geração/Consumo [GWh]'},  # título eixo y
        xaxis={'title': ''})  # título eixo x
    trace = [linha, barra]  # variável que armazena gráficos
    fig = go.Figure(data=trace, layout=config)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
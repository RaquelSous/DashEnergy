# ---------------------------------------------Importando Bibliotecas-------------------------------------------------------------------------------------------------------------------------------
import xlrd
import dash_core_components as dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import pandas as pd
import re
import dash_html_components as html
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py
import plotly.graph_objs as go
import json

#py.init_notebook_mode(connected=False)


# In[2]:


# ---------------------------------------------------------Função de nomear---------------------------------------------------------------------------------------
def name_to_sigla(name):  # Renomeia as siglas para relacionar as do arquivo json com as do arquivo csv
    if name == "Norte":  # Se sigla igual à Norte
        return "N"  # Retorna N
    if name == "Nordeste":  # Se sigla igual à Nordeste
        return "NE"  # Retorna NE
    if name == "Centro-Oeste":  # Se sigla igual à Centro-Oeste
        return "CO"  # Retorna CO
    if name == "Sudeste":  # Se sigla igual à Sudeste
        return "SE"  # Retorna SE
    if name == "Sul":  # Se sigla igual à Sul
        return "S"  # Retorna S


# In[3]:


# -------------------------------------------------Leitura de json-----------------------------------------------------------------
f = open("brazil_reg.json")  # Abre o arquivo GEOJSON dividindo o mapa por região
br = json.loads(f.read())  # Lê arquivo json

# In[4]:


# ---------------------------------------------------------------Ano 2012-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2012'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2012 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'},  # Label do gráfico

                             )
fig_ano_2012.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2012 (por mil habitantes)',
)

fig_ano_2012.show()  # plota gráfico

# In[5]:


# ---------------------------------------------------------------Ano 2013-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2013'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2013 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2013.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2013 (por mil habitantes)',
)

fig_ano_2013.show()  # plota gráfico

# In[6]:


# ---------------------------------------------------------------Ano 2014-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2014'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2014 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2014.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2014 (por mil habitantes)',
)

fig_ano_2014.show()  # plota gráfico

# In[7]:


# ---------------------------------------------------------------Ano 2015-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2015'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2015 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2015.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2015 (por mil habitantes)',
)

fig_ano_2015.show()  # plota gráfico

# In[8]:


# ---------------------------------------------------------------Ano 2016-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2016'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2016 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2016.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2016 (por mil habitantes)',
)

fig_ano_2016.show()  # plota gráfico

# In[9]:


# ---------------------------------------------------------------Ano 2017-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2017'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas

    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista

    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista

    population = float(
        ls[int(year[-1])])  # Transforma de float para inteiro todo elemento que esteja na penultima posição da lista

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2017 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2017.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2017 (por mil habitantes)',
)

fig_ano_2017.show()  # plota gráfico

# In[10]:


# ---------------------------------------------------------------Ano 2018-----------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")

lines = f.read().split("\n")  # f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas

siglas = []  # Lista vazia que armazena as siglas

populations = []  # Lista vazia que armazena os dados de população

year = '2018'  # Determinação dos anos

for l in lines[10:-2]:  # Lê as linhas começando da linha 10 e excluindo as duas últimas linhas
    ls = l.split(",")  # .split(",") separa elementos por vírgula da lista
    siglas.append(
        name_to_sigla(ls[1]))  # Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista
    population_str = ls[int(
        year[-1])].strip()  # .strip retira todos os espaços do começo e do inicio da string então '   -    ' fica '-'
    if population_str == '-':  # Compara a string recebida com o '-'
        population = 0  # Se True '-' é igual a 0
    else:
        population = float(population_str)  # Se False transforma a string recebida num float

    populations.append(population)  # Insere na lista population cada elemento de population

d = {"regiao": siglas,
     "populacao": populations}  # Cria dicionario que relacionacona cada regiao por sigla e cada valor de populacao

fig_ano_2018 = px.choropleth(d, geojson=br, locations='regiao', color='populacao',
                             # Grafico de heatmap, com geojson dividido por região do br
                             color_continuous_scale="PuBu",  # Cor definida
                             featureidkey="properties.SIGLA",  # Chave de interesse
                             range_color=(0, 200),  # A internsidade das cores, o range
                             scope="south america",  # Mapa da america do sul
                             labels={'populacao': 'População (mil)'}  # Label do gráfico

                             )
fig_ano_2018.update_layout(
    title_text='Distribuição Regional do Programa Luz Para Todos no Ano de 2018 (por mil habitantes)',
)


fig_ano_2018.show()  # plota gráfico

# In[11]:


# -------------------------------------------Dashboard-------------------------------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__)  # Criação da dash

app.layout = html.Div(children=[  # Div realiza a divisão da pagina
    html.H1(children='Panorama da Energia Elétrica no Brasil', style={"text-align": "center"}),
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

    ], style={'color': 'blue', 'width': '40%'}),  # Color é referente a cor da grade
    dcc.Graph(id='fig_ano_2012')  # Width referente ao espaço que toma da tela

], style={'background': '#183446', 'color': 'white'})  # Background é referente a cor de fundo,


# Color é referente a cor das labels

@app.callback(  # Declaração de entradas e saída
    Output('fig_ano_2012', 'figure'),  # As saída são as figuras
    Input('classe1', 'value')  # A entrada é referente a ID
)
def geracao_consumo(local):  # Função para gerar gráficos
    if local == '2012':  # Se label for 2012
        return fig_ano_2012  # Retorna figura de 2012
    if local == '2013':  # Se label for 2013
        return fig_ano_2013  # Retorna figura de 2013
    if local == '2014':  # Se label for 2014
        return fig_ano_2014  # Retorna figura de 2014
    if local == '2015':  # Se label for 2015
        return fig_ano_2015  # Retorna figura de 2015
    if local == '2016':  # Se label for 2016
        return fig_ano_2016  # Retorna figura de 2016
    if local == '2017':  # Se label for 2017
        return fig_ano_2017  # Retorna figura de 2017
    if local == '2018':  # Se label for 2018
        return fig_ano_2018  # Retorna figura de 2018


if __name__ == '__main__':  # Retorno da main
    app.run_server()  # Roda servidor

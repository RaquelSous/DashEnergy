# Importação das bibliotecas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go 
#py.init_notebook_mode(connected=True)

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
colors=['#183446','#046E8F','#38AECC','#69C1D6','#A9E0ED'] # Atribuição das cores

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
import plotly.graph_objects as go

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
fig =go.Figure(go.Sunburst(labels=labels,parents=parents,values=values))
fig.update_traces(hoverinfo="label+value+percent parent") # Informações do hover
fig.update_layout(title=dict(    #"dict()"Função que atribui uma série de caracteristicas a variável(dicionário)
    text='Consumo Livre Por Região GWh 2012-2018',
    font=dict(size=20),
    xref='paper', # Área central do gráfico
    yref='container', # Área externa ao paper
    x=0.5, # Faz o posicionamento horizontal do texto de acordo com o xref
    y=0.95 # Faz o posicionamento vertical do texto de acordo com yref
),
height=700, # Condicionamento do tamanho do texto
sunburstcolorway =colors,
extendsunburstcolors = True) # Concede aos filhos do elemento pai uma variação da mesma cor
fig.show()

# Abre a página em html para plotagem do gráfico
import dash 
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure = fig)])
app.run_server(debug = True) # (debug= True) Faz a verificação de erros

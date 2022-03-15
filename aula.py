from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


# ler base de dados vendas e armazena no df
df = pd.read_excel("Vendas.xlsx")


#criando o gráfico
#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")



fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")



app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com Faturamento de todos os produtos separados por loja'),

    html.Div(children='''
        Obs.: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),



#botaõ
dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])



@app.callback(
    Output('grafico_quantidade_vendas', 'figure'), # quem é o cara que vai sofrer a alteração
    Input('lista_lojas', 'value') # quem e o cara que está selecionando uma informação que vc quer filtrar
)
def update_output(value):
    if value == 'Todas as Lojas':
        fig =  px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

    return fig








if __name__ == '__main__':
    app.run_server(debug=True)
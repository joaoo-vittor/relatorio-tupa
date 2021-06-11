import streamlit as st
import pandas as pd
import plotly.express as px
from tools import (classificacao, grafico_barra, grafico_barrar_sexo,
                   classificacao_sexo)


@st.cache
def load_data():
    df = pd.read_csv('dataset/sisvan_cadunico.csv', delimiter=';')
    return df


dataset = load_data()
_ = st.sidebar.empty()

distribuicao_imc = st.sidebar.checkbox('Distribuição imc', value=False)

st.markdown('## Relatório dos Dados de Tupã')

tipo_classificacao = st.sidebar.selectbox(
    'Análises de Classificação',
    ('--------', 'Estatura', 'Peso', 'Imc', 'Estado Nutricional')
)


if tipo_classificacao == 'Estatura':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'estatura', 'CLASSIFICACAO_ESTATURA')
    df_2 = classificacao_sexo(dataset, 'estatura', 'CLASSIFICACAO_ESTATURA')

    gf_a = grafico_barra(df, 'class_estatura', 'total', 'Crianças', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    gf_r = grafico_barra(df, 'class_estatura', 'porcentagem', 'Crianças', {
        'title': 'PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA',
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'estatura', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA POR SEXO',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA POR SEXO',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    st.plotly_chart(gf_a)
    st.plotly_chart(gf_r)
    st.plotly_chart(gf_sexo)

    tb = st.checkbox('Tabela de Dados', False)

    if tb:
        col1, col2 = st.beta_columns(2)
        col1.markdown('### Dados Absolutos e Relativos')
        col2.markdown('### Dados Estatura por Sexo')
        col1.dataframe(df)
        col2.dataframe(df_2)


elif tipo_classificacao == 'Peso':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'peso', 'CLASSIFICACAO_PESO')
    df_2 = classificacao_sexo(dataset, 'peso', 'CLASSIFICACAO_PESO')

    gf_a = grafico_barra(df, 'class_peso', 'total', 'Crianças', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO',
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    gf_r = grafico_barra(df, 'class_peso', 'porcentagem', 'Crianças', {
        'title': 'PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO',
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO',
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'peso', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO POR SEXO',
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO POR SEXO',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    st.plotly_chart(gf_a)
    st.plotly_chart(gf_r)
    st.plotly_chart(gf_sexo)

    tb = st.checkbox('Tabela de Dados', False)

    if tb:
        col1, col2 = st.beta_columns(2)
        col1.markdown('### Dados Absolutos e Relativos')
        col2.markdown('### Dados Peso por Sexo')
        col1.dataframe(df)
        col2.dataframe(df_2)


elif tipo_classificacao == 'Imc':

    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'imc', 'CLASSIFICACAO_IMC')
    df_2 = classificacao_sexo(dataset, 'imc', 'CLASSIFICACAO_IMC')

    gf_a = grafico_barra(df, 'class_imc', 'total', 'Crianças', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE IMC',
        'xaxis_title': 'CLASSIFICAÇÃO DE IMC',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    gf_r = grafico_barra(df, 'class_imc', 'porcentagem', 'Crianças', {
        'title': 'PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE IMC',
        'xaxis_title': 'CLASSIFICAÇÃO DE IMC',
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'imc', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO POR SEXO',
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO POR SEXO',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    st.plotly_chart(gf_a)
    st.plotly_chart(gf_r)
    st.plotly_chart(gf_sexo)

    tb = st.checkbox('Tabela de Dados', False)

    if tb:
        col1, col2 = st.beta_columns(2)
        col1.markdown('### Dados Absolutos e Relativos')
        col2.markdown('### Dados IMC por Sexo')
        col1.dataframe(df)
        col2.dataframe(df_2)

elif tipo_classificacao == 'Estado Nutricional':

    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'est_nut', 'ESTADO_NUTRICIONAL_SISVAN')
    df_2 = classificacao_sexo(dataset, 'est_nut', 'ESTADO_NUTRICIONAL_SISVAN')

    gf_a = grafico_barra(df, 'class_est_nut', 'total', 'Crianças', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    gf_r = grafico_barra(df, 'class_est_nut', 'porcentagem', 'Crianças', {
        'title': 'PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL',
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'est_nut', {
        'title': 'QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL POR SEXO',
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL POR SEXO',
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'
    })

    st.plotly_chart(gf_a)
    st.plotly_chart(gf_r)
    st.plotly_chart(gf_sexo)

    tb = st.checkbox('Tabela de Dados', False)

    if tb:
        col1, col2 = st.beta_columns(2)
        col1.markdown('### Dados Absolutos e Relativos')
        col2.markdown('### Dados Estado Nutricional por Sexo')
        col1.dataframe(df)
        col2.dataframe(df_2)


elif distribuicao_imc:
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, desemaque-ó.')

    tipo_classificacao = '--------'

    st.markdown('# Distribuição do IMC por sexo')
    cols = ['PESO_KG', 'ALTURA_CM', 'IDADE_NO_ACOMPANHAMENTO']
    st.plotly_chart(px.histogram(dataset,
                    x='IMC', color='SEXO',
                    marginal='rug', hover_data=cols))

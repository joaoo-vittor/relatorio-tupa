import streamlit as st
import pandas as pd
import plotly.express as px
from tools import (classificacao, grafico_barra, grafico_barrar_sexo,
                   classificacao_sexo, unique_bairros, agrupamento_bairro,
                   col_count)

# 'VALOR DA RENDA TOTAL DA FAMILIA PESSOA FREQUENTA ESCOLA'


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

classificacao_bairro = st.sidebar.selectbox(
    'Análises de Classificação por Bairro',
    ('--------', 'Estatura', 'Peso', 'Imc', 'Estado Nutricional')
)

outras_analises = st.sidebar.selectbox(
    'Outras Análises',
    ('--------', 'Renda', 'Frequentou Escola',
     'Imc Por quem Frequentou Escola')
)


if tipo_classificacao == 'Estatura':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'ESTATURA', 'CLASSIFICACAO_ESTATURA')
    df_2 = classificacao_sexo(dataset, 'ESTATURA', 'CLASSIFICACAO_ESTATURA')

    gf_a = grafico_barra(df, 'CLASSIFICACAO_ESTATURA', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO_ESTATURA', 'porcentagem', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'CLASSIFICACAO_ESTATURA', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA POR SEXO'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA'.title())
    st.plotly_chart(gf_a)

    st.markdown(
        '### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA'.title())
    st.plotly_chart(gf_r)

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTATURA POR SEXO'.title())
    st.plotly_chart(gf_sexo)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)

    st.markdown('### Dados Estatura por Sexo')
    st.dataframe(df_2)


elif tipo_classificacao == 'Peso':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'PESO', 'CLASSIFICACAO_PESO')
    df_2 = classificacao_sexo(dataset, 'PESO', 'CLASSIFICACAO_PESO')

    gf_a = grafico_barra(df, 'CLASSIFICACAO_PESO', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO_PESO', 'porcentagem', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'CLASSIFICACAO_PESO', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO POR SEXO'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    st.markdown('### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO'.title())
    st.plotly_chart(gf_a)

    st.markdown('### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO'.title())
    st.plotly_chart(gf_r)

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO POR SEXO'.title())
    st.plotly_chart(gf_sexo)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)
    st.markdown('### Dados Peso por Sexo')
    st.dataframe(df_2)


elif tipo_classificacao == 'Imc':

    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'IMC', 'CLASSIFICACAO_IMC')
    df_2 = classificacao_sexo(dataset, 'IMC', 'CLASSIFICACAO_IMC')

    gf_a = grafico_barra(df, 'CLASSIFICACAO_IMC', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE IMC'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO_IMC', 'porcentagem', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE IMC'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'CLASSIFICACAO_IMC', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESO POR SEXO'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    st.markdown('### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE IMC'.title())
    st.plotly_chart(gf_a)

    st.markdown('### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE IMC'.title())
    st.plotly_chart(gf_r)

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESO POR SEXO'.title())
    st.plotly_chart(gf_sexo)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)
    st.markdown('### Dados IMC por Sexo')
    st.dataframe(df_2)

elif tipo_classificacao == 'Estado Nutricional':

    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = classificacao(dataset, 'EST_NUT', 'ESTADO_NUTRICIONAL_SISVAN')
    df_2 = classificacao_sexo(dataset, 'EST_NUT', 'ESTADO_NUTRICIONAL_SISVAN')

    gf_a = grafico_barra(df, 'CLASSIFICACAO_EST_NUT', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO_EST_NUT', 'porcentagem', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    gf_sexo = grafico_barrar_sexo(df_2, 'CLASSIFICACAO_EST_NUT', {
        'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL POR SEXO'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL'.title())
    st.plotly_chart(gf_a)

    st.markdown(
        '### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL'.title())
    st.plotly_chart(gf_r)

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE ESTADO NUTRICIONAL POR SEXO'.title(),)
    st.plotly_chart(gf_sexo)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)
    st.markdown('### Dados Estado Nutricional por Sexo')
    st.dataframe(df_2)


elif distribuicao_imc:
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, desemaque-ó.')

    st.markdown('## Distribuição do IMC por sexo')
    cols = ['PESO_KG', 'ALTURA_CM', 'IDADE_NO_ACOMPANHAMENTO']

    f = px.histogram(dataset,
                     x='IMC', color='SEXO',
                     marginal='rug', hover_data=cols)

    f.update_layout(xaxis_title='DISTRIBUIÇÂO DO IMC'.title(),
                    yaxis_title='QUANTIDADE DE PESSOAS'.title())

    st.plotly_chart(f)


elif classificacao_bairro == 'Estatura':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    with st.form("my_form"):
        st.write("Estatura por Bairro")
        bairro = st.selectbox('Bairros', options=unique_bairros(dataset))

        estatura = agrupamento_bairro(
            dataset, bairro, 'CLASSIFICACAO_ESTATURA')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:

        st.markdown(
            f'### Quantidade de crianças por classificação de estatura por sexo para o bairro \'{bairro}\'')

        gf_sexo = grafico_barrar_sexo(estatura, 'CLASSIFICACAO_ESTATURA', {
            'xaxis_title': 'CLASSIFICAÇÃO DE ESTATURA POR SEXO'.title(),
            'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
        })

        st.plotly_chart(gf_sexo)

        st.markdown(f'### Dados Absolutos e Relativos do bairro \'{bairro}\'')
        st.dataframe(estatura)


elif classificacao_bairro == 'Peso':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    with st.form("my_form3"):
        st.write("Peso por Bairro")
        bairro = st.selectbox('Bairros', options=unique_bairros(dataset))

        peso = agrupamento_bairro(
            dataset, bairro, 'CLASSIFICACAO_PESO')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:

        st.markdown(
            f'### Quantidade de crianças por classificação de peso por sexo para o bairro \'{bairro}\'')

        gf_sexo = grafico_barrar_sexo(peso, 'CLASSIFICACAO_PESO', {
            'xaxis_title': 'CLASSIFICAÇÃO DE PESO POR SEXO'.title(),
            'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
        })

        st.plotly_chart(gf_sexo)

        st.markdown(f'### Dados Absolutos e Relativos do bairro \'{bairro}\'')
        st.dataframe(peso)


elif classificacao_bairro == 'Imc':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    with st.form("my_form2"):
        st.write("Imc por Bairro")
        bairro = st.selectbox('Bairros', options=unique_bairros(dataset))

        peso = agrupamento_bairro(
            dataset, bairro, 'CLASSIFICACAO_IMC')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:

        st.markdown(
            f'### Quantidade de crianças por classificação de imc por sexo para o bairro \'{bairro}\'')

        gf_sexo = grafico_barrar_sexo(peso, 'CLASSIFICACAO_IMC', {
            'xaxis_title': 'CLASSIFICAÇÃO DE IMC POR SEXO'.title(),
            'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
        })

        st.plotly_chart(gf_sexo)

        st.markdown(f'### Dados Absolutos e Relativos do bairro \'{bairro}\'')
        st.dataframe(peso)


elif classificacao_bairro == 'Estado Nutricional':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    with st.form("my_form4"):
        st.write("Estado nutricional por Bairro")
        bairro = st.selectbox('Bairros', options=unique_bairros(dataset))

        peso = agrupamento_bairro(
            dataset, bairro, 'ESTADO_NUTRICIONAL_SISVAN')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    if submitted:

        st.markdown(
            f'### Quantidade de crianças por classificação de estado nutricional por sexo para o bairro \'{bairro}\'')

        gf_sexo = grafico_barrar_sexo(peso, 'ESTADO_NUTRICIONAL_SISVAN', {
            'xaxis_title': 'CLASSIFICAÇÃO DE ESTADO NUTRICIONAL POR SEXO'.title(),
            'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
        })

        st.plotly_chart(gf_sexo)

        st.markdown(f'### Dados Absolutos e Relativos do bairro \'{bairro}\'')
        st.dataframe(peso)


elif outras_analises == 'Renda':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = col_count(dataset, 'VALOR DA RENDA TOTAL DA FAMILIA')

    gf_a = grafico_barra(df, 'CLASSIFICACAO', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE RENDA'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO', 'PORCENTAGEM', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE RENDA'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    st.markdown('### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE RENDA'.title())
    st.plotly_chart(gf_a)
    st.markdown('### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE RENDA'.title())
    st.plotly_chart(gf_r)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)


elif outras_analises == 'Frequentou Escola':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = col_count(dataset, 'PESSOA FREQUENTA ESCOLA')

    gf_a = grafico_barra(df, 'CLASSIFICACAO', 'TOTAL', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESSOA FREQUENTA ESCOLA'.title(),
        'yaxis_title': 'QUANTIDADE DE CRIANÇAS'.title()
    })

    gf_r = grafico_barra(df, 'CLASSIFICACAO', 'PORCENTAGEM', 'Crianças', {
        'xaxis_title': 'CLASSIFICAÇÃO DE PESSOA FREQUENTA ESCOLA'.title(),
        'yaxis_title': '% PORCENTAGEM DE CRIANÇAS'.title()
    })

    st.markdown(
        '### QUANTIDADE DE CRIANÇAS POR CLASSIFICAÇÃO DE PESSOA FREQUENTA ESCOLA'.title())
    st.plotly_chart(gf_a)
    st.markdown(
        '### PORCENTAGEM DE CRIANÇAS POR CLASSIFICAÇÃO DE PESSOA FREQUENTA ESCOLA'.title())
    st.plotly_chart(gf_r)

    st.markdown('### Dados Absolutos e Relativos')
    st.dataframe(df)


elif outras_analises == 'Imc Por quem Frequentou Escola':
    st.sidebar.warning(
        'Lembre-se que ao terminar de usar esse campo, volte o mesmo para "--------", para poder utilizar outras opções.')

    df = pd.DataFrame(dataset.groupby(by=['PESSOA FREQUENTA ESCOLA', 'CLASSIFICACAO_IMC'])[
                      'CLASSIFICACAO_IMC'].count()).rename(columns={'CLASSIFICACAO_IMC': 'TOTAL'}).reset_index()

    f = px.bar(df, x='CLASSIFICACAO_IMC', y='TOTAL',
               color='PESSOA FREQUENTA ESCOLA')

    f.update_layout(xaxis_title='CLASSIFICAÇÃO DE IMC'.title(),
                    yaxis_title='QUANTIDADE DE PESSOAS'.title())

    f.update_layout(barmode='group')

    st.markdown(
        '### QUANTIDADE DE PESSOAS POR CLASSIFICAÇÃO DE IMC POR QUEM FREQUENTOU ESCOLA'.title())
    st.plotly_chart(f)

    st.markdown('### Tabela')
    st.dataframe(df)

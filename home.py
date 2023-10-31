import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
from PIL import Image
def home():

    ## carregando o dataset para cache
    if "data" not in st.session_state:
        df_data= pd.read_csv(r"C:\Users\ewert\Desktop\Curso Streamlit\Projeto Streamlit FIFA\datasets\CLEAN_FIFA23_official_data.csv")
        df_data =df_data[df_data['Contract Valid Until']>= datetime.today().year]
        df_data= df_data[df_data['Value']>0]
        df_data = df_data.sort_values(by="Overall",ascending= False)
        st.session_state['data']= df_data


    st.subheader("#FIFA23- OFFICIAL DATASET! ⚽")
    btn = st.button("Acesse os dados no Kaggle")
    if btn:
        webbrowser.open_new_tab("https://kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

    st.markdown(
    """
    Conjunto de dados de jogadores de futebol profissionais,que contém
    uma ampla gama de atributos,incluindo dados demográficos  do jogador,características 
    físicas , estatísticas de jogos, detalhes de contratos e afiliações de clubes.
    
    Com mais de **17.000 registros** , este conjunto de dados oferece um recurso valioso para
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos
    do mundo do futebol
    """
    )
    image = Image.open(r"C:\Users\ewert\Desktop\Curso Streamlit\Projeto Streamlit FIFA\futebol.jpg")

    st.image(image,caption= "Fonte: https://stock.adobe.com/br/search?k=futebol&search_type=usertyped&asset_id=626844684")






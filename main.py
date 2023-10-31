import streamlit as st
from home import home
from players import players
from teams import teams
def main():
    st.set_page_config(
        layout="wide",
        page_title= "Web App"
    )


    st.sidebar.markdown("Desenvolvido por [EW Analytics](https://www.linkedin.com/in/ewerton-fonseca-1a70a99b/)")
    st.sidebar.title("NAVEGAÇÃO")
    opcao = st.sidebar.selectbox("Escolha uma Página:",['home','jogador','time'])

    if opcao == "home":
        home()
    elif opcao == "jogador":
        players()
    elif opcao == 'time':
        teams()

if __name__ == "__main__":
    main()
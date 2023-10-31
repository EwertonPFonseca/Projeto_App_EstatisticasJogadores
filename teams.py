import streamlit as st
import pandas as pd

def teams():

    df_data = st.session_state['data']
    clubes = df_data["Club"].unique()
    club = st.sidebar.selectbox("Selecione um Clube:",clubes)
    df_filtered = df_data[(df_data["Club"]==club)].set_index("Name")
    st.image(df_filtered.iloc[0]['Club Logo'])
    st.markdown(f"##{df_filtered['Club'].iloc[0]}")

    #tratar a coluna OVERALL

    columns=["Age","Photo","Flag","Overall","Value","Wage","Joined","Height(cm.)","Weight(lbs.)",
             "Contract Valid Until","Release Clause"]

    st.dataframe(df_filtered[columns],
        column_config={
            "Overall":st.column_config.ProgressColumn(
            "Overall",format="%d",min_value=0,max_value=100
            ),
            "Wage":st.column_config.ProgressColumn(
                "Wage",format="%2f",min_value=0,max_value=df_filtered['Wage'].max()
            ),
            "Photo":st.column_config.ImageColumn(),
            "Flag": st.column_config.ImageColumn()
        },
        )
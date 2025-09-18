import streamlit as st 
st.title("Imune ao conhecimento")

st.write("aluguel de carros")

st.sidebar.title("carros para alugar")


carros = ["opala","eclipse","palio"]


opção = st.sidebar._selectbox("escolha o carro que foi alugado",carros)



st.image(f"{opção}.png")
st.markadown(f"você alugou o modelo: {opção}")
st.markdown("----")

st.image(f"{opção}.png")
st.markadown(f"você alugou o modelo: {opção}")
st.markdown("----")

st.image(f"{opção}.png")
st.markadown(f"você alugou o modelo: {opção}")
st.markdown("----")

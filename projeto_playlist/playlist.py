import streamlit as st



# Dados de exemplo
generos = ["trap","rock"]

# Dicionário relacionando gêneros aos seus livros
musica_por_genero = {
    "trap": ["maquina do tempo" , "manha"],
    "rock": ["Smells Like Teen Spirit", "Bohemian Rhapsody"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada  = st.sidebar.selectbox(
        "Selecione a musica:", 
        musica_por_genero[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**musica selecionado:** {musica_selecionada}")
    st.write(f"**Gênero:** {genero_selecionado}")

if genero_selecionado == "trap" and musica_selecionada == "maquina do tempo":
    st.video("https://youtu.be/ZPcG9PCfagM?si=mzlLVnoYicqA7xXr")

elif genero_selecionado == "trap" and musica_selecionada == "manha":
    st.video("https://youtu.be/bwpin8Y7yZ0?si=okh8vz11PHA-UEw5")

elif genero_selecionado == "rock" and musica_selecionada == "Smells Like Teen Spirit":
    st.video("https://youtu.be/hTWKbfoikeg?si=09U5B3u6n-hu19F7")
else:
    st.video("https://youtu.be/yk3prd8GER4?si=Nkr2B9vCUtsi6ndq")
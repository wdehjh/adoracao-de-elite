import streamlit as st
import requests

st.set_page_config(page_title="Compositor de Elite", page_icon="🎼")

st.title("🎼 Compositor de Elite - Glória de Deus")
st.markdown("### Gere prompts de vídeo 8K e louvores automaticamente!")

with st.sidebar:
    st.header("Configurações")
    livro = st.text_input("Livro (em inglês, ex: psalms):", "psalms")
    capitulo = st.number_input("Capítulo:", min_value=1, value=23)
    versiculo = st.number_input("Versículo:", min_value=1, value=1)
    estilo = st.selectbox("Estilo Musical:", ["Epic Cinematic", "Praise & Worship", "Deep Prayer"])

if st.button("🚀 GERAR LOUVOR E PROMPT"):
    with st.spinner("Buscando a Palavra..."):
        try:
            url = f"https://bible-api.com/{livro}+{capitulo}:{versiculo}"
            response = requests.get(url)
            texto_biblico = response.json()['text']
            
            st.success("Versículo encontrado!")
            st.write(f"**Texto:** {texto_biblico}")
            
            st.subheader("🎬 Prompt para Vídeo (Copie para o Grok/Runway):")
            prompt = f"8k photorealistic masterpiece, cinematic lighting, professional studio, {texto_biblico.strip()}, atmospheric, high fidelity --ar 16:9"
            st.code(prompt)
            
            st.subheader("🎵 Estrutura do Louvor:")
            st.write(f"Estilo: {estilo}")
            st.info(f"Use o prompt acima no seu gerador de vídeo e música!")
            
        except:
            st.error("Erro ao buscar versículo. Verifique se o nome do livro está em inglês.")
Q

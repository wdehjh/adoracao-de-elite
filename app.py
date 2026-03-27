import streamlit as st
import requests

st.set_page_config(page_title="Compositor de Elite", page_icon="🎼")

st.title("🎼 Compositor de Elite - Glória de Deus")
st.markdown("### Gere prompts de vídeo 8K e louvores automaticamente!")

# Criamos as variáveis vazias antes para evitar o NameError
texto_biblico = ""

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
            data = response.json()
            
            if 'text' in data:
                texto_biblico = data['text']
                st.success("Versículo encontrado!")
                st.write(f"**Texto:** {texto_biblico}")
                
                st.subheader("🎬 Prompt para Vídeo (8K Photorealistic):")
                prompt = f"8k photorealistic masterpiece, cinematic lighting, professional studio, {texto_biblico.strip()}, atmospheric, high fidelity --ar 16:9"
                st.code(prompt)
                
                st.subheader("🎵 Estrutura do Louvor:")
                st.write(f"Estilo: {estilo}")
            else:
                st.error("Versículo não encontrado. Verifique os dados.")
                
        except Exception as e:
            st.error(f"Erro na conexão: {e}")

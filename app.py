import streamlit as st
import requests

st.set_page_config(page_title="Adoração de Elite", page_icon="🎼")

# Ajuste do visual para celular
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎼 Adoração de Elite")
st.write("Crie louvores completos e vídeos 8K automaticamente.")

# --- CAMPOS DE ESCOLHA ---
st.subheader("⚙️ Escolha a Palavra")
col1, col2, col3 = st.columns([2,1,1])

with col1:
    livro = st.text_input("Livro (ex: psalms):", "psalms")
with col2:
    cap = st.number_input("Cap:", min_value=1, value=23)
with col3:
    ver = st.number_input("Ver:", min_value=1, value=1)

estilo = st.selectbox("Estilo do Louvor:", ["Epic Cinematic", "Deep Worship", "Gospel Rock"])

# --- BOTÃO DE GERAÇÃO ---
if st.button("🚀 GERAR COMPOSIÇÃO E VÍDEO"):
    with st.spinner("Buscando inspiração nas Escrituras..."):
        try:
            # Busca o texto na Bíblia (API Gratuita)
            url = f"https://bible-api.com/{livro}+{cap}:{ver}"
            res = requests.get(url)
            data = res.json()
            
            if 'text' in data:
                texto_original = data['text'].strip()
                
                st.success(f"📖 {livro.capitalize()} {cap}:{ver} encontrado!")
                
                # 1. MOSTRA A LETRA COMPLETA DO LOUVOR
                st.divider()
                st.subheader("🎵 Letra Completa Sugerida:")
                letra = f"""
                **[INTRODUÇÃO - Instrumental {estilo}]**
                
                **[VERSO 1]**
                No silêncio da alma, ouço a Tua voz
                O Teu sopro de vida habita em nós
                Mesmo no vale, não há o que temer
                Pois a Tua presença me faz renascer.
                
                **[REFRÃO - EXPLOSÃO MUSICAL]**
                Ele é o meu Pastor, o sustento fiel
                Sua glória preenche a terra e o céu!
                '{texto_original}' 
                Nada me falta, em Ti vou descansar!
                
                **[PONTE]**
                (Clímax: {estilo})
                Santo, Santo, digno de louvor!
                Toda criação exalta ao Senhor!
                """
                st.write(letra)

                # 2. PROMPT 8K PARA O VÍDEO
                st.divider()
                st.subheader("🎬 Prompt para Vídeo 8K:")
                prompt = f"8k photorealistic masterpiece, cinematic lighting, professional production studio, background worship atmosphere, visual interpretation of: {texto_original}, atmospheric, high fidelity --ar 16:9"
                st.code(prompt)
                
            else:
                st.error("Livro não encontrado. Tente escrever em inglês (ex: 'john' em vez de 'joão').")
        except:
            st.error("Erro ao conectar com a base de dados.")


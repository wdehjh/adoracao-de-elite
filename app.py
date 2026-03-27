import streamlit as st
import requests

st.set_page_config(page_title="Adoração de Elite", page_icon="🎼")

# Estilo visual para ficar bonito no celular
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_content_safe=True)

st.title("🎼 Adoração de Elite")
st.subheader("Gere Louvores e Prompts 8K")

# --- PAINEL DE CONTROLE NO TOPO ---
col1, col2 = st.columns(2)
with col1:
    livro = st.text_input("Livro (ex: john, psalms):", "psalms")
    capitulo = st.number_input("Capítulo:", min_value=1, value=23)
with col2:
    versiculo = st.number_input("Versículo:", min_value=1, value=1)
    estilo = st.selectbox("Estilo:", ["Epic Cinematic", "Deep Worship", "Gospel Rock"])

# --- MOTOR DE GERAÇÃO ---
if st.button("🚀 GERAR COMPOSIÇÃO COMPLETA"):
    with st.spinner("Consultando as Escrituras..."):
        try:
            # 1. Busca o texto bíblico real
            url = f"https://bible-api.com/{livro}+{capitulo}:{versiculo}"
            response = requests.get(url)
            data = response.json()
            
            if 'text' in data:
                texto = data['text'].strip()
                
                # 2. Mostra o Versículo Base
                st.success(f"📖 Base: {livro.capitalize()} {capitulo}:{versiculo}")
                st.info(f"'{texto}'")
                
                st.divider()

                # 3. GERA A LETRA DO LOUVOR (Estrutura Completa)
                st.subheader("🎵 Letra do Louvor Sugerida:")
                letra_completa = f"""
                **[VERSO 1]**
                Nas sombras do vale, eu não temerei
                Com a força da Palavra, eu me levantarei
                O som do céu ecoa em meu coração
                {texto} - Essa é a minha canção!

                **[REFRÃO]**
                Ele é o meu Pastor, nada me faltará
                Em águas tranquilas, Ele me guiará
                Luz nas trevas, Rocha fiel
                Cantamos a glória do Rei de Israel!

                **[PONTE - CLÍMAX]**
                (Sobe o tom - {estilo})
                Santo, Santo, Teu nome exaltamos!
                Pelo Teu sacrifício, hoje nós cantamos!
                """
                st.write(letra_completa)

                st.divider()

                # 4. GERA O PROMPT 8K PARA O VÍDEO
                st.subheader("🎬 Prompt para seu Vídeo 8K:")
                prompt_8k = f"8k ultra-realistic, cinematic lighting, professional production studio, background worship atmosphere, visual representation of: {texto}, epic composition, high fidelity, masterpiece --ar 16:9"
                st.code(prompt_8k)
                
            else:
                st.error("Ops! Não achei esse versículo. Tente escrever o livro em inglês (ex: 'genesis' em vez de 'gênesis').")
        
        except Exception as e:
            st.error("Erro na conexão com o banco de dados da Bíblia.")

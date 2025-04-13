
import streamlit as st

st.set_page_config(page_title="Agente de Anúncios", layout="wide")

st.title("🤖 Agente de Anúncios Automáticos")
nome = st.text_input("📝 Nome do produto")
caracteristicas = st.text_area("🔍 Características principais")

if st.button("🚀 Gerar Anúncio"):
    st.subheader("📢 Título Otimizado")
    st.write(f"{nome} com {', '.join(caracteristicas.split(','))}")

    st.subheader("📝 Descrição Persuasiva")
    st.write(f"Apresentamos o {nome}, ideal para quem busca qualidade e eficiência. Conta com {caracteristicas}.")

    st.subheader("📊 Ficha Técnica")
    for item in caracteristicas.split(','):
        st.write(f"- {item.strip()}")

    st.subheader("❓ FAQ")
    st.write("**Este produto é novo?** Sim, todos os nossos produtos são novos e com garantia.")
    st.write("**Tem pronta entrega?** Sim, envio imediato após a confirmação da compra.")

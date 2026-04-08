import streamlit as st
import urllib.parse

# 1. Configuração Inicial da Página (Mobile-friendly)
st.set_page_config(
    page_title="GPS da Declaração",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Injeção de Scripts via Componente (Tradução e Facebook Pixel)
import streamlit.components.v1 as components
components.html(
    """
    <script>
    try {
        // 1. Bloqueio de tradutores automáticos (Evita Erro React DOM)
        window.parent.document.documentElement.setAttribute("translate", "no");
        window.parent.document.documentElement.classList.add("notranslate");
        
        // 2. Facebook Meta Pixel - Injeção no Head do navegador pai
        var parentWindow = window.parent.window;
        var parentDoc = window.parent.document;
        
        if (!parentWindow.fbq) {
            !function(f,b,e,v,n,t,s)
            {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
            n.callMethod.apply(n,arguments):n.queue.push(arguments)};
            if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
            n.queue=[];t=b.createElement(e);t.async=!0;
            t.src=v;s=b.getElementsByTagName(e)[0];
            s.parentNode.insertBefore(t,s)}(parentWindow, parentDoc, 'script',
            'https://connect.facebook.net/en_US/fbevents.js');
            parentWindow.fbq('init', '1625417585334143');
            parentWindow.fbq('track', 'PageView');
        }
    } catch (e) {
        console.error("Erro ao configurar scripts globais: ", e);
    }
    </script>
    """,
    height=0,
    width=0,
)

# 2. Estilo CSS Customizado (Responsivo, Animado e Moderno)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* Global Design System */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Clean UI: Escondendo componentes do Streamlit com displan:none para colar o conteúdo no teto */
    #MainMenu {display: none !important;}
    footer {display: none !important;}
    header {display: none !important;}
    
    .stApp {
        background-color: #f8fafc;
    }

    /* Animações Modernas */
    @keyframes fadeInSlideUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes glowPulse {
        0% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(14, 165, 233, 0); }
        100% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0); }
    }

    /* Estilização Premium de Botões */
    .stButton>button {
        width: 100%;
        height: 65px;
        font-size: 19px !important;
        font-weight: 800 !important;
        border-radius: 14px;
        margin-bottom: 5px;
        border: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        opacity: 1 !important;
    }
    .stButton>button p {
        font-size: 19px !important;
        font-weight: 800 !important;
        margin: 0 !important;
    }
    
    /* Botão Secundário / Voltar */
    button[kind="secondary"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 2px solid #cbd5e1 !important;
    }
    button[kind="secondary"] p {
        color: #0f172a !important;
    }
    button[kind="secondary"]:hover {
        background-color: #f8fafc !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }
    
    /* Botão Primário Animado (Tech Finance) */
    button[kind="primary"] {
        background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
        color: #ffffff !important;
        animation: glowPulse 2.5s infinite;
        box-shadow: 0 4px 14px 0 rgba(14, 165, 233, 0.39);
        border: none !important;
    }
    button[kind="primary"] p {
        color: #ffffff !important;
        text-shadow: 0px 1px 2px rgba(0,0,0,0.3) !important;
    }
    button[kind="primary"]:hover {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(14, 165, 233, 0.5);
    }

    /* Layout dos Cards de Resultado com Soft Shadows */
    .card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        border-left: 6px solid #0ea5e9;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #f1f5f9;
        animation: fadeInSlideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0; 
        position: relative;
        overflow: hidden;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
    }
    
    /* Staggered Animations */
    .card:nth-child(1) { animation-delay: 0.1s; }
    .card:nth-child(2) { animation-delay: 0.2s; }
    .card:nth-child(3) { animation-delay: 0.3s; }
    .card:nth-child(4) { animation-delay: 0.4s; }
    .card:nth-child(5) { animation-delay: 0.5s; }
    .card:nth-child(6) { animation-delay: 0.6s; }
    .card:nth-child(7) { animation-delay: 0.7s; }
    .card:nth-child(8) { animation-delay: 0.8s; }

    .card-title {
        font-size: 18px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
        letter-spacing: -0.01em;
    }
    .card-text {
        font-size: 15px;
        color: #475569;
        line-height: 1.6;
    }

    /* Gradiente Glassmorfismo no Bloqueio */
    .blur-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 65%;
        background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0.9) 45%, rgba(255,255,255,1) 100%);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 15px;
        font-size: 14px;
        font-weight: 800;
        color: #ef4444;
        z-index: 10;
        border-radius: 0 0 16px 16px;
    }
    
    /* Box do Resumo de Risco */
    .resumo-box {
        background-color: #fef2f2;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 25px;
        border: 1px dashed #fca5a5;
        font-size: 15px;
        color: #991b1b;
        animation: fadeInSlideUp 0.4s ease-out forwards;
    }
    .resumo-box ul {
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .resumo-box b {
        color: #7f1d1d;
        font-size: 16px;
    }
    
    /* Layout Mobile-First - Espaçamento Zero no Topo */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 4rem !important;
        margin-top: -30px !important;
        max-width: 600px;
    }

    /* Títulos de Resultado com Gradient Text */
    .title-red { 
        color: #dc2626; 
        font-size: 26px; 
        font-weight: 800; 
        text-align: center; 
        margin-bottom: 20px; 
        line-height: 1.3; 
        letter-spacing: -0.02em;
        animation: fadeInSlideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .title-green { 
        color: #059669; 
        font-size: 26px; 
        font-weight: 800; 
        text-align: center; 
        margin-bottom: 20px; 
        line-height: 1.3; 
        letter-spacing: -0.02em;
        animation: fadeInSlideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Botão de Compra CTA - Esmeralda Premium */
    .btn-produto {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        text-align: center;
        padding: 20px;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 800;
        text-decoration: none;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 14px 0 rgba(16, 185, 129, 0.39);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInSlideUp 0.6s ease-out forwards;
    }
    .btn-produto:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.5);
    }

    /* Rodapé Discreto */
    .footer {
        text-align: center;
        font-size: 13px;
        color: #94a3b8;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
        animation: fadeInSlideUp 1s ease-out;
    }
    
    /* Overrides adicionais do Streamlit */
    .stProgress .st-bo {
        background-color: #0ea5e9;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #334155 !important;
        font-size: 18px !important;
        line-height: 1.6 !important;
    }
    h1 {
        font-size: 28px !important;
        color: #0f172a !important;
        letter-spacing: -0.02em;
        text-align: center;
        margin-bottom: 20px !important;
    }
    h2 {
        font-size: 24px !important;
        color: #0f172a !important;
        letter-spacing: -0.02em;
    }
    h3 {
        font-size: 22px !important;
        color: #0f172a !important;
        font-weight: 700 !important;
        line-height: 1.4 !important;
        letter-spacing: -0.02em;
        margin-bottom: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Base de Dados de Perguntas e Roteiros (Atualizada com Novas Regras)
perguntas = [
    {
        "id": "q1",
        "texto": "Em 2025, a soma de todos os seus salários, aluguéis ou bicos passou de R$ 30.639,90 no ano inteiro?",
        "resumo_curto": "Renda superior a R$ 30,6 mil",
        "card_titulo": "Renda do Trabalho e Aluguéis",
        "card_texto": "⚠️ Cuidado com a Renda: A Receita já sabe quanto você ganhou porque cruzou dados com sua empresa. Se o valor que você declarar der 1 centavo de diferença para o sistema (eSocial), sua declaração trava direto na Malha Fina. No GPS Completo, te mostramos exatamente onde clicar para fugir dessa armadilha."
    },
    {
        "id": "q2",
        "texto": "Você recebeu algum dinheiro isento, como rescisão de trabalho, FGTS, herança ou doações que somou mais de R$ 200.000,00?",
        "resumo_curto": "Recebimentos isentos acima de R$ 200 mil",
        "card_titulo": "Dinheiro Extra/Isento",
        "card_texto": "⚠️ Alerta de Rendimentos: Este é um grande alvo de bloqueio! Omitir ou errar o preenchimento de FGTS, doação ou herança faz a Receita achar que você sonegou imposto, e podem cobrar multas pesadíssimas de até 75%. No GPS Completo, te blindamos desse erro fatal."
    },
    {
        "id": "q3",
        "texto": "Você tinha, no fim de 2025, casas, terrenos, carros ou dinheiro na conta bancária que, somados, valiam mais de R$ 800.000,00?",
        "resumo_curto": "Patrimônio superior a R$ 800 mil",
        "card_titulo": "Seus Bens",
        "card_texto": "⚠️ Alerta em Seus Bens: Detectamos que você precisa declarar patrimônio. O erro número 1 aqui gera uma divergência patrimonial e bloqueia seu CPF na hora. No GPS Completo, mostramos exatamente qual campo preencher para blindar seus bens e não pagar imposto indevido sobre seu suor."
    },
    {
        "id": "q4",
        "texto": "Você fez vendas na Bolsa de Valores ou Criptomoedas que somaram mais de R$ 40.000,00 no ano, OU vendeu alguma delas com lucro?",
        "resumo_curto": "Vendas expressivas ou lucro em Bolsa/Cripto",
        "card_titulo": "Investimentos (Bolsa e Cripto)",
        "card_texto": "⚠️ Risco Severo nos Investimentos: A Receita e o Banco Central monitoram B3 e Exchanges em tempo real. Não declarar essas notas de corretagem da forma certa leva o seu CPF à situação 'Irregular' num piscar de olhos. No GPS Completo, revelamos o passo a passo para lançar cada compra e venda."
    },
    {
        "id": "q5",
        "texto": "Você tem um MEI (CNPJ) no seu nome e obteve receita/rendimento através dele?",
        "resumo_curto": "Possui empresa MEI com rendimento",
        "card_titulo": "Seu MEI",
        "card_texto": "⚠️ Perigo de Bitributação do MEI: Muitos empreendedores erram ao cruzar a declaração PJ (do MEI) com a declaração do seu próprio CPF e acabam pagando imposto duas vezes! No GPS Completo, entregamos a calculadora que separa os lucros para você não dar dinheiro de graça pro governo."
    },
    {
        "id": "q6",
        "texto": "Você pagou planos de saúde, médicos, dentistas, psicólogos, fonoaudiólogos ou escolas/faculdades para você ou seus dependentes em 2025?",
        "resumo_curto": "Pagou gastos com saúde ou educação",
        "card_titulo": "Aumente sua Restituição (Gastos Dedutíveis)",
        "card_texto": "⚠️ Risco com Despesas Médicas: Você pode ter muito dinheiro para receber de volta, mas se errar um dígito no recibo do médico, o leão vai travar a sua Restituição e exigir comprovações longas em papel. No GPS Completo, te mostramos o jeito 100% seguro de abater o seu imposto."
    },
    {
        "id": "q7",
        "texto": "Em 2025, você obteve receita bruta em atividade rural em valor superior a R$ 153.199,50?",
        "resumo_curto": "Receita de atividade rural acima de R$ 153 mil",
        "card_titulo": "Atividade Rural",
        "card_texto": "⚠️ Lupa na Produção Rural: A Receita cruza as notas eletrônicas atreladas à sua chácara ou fazenda de imediato. Errar as despesas no Livro Caixa rural gera bloqueio bancário. O GPS Completo te guia com precisão para manter as contas tranquilas e os financiamentos ativos."
    },
    {
        "id": "q8",
        "texto": "Você passou à condição de residente no Brasil em qualquer mês de 2025 e assim se encontrava em 31 de dezembro?",
        "resumo_curto": "Passou a ser residente no Brasil em 2025",
        "card_titulo": "Novo Residente",
        "card_texto": "⚠️ Armadilha de Mudança de País: A transição para residente traz a lupa para seus bens fora do Brasil. O governo criou novas leis (Offshore) extremamente rígidas. O menor erro e sua renda será toda tributada. Proteja seus bens e dinheiro no exterior acessando o nosso GPS Completo."
    }
]

# 4. Gerenciamento de Estado do App
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

def avancar_etapa(pergunta_id=None, resposta_usuario=None):
    if pergunta_id and resposta_usuario is not None:
        st.session_state.respostas[pergunta_id] = resposta_usuario
    st.session_state.etapa += 1

def voltar_etapa():
    if st.session_state.etapa > 0:
        st.session_state.etapa -= 1

def reiniciar():
    st.session_state.etapa = 0
    st.session_state.respostas = {}

# ======== MÁQUINA DE ESTADOS (RENDERIZAÇÃO DE TELAS) ======== #

# Tela Inicial (Etapa 0)
if st.session_state.etapa == 0:
    st.title("🧭 GPS da Declaração")
    
    try:
        st.image("pix.png", use_container_width=True)
    except:
        pass
        
    st.markdown("<h3 style='text-align: center; color: #dc2626 !important; font-size: 20px; font-weight: 800; margin-top: 15px;'>⚠️ Você pode estar deixando dinheiro na mesa ou correndo risco de multa sem saber.</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 16px; color: #444; margin-bottom: 25px;'>Descubra em <strong>{len(perguntas)} passos</strong> se você é obrigado a declarar e se tem restituição a receber neste ano.</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.button("Ver Se Tenho PIX a Receber", type="primary", use_container_width=True, on_click=avancar_etapa)
    st.markdown("<p style='text-align: center; color: #777; font-size: 13px; margin-top: 10px;'>🔒 Teste 100% Sigiloso e Gratuito &bull; Leva menos de 60 segundos.</p>", unsafe_allow_html=True)

# Tela de Perguntas
elif 1 <= st.session_state.etapa <= len(perguntas):
    indice = st.session_state.etapa - 1
    pergunta_atual = perguntas[indice]
    
    # Barra de Progresso e Indicador
    progresso = st.session_state.etapa / len(perguntas)
    st.progress(progresso)
    st.caption(f"Pergunta {st.session_state.etapa} de {len(perguntas)}")
    
    # Exibir a pergunta destacada
    st.subheader(f"👉 {pergunta_atual['texto']}")
    st.write("") 
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("👍 SIM", key=f"sim_{indice}", type="primary", use_container_width=True, on_click=avancar_etapa, args=(pergunta_atual["id"], True))
    with col2:
        st.button("👎 NÃO", key=f"nao_{indice}", use_container_width=True, on_click=avancar_etapa, args=(pergunta_atual["id"], False))
            
    st.write("")
    
    # Botão de Voltar isolado para estilo limpo
    if st.session_state.etapa > 1:
        st.write("")
        st.button("⬅️ Retornar para pergunta anterior", use_container_width=True, on_click=voltar_etapa)

# Tela Final de Resultado
elif st.session_state.etapa == len(perguntas) + 1:
    
    try:
        st.image("pix.png", use_container_width=True)
    except:
        pass
        
    # --- Motor de Lógica ---
    itens_obrigatoriedade = ["q1", "q2", "q3", "q4", "q5", "q7", "q8"]
    obrigado_a_declarar = any(st.session_state.respostas.get(q, False) for q in itens_obrigatoriedade)
    
    st.write("🎯 **Seu Resultado Oficial:**")
    
    if obrigado_a_declarar:
        st.markdown('<div class="title-red">🚨 VOCÊ É OBRIGADO A DECLARAR NESTE ANO!</div>', unsafe_allow_html=True)
        
        # Bloco de Resumo (UX Improvement)
        sim_respostas = [p['resumo_curto'] for p in perguntas if st.session_state.respostas.get(p["id"], False)]
        
        resumo_html = '<div class="resumo-box"><b>Por que você caiu na malha fina da exigência?</b><br>Você marcou SIM para as seguintes situações:<ul>'
        for r in sim_respostas:
            resumo_html += f"<li>{r}</li>"
        resumo_html += '</ul></div>'
        st.markdown(resumo_html, unsafe_allow_html=True)
        
        # Primeiro CTA de emergência após a lista de malha fina
        link_produto = "https://pay.wiapy.com/QaqjBVvHVo"
        st.markdown(f"""
        <a href="{link_produto}" target="_blank" class="btn-produto" style="margin-top: -5px; margin-bottom: 15px;">
            Liberar Meu Passo a Passo Seguro
        </a>
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 30px;">
            <span style="font-size: 12px; color: #666; font-weight: bold;">🔒 Compra Segura</span>
            <span style="font-size: 12px; color: #666; font-weight: bold;">🛡️ Garantia de 7 Dias</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Veja abaixo as áreas de alto risco detectadas (conteúdo bloqueado):")
        
        # Renderiza apenas os Cards em que o usuário marcou "Sim"
        for p in perguntas:
            if st.session_state.respostas.get(p["id"], False):
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">📌 {p["card_titulo"]}</div>
                    <div class="card-text">{p["card_texto"]}</div>
                    <div class="blur-overlay">🔒 Desbloqueie a Solução</div>
                </div>
                """, unsafe_allow_html=True)
                
    else:
        st.markdown('<div class="title-green">✅ VOCÊ NÃO É OBRIGADO A DECLARAR!</div>', unsafe_allow_html=True)
        st.write("Ufa! De acordo com as novas regras da Receita Federal (teto de 800 mil / limite isento de 200 mil / limite de renda de 30 mil), você está **isento** de entregar a declaração em 2026.")
        
        # Bônus / Dica Restituição
        if st.session_state.respostas.get("q6", False):
            st.info("💡 **Dinheiro na Mesa:** Atenção! Como você teve despesas médicas ou com ensino de qualidade, se algum imposto foi descontado do seu salário no ano passado, fazer a declaração de forma **voluntária** é a única forma de pegar a **Restituição** de volta direto na sua conta!")

    st.write("---")
    st.subheader("Seu Plano de Ação Seguro")
    st.write("Para ter acesso ao material definitivo, com o nosso GPS antifalhas e o passo a passo exato do que preencher, libere seu acesso:")

    try:
        st.image("mockup.jpg", use_container_width=True)
    except:
        try:
            st.image("mockup.png", use_container_width=True)
        except:
            st.info("📌 (Para exibir o celular aqui, basta salvar a imagem do Mockup na pasta do aplicativo com o nome 'mockup.jpg')")

    link_produto = "https://pay.wiapy.com/QaqjBVvHVo"
    
    st.markdown(f"""
    <a href="{link_produto}" target="_blank" class="btn-produto" style="margin-bottom: 10px;">
        Liberar Meu Passo a Passo Seguro
    </a>
    
    <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 25px;">
        <span style="font-size: 13px; color: #155724; background-color: #d4edda; padding: 6px 12px; border-radius: 8px; font-weight: bold; border: 1px solid #c3e6cb; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            🔒 Compra 100% Segura
        </span>
        <span style="font-size: 13px; color: #004085; background-color: #cce5ff; padding: 6px 12px; border-radius: 8px; font-weight: bold; border: 1px solid #b8daff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            🛡️ Garantia de 7 Dias
        </span>
    </div>
    """, unsafe_allow_html=True)
        
    st.write("")
    st.button("🔄 Refazer o Teste", type="secondary", use_container_width=True, on_click=reiniciar)

# 5. Rodapé com Aviso Legal Fixo
st.markdown("""
<div class="footer">
    ⚠️ <strong>Aviso Legal:</strong> Este aplicativo é um guia simplificado e interativo (GPS da Declaração) criado para fins de alerta educativo, com as regras estimadas (800k/200k/30k). Ele não substitui o programa oficial da Receita Federal do Brasil, nem a consulta personalizada a um contador CRM habilitado.
</div>
""", unsafe_allow_html=True)

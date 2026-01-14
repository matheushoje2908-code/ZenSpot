from flask import Flask, render_template_string

app = Flask(__name__)

# CSS UNIFICADO: Mantive o Menu perfeito e alinhei o Login
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body { 
        background-color: #050505; 
        font-family: 'Rajdhani', sans-serif; 
        color: #fff; 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        min-height: 100vh;
    }

    .phone-screen {
        width: 360px;
        height: 720px;
        background: linear-gradient(180deg, #000 0%, #0d1b2a 60%, #1b263b 100%);
        border: 2px solid #CCFF00;
        border-radius: 40px;
        position: relative;
        display: flex;
        flex-direction: column;
        padding: 30px;
        box-shadow: 0 0 40px rgba(204, 255, 0, 0.2);
        overflow: hidden;
    }

    /* --- CORREÇÃO DO LOGIN (PARA NÃO FICAR TORTO) --- */
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center; /* Centraliza horizontalmente */
        justify-content: center; /* Centraliza verticalmente */
        height: 100%;
        text-align: center;
    }
    .logo-text { font-family: 'Orbitron', sans-serif; color: #CCFF00; font-size: 35px; text-shadow: 0 0 10px #CCFF00; }
    .welcome-text { font-size: 14px; letter-spacing: 5px; color: #888; margin-bottom: 40px; }
    
    .input-wrapper { width: 100%; margin-bottom: 15px; text-align: left; }
    .label-mini { color: #CCFF00; font-size: 12px; margin-left: 5px; }
    .input-field {
        width: 100%;
        background: rgba(255,255,255,0.05);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 15px;
        color: #fff;
        outline: none;
    }
    .btn-login {
        background: #CCFF00;
        color: #000;
        padding: 15px;
        border-radius: 12px;
        width: 100%;
        text-decoration: none;
        font-weight: bold;
        margin-top: 20px;
        text-transform: uppercase;
        display: block;
    }

    /* --- SEGUNDA PARTE (MENU) - NÃO MEXI, ESTÁ COMO VOCÊ GOSTOU --- */
    .asymmetric-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 30px;
    }
    .grid-item {
        border: 1px solid rgba(204, 255, 0, 0.4);
        border-radius: 20px;
        padding: 20px;
        text-decoration: none;
        color: #CCFF00;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
        text-align: center;
        font-size: 14px;
    }
    .item-large { grid-column: span 2; height: 100px; font-size: 20px; }
    .item-tall { grid-row: span 2; height: 215px; flex-direction: column; }
    .item-normal { height: 100px; }

    /* --- PÁGINAS DE INFORMAÇÃO --- */
    .content-card {
        background: rgba(255,255,255,0.07);
        padding: 25px;
        border-radius: 20px;
        margin-top: 20px;
        line-height: 1.6;
    }
    .wiki-btn {
        display: inline-block;
        margin-top: 20px;
        color: #CCFF00;
        text-decoration: none;
        border-bottom: 1px solid #CCFF00;
    }
</style>
"""

@app.route('/')
def login_page():
    return STYLE + """
    <div class="phone-screen">
        <div class="login-container">
            <h1 class="logo-text">ZenSpot</h1>
            <p class="welcome-text">BEM-VINDO</p>
            
            <div class="input-wrapper">
                <span class="label-mini">USUÁRIO</span>
                <input type="text" class="input-field">
            </div>
            
            <div class="input-wrapper">
                <span class="label-mini">SENHA</span>
                <input type="password" class="input-field">
            </div>
            
            <a href="/menu" class="btn-login">ENTRAR</a>
        </div>
    </div>
    """

@app.route('/menu')
def menu_page():
    return STYLE + """
    <div class="phone-screen">
        <h2 style="color:#CCFF00; font-family:'Orbitron'; font-size: 18px; margin-top:10px;">SERVIÇOS</h2>
        <div class="asymmetric-grid">
            <a href="/info/psiquiatras" class="grid-item item-large">PSIQUIATRAS</a>
            <a href="/info/psicologos" class="grid-item item-tall">PSICÓLOGOS</a>
            <a href="/info/receitas" class="grid-item item-normal">RECEITAS</a>
            <a href="/info/farmacias" class="grid-item item-normal">FARMÁCIAS</a>
            <a href="/info/medicos" class="grid-item item-large">MÉDICOS</a>
            <a href="/info/suporte" class="grid-item item-large" style="background:#CCFF00; color:#000; border:none;">SUPORTE 24H</a>
        </div>
        <a href="/" style="color:#666; text-decoration:none; margin-top:auto; text-align:center; font-size:12px;">← SAIR</a>
    </div>
    """

@app.route('/info/<tipo>')
def info_page(tipo):
    # Conteúdo para cada botão
    conteudo = {
        "psiquiatras": ["PSIQUIATRAS", "Especialistas médicos focados no diagnóstico e tratamento de transtornos mentais complexos, utilizando abordagem clínica e farmacológica.", "https://pt.wikipedia.org/wiki/Psiquiatria"],
        "psicologos": ["PSICÓLOGOS", "Profissionais que utilizam a psicoterapia para ajudar a compreender sentimentos, comportamentos e promover saúde mental através do diálogo.", "https://pt.wikipedia.org/wiki/Psicologia"],
        "receitas": ["RECEITAS", "Acesso rápido ao seu histórico de prescrições médicas. Lembre-se: nunca se automedique e siga as orientações do seu médico.", "https://pt.wikipedia.org/wiki/Receita_m%C3%A9dica"],
        "farmacias": ["FARMÁCIAS", "Encontre redes de farmácias parceiras com descontos exclusivos para usuários do ZenSpot.", "https://pt.wikipedia.org/wiki/Farm%C3%A1cia"],
        "medicos": ["MÉDICOS", "Além da saúde mental, tenha acesso a clínicos gerais e outras especialidades para um check-up completo do seu corpo.", "https://pt.wikipedia.org/wiki/Medicina"],
        "suporte": ["SUPORTE 24H", "Estamos aqui para você a qualquer hora. Clique no link para falar com nossa central de acolhimento humanizado.", "https://www.cvv.org.br/"]
    }
    
    item = conteudo.get(tipo, ["ERRO", "Página não encontrada", "#"])
    
    return STYLE + f"""
    <div class="phone-screen">
        <h2 style="color:#CCFF00; font-family:'Orbitron'; margin-top:10px;">{item[0]}</h2>
        <div class="content-card">
            <p>{item[1]}</p>
        </div>
        <a href="{item[2]}" target="_blank" class="wiki-btn">Saber mais (Wikipedia) →</a>
        <a href="/menu" class="btn-login" style="background:none; border:1px solid #CCFF00; color:#CCFF00; margin-top:auto;">VOLTAR AO MENU</a>
    </div>
    """

if __name__ == "__main__":
    if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
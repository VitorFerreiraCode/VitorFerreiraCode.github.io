#!/usr/bin/env python3
# Site pessoal (direção H): PT em index.html e EN em en/index.html, gerados do mesmo modelo.
import hashlib, os, re, sys

RAIZ = sys.argv[1]
# Versão dos arquivos no link: o navegador não mistura HTML novo com CSS/JS antigo do cache.
VERSAO = hashlib.sha1(b"".join(open(os.path.join(RAIZ, "assets", f), "rb").read() for f in ("estilo.css", "main.js"))).hexdigest()[:8]
VEENUX = "https://vnxbot.mivsistemas.com/conheca"
GH = "https://github.com/VitorFerreiraCode"
EMAIL = "vitorferreiraviana@alunos.utfpr.edu.br"
WHATS = "https://wa.me/5512981424603"
WHATS_TXT = "+55 12 98142-4603"
DISCORD = "levitin_"
REPOS = {
    "botia": "https://github.com/VitorFerreiraCode/bot-discord-IA",
    "of1": "https://github.com/VitorFerreiraCode/oficina-cheat-e-anticheat",
    "of2": "https://github.com/VitorFerreiraCode/oficina-malwares",
    "transf": "https://github.com/ProjetoTransformar/projeto-transformar",
    "tcc": "https://github.com/VitorFerreiraCode/tcc-sabermais",
}
VX_SVG = '<svg width="36" height="36" viewBox="0 0 512 512" aria-hidden="true"><circle cx="256" cy="256" r="240" fill="#0B2622"/><path d="M144 258 L226 348 L366 168" fill="none" stroke="#10B981" stroke-width="66" stroke-linecap="round" stroke-linejoin="round"/><circle cx="382" cy="140" r="26" fill="#FF7A59"/></svg>'
SM_SVG = '<svg width="36" height="36" viewBox="0 0 1000 1000" aria-hidden="true"><rect width="1000" height="1000" rx="230" fill="#16A34A"/><path d="M500 265V735M265 500H735" fill="none" stroke="#fff" stroke-width="145" stroke-linecap="round"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
SUN = '<svg class="tema__sol" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 1.5v2.5M12 20v2.5M4.6 4.6l1.8 1.8M17.6 17.6l1.8 1.8M1.5 12H4M20 12h2.5M4.6 19.4l1.8-1.8M17.6 6.4l1.8-1.8"/></svg>'
MOON = '<svg class="tema__lua" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/></svg>'

T = {}
T["pt"] = dict(
    lang="pt-BR", a="", url="https://vitorferreiracode.github.io/",
    title="Vitor Ferreira Viana — Desenvolvedor Full Stack (Java e TypeScript)",
    desc="Desenvolvedor Full Stack (Java e TypeScript) aberto a vagas CLT. Desenvolvedor em empresa, dois produtos próprios no ar, estudante de Sistemas de Informação na UTFPR, fundador da TypeX Empresa Júnior e coordenador da TechWeek 2025.",
    pular="Pular para o conteúdo", inicio="Início", secoes="Seções", idioma="Idioma do site", tema="Alternar tema claro/escuro",
    nav=[("trajetoria", "Trajetória"), ("projetos", "Projetos"), ("formacao", "Formação"), ("sobre", "Sobre mim"), ("contato", "Contato")],
    aberto="Aberto a vagas CLT · remoto ou híbrido no Paraná",
    frases=["Desenvolvedor Full Stack · Java e TypeScript", "Criador do VeenuX Payments e do SaberMais+", "Coordenador da TechWeek 2025", "Fundador da TypeX Empresa Júnior"],
    abertura="Em dois anos, fui de <b>bolsista de pesquisa</b> a <b>desenvolvedor em empresa</b>, com <b>dois produtos meus no ar</b> e uma <b>empresa júnior fundada</b>. Programo, estudo, empreendo e lidero.",
    b_traj="Ver minha trajetória",
    cv="Currículo", idiomas="Idiomas", cv_pt="Português", cv_en="English",
    langs=[("Português", 6, "Nativo"), ("Inglês", 3, "B1 · intermediário"), ("Francês", 3, "B1 · intermediário")],
    pilares=[
        ("prog", "Programador", "Código em produção", ["Java em um sistema usado por empresas", "Dois produtos meus no ar, com usuários", "Pagamentos, IA e painéis"]),
        ("acad", "Acadêmico", "UTFPR e pesquisa", ["Sistemas de Informação", "Bolsista da Fundação Araucária", "TCC que virou produto"]),
        ("empr", "Empreendedor", "Negócios do zero", ["Fundei a TypeX Empresa Júnior", "Mais de R$ 10 mil no 1º ano", "VeenuX com clientes pagantes"]),
        ("lider", "Líder", "Gente e palco", ["Coordenei a TechWeek 2025 (+200)", "Ajudei a organizar a de 2026 (+150)", "Mediei o CFO da LVMH"]),
    ],
    nome_pilar={"prog": "Programador", "acad": "Acadêmico", "empr": "Empreendedor", "lider": "Líder"},
    traj="Trajetória", hoje="hoje",
    traj_itens=[
        ("hoje", [
            (["prog"], "Desenvolvedor de software na Axdoc", "Desenvolvo e mantenho, em time, um sistema de gestão eletrônica de documentos em Java usado por empresas. Também gravo os tutoriais em vídeo do produto."),
            (["prog", "empr"], "VeenuX Payments no ar, com clientes", "Plataforma em que coaches vendem aulas dentro do Discord. Cuido de tudo sozinho: produto, código, cobrança e suporte."),
            (["lider"], "TechWeek 2026 · +150 estudantes", "Ajudei na organização e nas decisões do evento e ministrei duas oficinas de segurança da informação."),
        ]),
        ("2025", [
            (["empr", "lider"], "Fundei e presidi a TypeX Empresa Júnior", "45 membros e 7 diretores, mais de R$ 10 mil faturados no primeiro ano e os prêmios EJ Iniciativa (Vértice 2025) e EJ Aspirante (Vendaval 2025)."),
            (["lider"], "Coordenei a TechWeek 2025 · +200 estudantes", "Liderei a equipe de organização, trouxe palestrantes, fechei patrocínios e parcerias e montei a programação e a divulgação. Mediei a palestra de Julien Decultot, CFO da LVMH."),
            (["acad", "prog"], "SaberMais+, meu TCC, vira produto", "Plataforma de ensino que entende como cada aluno estuda e ajuda o professor a se adaptar à turma."),
            (["prog"], "Hackathon da Via do Leite · 4º lugar", "Solução construída em equipe, sob pressão de tempo."),
            (["prog"], "Primeiros trabalhos como desenvolvedor", "Sistemas web e sites para clientes na TriXX Software e na DNS Agência, em trabalho remoto."),
        ]),
        ("2024", [
            (["acad"], "Bolsista de pesquisa da Fundação Araucária", "Projeto Transformar: aparelhos apreendidos pela Receita Federal viraram computadores para escolas sem recursos."),
            (["prog"], "HackLab 2024 · 4º lugar", "Primeira competição de programação em equipe."),
        ]),
    ],
    proj="Projetos", proj_intro="Os dois produtos que construí sozinho e que estão no ar, e o código que deixo aberto.",
    vx_et="No ar · clientes reais", vx_p="Coaches de e-sports vendem aulas dentro do Discord: loja com Pix e cartão, agenda com lembretes e remarcação, área do aluno e suporte com IA. Virou um negócio, com teste grátis e cobrança mensal.",
    vx_alt="Loja do VeenuX Payments no Discord: pacote de aulas, botão Pagar com Pix, pagamento aprovado e escolha de horário",
    vx_cta="Conhecer o produto",
    dep_tit="O que dizem os clientes",
    deps=[
        ("Também quero destacar o trabalho do Vitor, meu aluno e desenvolvedor do bot. É muito gratificante ver a dedicação dele e a qualidade do projeto.", "Neitan", "Coach profissional de Rocket League"),
        ("Eu não entendo nada de bots e integrações do Discord, então eu só dava as ideias e ele implementava dando sugestões pra melhorar mais ainda. Recomendo demais, pode confiar!", "xPuurga", "Coach de Rocket League, servidor com 3.400 membros"),
    ],
    sm_et="Meu TCC · no ar", sm_p="Plataforma de ensino que descobre como cada aluno estuda, monta um plano para ele e mostra ao professor onde a turma precisa de ajuda, com sugestões de como ensinar. Pronta para várias escolas e faculdades.",
    sm_alt="Visão do professor no SaberMais+: perfil de estudo da turma por categoria e sugestões de como ensinar",
    sm_cta="Pedir uma demonstração", sm_nota="Código privado.",
    aberto_tit="Código aberto", aberto_intro="Para quem quer ver como eu programo e explico.",
    repos=[
        ("botia", "Bot que monta servidores com IA", "Você descreve o servidor do Discord e a IA cria canais, cargos e permissões."),
        ("of1", "Oficina: cheats vs anticheats", "Slides e materiais da oficina que dei na TechWeek 2026."),
        ("of2", "Oficina: malwares", "Como ameaças agem no Windows e como são barradas. Educacional e defensivo."),
        ("transf", "Projeto Transformar", "O projeto de pesquisa que transformou aparelhos apreendidos em computadores."),
        ("tcc", "TCC SaberMais+", "Planejamento e escrita do meu TCC, abertos."),
    ],
    ver_codigo="Ver no GitHub",
    form="Formação", ferr="Ferramentas",
    utf_t="Sistemas de Informação · UTFPR", utf_s="Câmpus Francisco Beltrão · previsão de formatura: 2º semestre de 2028",
    utf_li=["Bolsista de pesquisa da Fundação Araucária (2024 – 2026)", "TCC: SaberMais+, plataforma de ensino em produção", "Duas oficinas de segurança ministradas na TechWeek 2026", "4º lugar no HackLab 2024 e no Hackathon da Via do Leite 2025"],
    cursos_t="Cursos",
    cursos=[("Metodologias Ágeis", "Workshop com Adenilson, coordenador de suporte da Cresol."), ("ExponencIA", "Curso de IA de Tulio Bittencourt: harness, agents e skills.")],
    st=[("Linguagens", ["Java", "TypeScript", "JavaScript", "SQL", "PHP"]), ("Web", ["Next.js", "React", "NestJS", "Node.js", "Laravel"]), ("Dados", ["PostgreSQL", "MySQL", "Prisma"]), ("Entrega", ["Git e GitHub", "Docker", "Testes automatizados", "Deploy em nuvem"]), ("Também", ["IA e agentes", "Pagamentos (Pix, Mercado Pago)", "Discord"])],
    time="Como eu trabalho em time",
    time_cards=[
        ("Comunicação clara", "Pergunto antes de codar, aviso cedo quando algo trava e deixo as decisões registradas para o time."),
        ("Qualidade de verdade", "Testo e reviso o que entrego antes de subir. Erro corrigido vira teste, para não voltar."),
        ("Autonomia com responsabilidade", "Já levei produtos inteiros do zero ao ar sozinho. No time, assumo a minha parte até o fim."),
        ("IA a favor do time", "Uso agentes de IA com método para ganhar velocidade, sem abrir mão de entender e revisar o que vai para produção."),
    ],
    sobre="Sobre mim",
    sobre_p="Sou o Vitor, de Francisco Beltrão, no Paraná. Sou movido por desafios e pela vontade de construir coisas que gerem <b>impacto real</b>, e acredito na <b>colaboração</b> e na <b>liderança com propósito</b>. Fora do código, estudo matemática, história, política e filosofia, leio bastante e vivo criando mods e plugins para jogos.",
    cont="Contato", cont_intro="Procurando alguém para o seu time? Fale comigo pelo canal que preferir. Respondo com o currículo e o que mais você precisar.",
    copiar="Copiar usuário do Discord", copiado="copiado!",
    rodape="Feito à mão, sem framework.",
)

T["en"] = dict(
    lang="en", a="../", url="https://vitorferreiracode.github.io/en/",
    title="Vitor Ferreira Viana — Full Stack Developer (Java and TypeScript)",
    desc="Full Stack Developer (Java and TypeScript) open to full-time roles. Developer at a software company, two products of my own in production, Information Systems student at UTFPR (Brazil), founder of TypeX Junior Enterprise and TechWeek 2025 coordinator.",
    pular="Skip to content", inicio="Home", secoes="Sections", idioma="Site language", tema="Toggle light/dark theme",
    nav=[("trajetoria", "Journey"), ("projetos", "Projects"), ("formacao", "Education"), ("sobre", "About"), ("contato", "Contact")],
    aberto="Open to full-time roles · remote in Brazil or hybrid in Paraná",
    frases=["Full Stack Developer · Java and TypeScript", "Creator of VeenuX Payments and SaberMais+", "TechWeek 2025 coordinator", "Founder of TypeX Junior Enterprise"],
    abertura="In two years, I went from <b>research scholarship student</b> to <b>developer at a company</b>, with <b>two products of my own in production</b> and a <b>junior enterprise I founded</b>. I code, study, build businesses and lead.",
    b_traj="See my journey",
    cv="Resume", idiomas="Languages", cv_pt="Português", cv_en="English",
    langs=[("Portuguese", 6, "Native"), ("English", 3, "B1 · intermediate"), ("French", 3, "B1 · intermediate")],
    pilares=[
        ("prog", "Developer", "Code in production", ["Java on a system used by companies", "Two products of my own, live with users", "Payments, AI and dashboards"]),
        ("acad", "Academic", "UTFPR and research", ["Information Systems degree", "Fundação Araucária research scholarship", "Capstone project that became a product"]),
        ("empr", "Entrepreneur", "Businesses from scratch", ["Founded TypeX Junior Enterprise", "Over BRL 10,000 in year one", "VeenuX with paying customers"]),
        ("lider", "Leader", "People and stage", ["Coordinated TechWeek 2025 (200+)", "Helped organize the 2026 edition (150+)", "Moderated LVMH’s CFO on stage"]),
    ],
    nome_pilar={"prog": "Developer", "acad": "Academic", "empr": "Entrepreneur", "lider": "Leader"},
    traj="Journey", hoje="today",
    traj_itens=[
        ("today", [
            (["prog"], "Software developer at Axdoc", "I develop and maintain, as part of a team, a Java electronic document management system used by companies. I also record the product’s video tutorials."),
            (["prog", "empr"], "VeenuX Payments live, with customers", "A platform where coaches sell lessons right inside Discord. I handle everything myself: product, code, billing and support."),
            (["lider"], "TechWeek 2026 · 150+ students", "Helped with the event’s organization and decisions, and taught two information security workshops."),
        ]),
        ("2025", [
            (["empr", "lider"], "Founded and led TypeX Junior Enterprise", "45 members and 7 directors, over BRL 10,000 in revenue in the first year, and the EJ Iniciativa (Vértice 2025) and EJ Aspirante (Vendaval 2025) awards."),
            (["lider"], "Coordinated TechWeek 2025 · 200+ students", "Led the organizing team, brought in speakers, closed sponsorships and partnerships, and put together the schedule and promotion. Moderated the talk by Julien Decultot, CFO of LVMH."),
            (["acad", "prog"], "SaberMais+, my capstone, becomes a product", "A learning platform that understands how each student studies and helps teachers adapt to their class."),
            (["prog"], "Via do Leite Hackathon · 4th place", "A solution built as a team, under time pressure."),
            (["prog"], "First jobs as a developer", "Web systems and websites for clients at TriXX Software and DNS Agência, working remotely."),
        ]),
        ("2024", [
            (["acad"], "Fundação Araucária research scholarship", "Projeto Transformar: devices seized by Brazil’s Federal Revenue Service became computers for under-resourced schools."),
            (["prog"], "HackLab 2024 · 4th place", "My first team programming competition."),
        ]),
    ],
    proj="Projects", proj_intro="The two products I built on my own that are live today, and the code I keep open.",
    vx_et="Live · real customers", vx_p="E-sports coaches sell lessons inside Discord: a store with Pix and cards, scheduling with reminders and rescheduling, a student area and AI support. It became a business, with a free trial and monthly billing.",
    vx_alt="VeenuX Payments store in Discord: lesson package, Pay with Pix button, approved payment and time slot selection",
    vx_cta="See the product",
    dep_tit="What customers say",
    deps=[
        ("I also want to highlight the work of Vitor, my student and the bot’s developer. It’s very rewarding to see his dedication and the quality of the project.", "Neitan", "Professional Rocket League coach"),
        ("I don’t understand anything about Discord bots and integrations, so I just gave the ideas and he built them, suggesting ways to make them even better. Highly recommended, you can trust him!", "xPuurga", "Rocket League coach, 3,400-member server"),
    ],
    sm_et="My capstone · live", sm_p="A learning platform that finds out how each student studies, builds a study plan for them and shows teachers where the class needs help, with suggestions on how to teach. Ready for many schools and universities.",
    sm_alt="Teacher view in SaberMais+: class study profile by category and teaching suggestions",
    sm_cta="Request a demo", sm_nota="Private code.",
    aberto_tit="Open source", aberto_intro="For anyone who wants to see how I code and explain.",
    repos=[
        ("botia", "Bot that builds servers with AI", "You describe the Discord server and the AI creates the channels, roles and permissions."),
        ("of1", "Workshop: cheats vs anti-cheats", "Slides and materials from the workshop I taught at TechWeek 2026."),
        ("of2", "Workshop: malware", "How threats act on Windows and how they are stopped. Educational and defensive."),
        ("transf", "Projeto Transformar", "The research project that turned seized devices into computers."),
        ("tcc", "SaberMais+ capstone", "Planning and writing of my capstone, in the open."),
    ],
    ver_codigo="View on GitHub",
    form="Education", ferr="Tools",
    utf_t="Information Systems · UTFPR", utf_s="Francisco Beltrão campus, Brazil · expected graduation: second half of 2028",
    utf_li=["Fundação Araucária research scholarship (2024 – 2026)", "Capstone: SaberMais+, a learning platform in production", "Taught two security workshops at TechWeek 2026", "4th place at HackLab 2024 and at the Via do Leite Hackathon 2025"],
    cursos_t="Courses",
    cursos=[("Agile Methodologies", "Workshop with Adenilson, support coordinator at Cresol."), ("ExponencIA", "AI course by Tulio Bittencourt: harnesses, agents and skills.")],
    st=[("Languages", ["Java", "TypeScript", "JavaScript", "SQL", "PHP"]), ("Web", ["Next.js", "React", "NestJS", "Node.js", "Laravel"]), ("Data", ["PostgreSQL", "MySQL", "Prisma"]), ("Delivery", ["Git and GitHub", "Docker", "Automated tests", "Cloud deployment"]), ("Also", ["AI and agents", "Payments (Pix, Mercado Pago)", "Discord"])],
    time="How I work in a team",
    time_cards=[
        ("Clear communication", "I ask before coding, flag blockers early and keep decisions written down for the team."),
        ("Real quality", "I test and review what I deliver before shipping. Every bug fixed becomes a test so it doesn’t come back."),
        ("Autonomy with responsibility", "I’ve taken whole products from zero to production on my own. In a team, I own my part to the end."),
        ("AI working for the team", "I use AI agents with a method to move faster, without giving up understanding and reviewing what goes to production."),
    ],
    sobre="About me",
    sobre_p="I’m Vitor, from Francisco Beltrão, in Paraná, Brazil. I’m driven by challenges and by the will to build things with <b>real impact</b>, and I believe in <b>collaboration</b> and <b>purpose-driven leadership</b>. Outside of code, I study math, history, politics and philosophy, read a lot and keep building mods and plugins for games.",
    cont="Contact", cont_intro="Looking for someone for your team? Reach me on whichever channel you prefer. I’ll reply with my resume and anything else you need.",
    copiar="Copy Discord username", copiado="copied!",
    rodape="Handmade, no framework.",
)


def chips(xs):
    return '<div class="chips">' + "".join(f"<span>{x}</span>" for x in xs) + "</div>"


def citacao(caminho):
    s = open(caminho, encoding="utf-8").read()
    m = re.search(r'<figure class="citacao citacao--abertura">.*?</figure>', s, re.S)
    return m.group(0)


def pagina(c, cit):
    a = c["a"]
    idioma = (
        f'<a href="{"./" if a == "" else "../"}"{" aria-current=\"page\"" if a == "" else ""} lang="pt-BR">PT</a>'
        f'<a href="{"en/" if a == "" else "./"}"{" aria-current=\"page\"" if a != "" else ""} lang="en">EN</a>'
    )
    nav = "\n".join(f'        <a href="#{h}">{t}</a>' for h, t in c["nav"])
    frases = "[" + ",".join(f'"{f}"' for f in c["frases"]) + "]"
    langs = "\n".join(
        f'            <li><span class="idiomas__nome">{n}</span><span class="nivel-barra" data-n="{k}" aria-hidden="true">' + "<i></i>" * 6 + f'</span><span class="idiomas__nivel">{v}</span></li>'
        for n, k, v in c["langs"]
    )
    pilares = "\n".join(
        f'          <article class="pilar pilar--{k}"><p class="pilar__nome">{n}</p><h3>{t}</h3><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></article>"
        for k, n, t, li in c["pilares"]
    )

    def tags(ks):
        return '<div class="tags">' + "".join(f'<span class="tag tag--{k}">{c["nome_pilar"][k]}</span>' for k in ks) + "</div>"

    linha = ""
    for i, (ano, itens) in enumerate(c["traj_itens"]):
        ultimo = i == len(c["traj_itens"]) - 1
        cards = "\n".join(f'              <article class="marco">{tags(ks)}<h3>{t}</h3><p>{p}</p></article>' for ks, t, p in itens)
        linha += (
            f'          <div class="linha__ano{" linha__ano--agora" if i == 0 else ""}">{ano}</div>\n'
            f'          <div class="linha__trilho{" linha__trilho--fim" if ultimo else ""}" aria-hidden="true"><i></i></div>\n'
            f'          <div class="linha__itens{" linha__itens--duas" if len(itens) > 3 else ""}">\n{cards}\n          </div>\n'
        )
    deps = "\n".join(
        f'              <figure class="depoimento"><blockquote>“{q}”</blockquote><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>'
        for q, n, r in c["deps"]
    )
    repos = "\n".join(
        f'          <a class="repo" href="{REPOS[k]}" target="_blank" rel="noopener noreferrer"><b>{t} <span aria-hidden="true">↗</span></b><span>{d}</span></a>'
        for k, t, d in c["repos"]
    )
    utf = "".join(f"<li>{x}</li>" for x in c["utf_li"])
    cursos = "\n".join(f'            <li><b>{t}</b><span>{d}</span></li>' for t, d in c["cursos"])
    stack = "\n".join(f"            <div><h4>{t}</h4>{chips(xs)}</div>" for t, xs in c["st"])
    time = "\n".join(f'          <article class="cartao"><h3>{t}</h3><p>{x}</p></article>' for t, x in c["time_cards"])

    return f"""<!doctype html>
<html lang="{c['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']}</title>
  <meta name="description" content="{c['desc']}">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{c['url']}">
  <meta name="theme-color" content="#0b1120">
  <link rel="alternate" hreflang="pt-BR" href="https://vitorferreiracode.github.io/">
  <link rel="alternate" hreflang="en" href="https://vitorferreiracode.github.io/en/">
  <link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&family=Lora:ital@1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{a}assets/estilo.css?v={VERSAO}">
  <script>
    try {{ const t = localStorage.getItem('tema'); if (t) document.documentElement.dataset.tema = t; }} catch (e) {{}}
  </script>
</head>
<body>
  <a class="pular" href="#conteudo">{c['pular']}</a>
  <div class="fundo-vivo" aria-hidden="true"><i></i><i></i><i></i></div>

  <header class="topo">
    <div class="largura topo__linha">
      <a class="logo" href="#inicio" aria-label="{c['inicio']}">
        <span class="logo__marca">VF</span><span class="logo__nome">VitorFerreira<span>Code</span></span>
      </a>
      <nav class="menu" aria-label="{c['secoes']}">
{nav}
      </nav>
      <div class="idioma-site" aria-label="{c['idioma']}">{idioma}</div>
      <button class="tema" type="button" aria-label="{c['tema']}">
        {SUN}
        {MOON}
      </button>
    </div>
  </header>

  <main id="conteudo">
    <!-- TOPO -->
    <section class="hero hero--h" id="inicio">
      <div class="largura">
        <p class="sobretitulo"><span class="ponto"></span> {c['aberto']}</p>
        <h1>Vitor Ferreira Viana</h1>
        <p class="hero__papel">
          <span class="mono">&gt;</span> <span class="digitando" data-frases='{frases}'>{c['frases'][0]}</span><span class="cursor" aria-hidden="true">_</span>
        </p>
        <p class="hero__texto">{c['abertura']}</p>
        <div class="acoes">
          <a class="botao botao--forte" href="#trajetoria">{c['b_traj']}</a>
          <a class="botao" href="{WHATS}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
          <a class="botao" href="{GH}" target="_blank" rel="noopener noreferrer">GitHub</a>
        </div>
      </div>
    </section>

    <!-- CURRÍCULO E IDIOMAS -->
    <section class="faixa-cv" id="curriculo">
      <div class="largura faixa-cv__grade">
        <div class="faixa-cv__bloco">
          <h2 class="faixa-cv__titulo">{c['cv']}</h2>
          <div class="faixa-cv__botoes">
            <a class="cv" href="{a}assets/curriculo/curriculo-vitor-ferreira-viana-pt.pdf" target="_blank" rel="noopener noreferrer"><span class="cv__sigla">PT</span><span>{c['cv_pt']}</span>{DOWN}</a>
            <a class="cv" href="{a}assets/curriculo/resume-vitor-ferreira-viana-en.pdf" target="_blank" rel="noopener noreferrer"><span class="cv__sigla">EN</span><span>{c['cv_en']}</span>{DOWN}</a>
          </div>
        </div>
        <div class="faixa-cv__bloco">
          <h2 class="faixa-cv__titulo">{c['idiomas']}</h2>
          <ul class="idiomas">
{langs}
          </ul>
        </div>
      </div>
    </section>

    <!-- PILARES -->
    <section class="secao secao--fina" id="pilares">
      <div class="largura pilares">
{pilares}
      </div>
    </section>

    <!-- TRAJETÓRIA -->
    <section class="secao" id="trajetoria">
      <div class="largura">
        <h2 class="titulo"><span class="mono">01.</span> {c['traj']}</h2>
        <div class="linha">
{linha}        </div>
      </div>
    </section>

    <!-- PROJETOS -->
    <section class="secao secao--alt" id="projetos">
      <div class="largura">
        <h2 class="titulo"><span class="mono">02.</span> {c['proj']}</h2>
        <p class="intro">{c['proj_intro']}</p>
        <div class="produtos">
          <article class="produto">
            <img class="produto__print" src="{a}assets/projetos/print-veenux.jpg" alt="{c['vx_alt']}" width="1050" height="852" loading="lazy">
            <div class="produto__corpo">
              <p class="etiqueta">{c['vx_et']}</p>
              <h3 class="caso__marca">{VX_SVG}VeenuX Payments</h3>
              <p>{c['vx_p']}</p>
              <a class="link" href="{VEENUX}" target="_blank" rel="noopener noreferrer">{c['vx_cta']} <span aria-hidden="true">↗</span></a>
              <p class="depoimentos__titulo">{c['dep_tit']}</p>
{deps}
            </div>
          </article>
          <article class="produto">
            <img class="produto__print" src="{a}assets/projetos/print-sabermais.jpg" alt="{c['sm_alt']}" width="1656" height="1496" loading="lazy">
            <div class="produto__corpo">
              <p class="etiqueta">{c['sm_et']}</p>
              <h3 class="caso__marca">{SM_SVG}SaberMais+</h3>
              <p>{c['sm_p']}</p>
              <a class="link" href="#contato">{c['sm_cta']} <span aria-hidden="true">→</span></a>
              <p class="privado">{c['sm_nota']}</p>
            </div>
          </article>
        </div>
        <h3 class="trabalho__anteriores">{c['aberto_tit']}</h3>
        <p class="intro">{c['aberto_intro']}</p>
        <div class="repos">
{repos}
        </div>
      </div>
    </section>

    <!-- FORMAÇÃO E FERRAMENTAS -->
    <section class="secao" id="formacao">
      <div class="largura duas">
        <div>
          <h2 class="titulo"><span class="mono">03.</span> {c['form']}</h2>
          <article class="cartao formacao">
            <h3>{c['utf_t']}</h3>
            <p class="formacao__sub">{c['utf_s']}</p>
            <ul class="lista-check">{utf}</ul>
          </article>
          <h3 class="trabalho__anteriores">{c['cursos_t']}</h3>
          <ul class="trajetoria">
{cursos}
          </ul>
        </div>
        <div>
          <h2 class="titulo"><span class="mono">04.</span> {c['ferr']}</h2>
          <div class="stack">
{stack}
          </div>
        </div>
      </div>
    </section>

    <!-- EM TIME -->
    <section class="secao secao--alt" id="time">
      <div class="largura">
        <h2 class="titulo"><span class="mono">05.</span> {c['time']}</h2>
        <div class="cartoes cartoes--2 principios">
{time}
        </div>
      </div>
    </section>

    <!-- SOBRE MIM -->
    <section class="secao" id="sobre">
      <div class="largura sobre">
        <h2 class="titulo"><span class="mono">06.</span> {c['sobre']}</h2>
        <div class="sobre__texto">
          {cit}
          <p>{c['sobre_p']}</p>
        </div>
      </div>
    </section>

    <!-- CONTATO -->
    <section class="secao contato" id="contato">
      <div class="largura">
        <h2 class="titulo"><span class="mono">07.</span> {c['cont']}</h2>
        <p class="intro">{c['cont_intro']}</p>
        <div class="contatos">
          <a class="contato-item" href="mailto:{EMAIL}"><b>E-mail</b><span>{EMAIL}</span></a>
          <a class="contato-item" href="{WHATS}" target="_blank" rel="noopener noreferrer"><b>WhatsApp</b><span>{WHATS_TXT}</span></a>
          <button class="contato-item" type="button" data-copiar="{DISCORD}" data-copiado="{c['copiado']}" aria-label="{c['copiar']}"><b>Discord</b><span>{DISCORD}</span></button>
          <a class="contato-item" href="{GH}" target="_blank" rel="noopener noreferrer"><b>GitHub</b><span>VitorFerreiraCode</span></a>
        </div>
      </div>
    </section>
  </main>

  <footer class="rodape">
    <div class="largura">© <span id="ano">2026</span> Vitor Ferreira Viana · {c['rodape']}</div>
  </footer>

  <script src="{a}assets/main.js?v={VERSAO}" defer></script>
</body>
</html>
"""


for chave, arq in [("pt", "index.html"), ("en", "en/index.html")]:
    caminho = os.path.join(RAIZ, arq)
    html = pagina(T[chave], citacao(caminho))
    open(caminho, "w", encoding="utf-8").write(html)
    print("gerado", arq)

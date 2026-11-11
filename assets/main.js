// Tema claro/escuro (lembra a escolha) e efeito de digitação no topo.
(function () {
  const raiz = document.documentElement;
  const botao = document.querySelector('.tema');
  const escuroSistema = () => window.matchMedia('(prefers-color-scheme: dark)').matches;
  const atual = () => raiz.dataset.tema || (escuroSistema() ? 'escuro' : 'claro');
  botao?.addEventListener('click', () => {
    const novo = atual() === 'escuro' ? 'claro' : 'escuro';
    raiz.dataset.tema = novo;
    try { localStorage.setItem('tema', novo); } catch (e) {}
  });

  const ano = document.getElementById('ano');
  if (ano) ano.textContent = new Date().getFullYear();

  const alvo = document.querySelector('.digitando');
  const calmo = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!alvo || calmo) return;
  let frases = [];
  try { frases = JSON.parse(alvo.dataset.frases); } catch (e) { return; }
  let i = 0, n = frases[0].length, apagando = true;
  function passo() {
    const frase = frases[i];
    n += apagando ? -1 : 1;
    alvo.textContent = frase.slice(0, n);
    let espera = apagando ? 28 : 55;
    if (!apagando && n === frase.length) { apagando = true; espera = 2200; }
    else if (apagando && n === 0) { apagando = false; i = (i + 1) % frases.length; espera = 350; }
    setTimeout(passo, espera);
  }
  setTimeout(passo, 2400);
})();

// Botões que copiam um texto (ex.: usuário do Discord) e confirmam na própria etiqueta.
document.querySelectorAll('[data-copiar]').forEach((botao) => {
  botao.addEventListener('click', () => {
    const alvo = botao.querySelector('span');
    const original = alvo ? alvo.textContent : '';
    navigator.clipboard?.writeText(botao.dataset.copiar).then(() => {
      if (!alvo) return;
      alvo.textContent = botao.dataset.copiado || 'copiado!';
      setTimeout(() => { alvo.textContent = original; }, 1500);
    }).catch(() => {});
  });
});

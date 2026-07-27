# 📖 Alura Album - Universo Geek

O **Alura Album** é uma aplicação web interativa desenvolvida no formato de álbum virtual de figurinhas, homenageando os maiores mundos, ícones e mentes criativas da cultura nerd e geek que moldam a nossa imaginação.

---

## 🎯 Objetivo do Projeto

O principal objetivo deste projeto é proporcionar uma experiência imersiva e interativa aos usuários, permitindo que naveguem por um livro digital tridimensional e "colem" figurinhas virtuais de lendas da cultura nerd. O projeto está estruturado em categorias que cobrem:
* **Ficção Científica (Sci-Fi)**: Ícones lendários como Spock, Darth Vader, Neo, Marty McFly e Doctor Who.
* **Quadrinhos (HQs)**: Criadores como Stan Lee e Alan Moore, e super-heróis marcantes como Batman, Homem-Aranha e Superman.
* **Games & RPG**: Criadores visionários como Shigeru Miyamoto, Gary Gygax (D&D), Hideo Kojima, e personagens marcantes como Mario e Geralt de Rívia.
* **Fantasia Medieval**: Mestres como J.R.R. Tolkien e George R.R. Martin, e heróis como Harry Potter, Jon Snow e Gandalf.
* **Animes e Mangás**: Lendas da animação e mangá como Akira Toriyama (Goku) e Hayao Miyazaki, além de ídolos como Naruto e Luffy.
* **Cultura Geek Brasil**: Celebridades que movimentam a cena geek brasileira como Jovem Nerd, Azaghal, Affonso Solano, e Leon & Nilce.

---

## 📂 Arquivos do Projeto e Suas Funcionalidades

### 1. `index.html`
Define a estrutura semântica da aplicação e do álbum de fotos. 
* Contém a marcação de todas as páginas do livro (capa dura com tema Geek/Nerd, páginas internas temáticas com slots para as figurinhas `#01` a `#30` e contracapa).
* Carrega a biblioteca de paginação tridimensional `St.PageFlip` a partir de uma CDN para habilitar o efeito de transição física das páginas.
* Habilita botões táteis de controle de som e navegação lateral.

### 2. `style.css`
Aplica a identidade visual e o design premium e futurista da aplicação.
* **Estética Cyber/Tech**: Utiliza paletas de cores baseadas em azul cósmico, gradientes suaves e temas escuros de alta fidelidade visual.
* **Efeitos de Profundidade**: Aplica degradês de sombreamento dinâmicos (`::after`) no centro do livro para simular com realismo a lombada física das páginas abertas.
* **Animações Fluidas**: Inclui efeitos visuais modernos como o efeito *glitch* de texto na capa, cards flutuantes dinâmicos com rotação física e animação suave ao "colar" figurinhas nos slots vazios.

### 3. `app.js`
Responsável pela inteligência, dinâmica interativa e integração com dados externos.
* **Integração com API (`preencherFigurinhas`)**: Realiza uma requisição assíncrona ao servidor backend local (`http://localhost:8000/figurinhas`) para carregar a lista de imagens e informações das figurinhas de forma dinâmica.
* **Controle de Arraste e Gestos**: Intercepta eventos de toque (`touchstart`/`touchmove`) e mouse (`mousedown`/`mousemove`) nas extremidades do álbum para permitir folhear o álbum arrastando-o manualmente.
* **Sintetização de Áudio (Web Audio API)**: Cria efeitos sonoros dinâmicos de vento e fricção de papel físico (folheamento) gerados inteiramente por programação (ruído branco associado a varreduras de filtro de frequência passa-faixa), dispensando a necessidade de arquivos pesados de áudio externos.
* **Navegação Inteligente**: Configura suporte a teclas de setas do teclado e controla a ocultação dos botões de controle nas páginas limites (capa e contracapa).

---

## 🚀 Como Executar o Projeto

1. Certifique-se de que a API de figurinhas (backend) esteja ativa no endereço padrão (`http://localhost:8000`).
2. Abra o arquivo `index.html` diretamente em seu navegador favorito ou utilize uma extensão de servidor local (como *Live Server* no VS Code).
3. Habilite o som pelo controle no canto superior direito para desfrutar da experiência auditiva de virada de páginas sintetizada!

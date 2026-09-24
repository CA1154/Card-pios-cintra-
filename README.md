# Gerador de Cardápios · Cintra Eventos

Página para montar cardápios personalizados com a identidade da Cintra Eventos (logo, cores e fontes) e baixar em PDF para enviar ao cliente.

## Como usar

1. Acesse **https://ca1154.github.io/Card-pios-cintra-/** (ou abra `index.html` no navegador) (Chrome, Edge ou Safari). É preciso ter internet, porque as fontes e o gerador de PDF são carregados online.
2. Escolha a **modalidade** principal: Churrasco, Comida de Boteco, Jantar Convencional ou Cardápio Especial (montado do zero). Em **Combinar com outra modalidade**, dá para juntar outras no mesmo cardápio. Com **Como sugestão** ligado, a modalidade extra aparece no PDF como "Sugestão para complementar", com valor próprio se quiser. Desligado, ela entra no título como parte do cardápio (ex.: "Churrasco & Comida de Boteco").
3. Preencha **cliente e evento**. Um campo deixado em branco ou marcado como **A definir** aparece no PDF como "A definir".
4. Em **Itens do cardápio**, toque num item para colocar ou tirar do cardápio:
   - azul-marinho: está no cardápio;
   - contorno simples: item que a Cintra já serve, fora deste cardápio;
   - contorno tracejado com a etiqueta *sugestão*: ideia nova para variar o cardápio.
   Dá para adicionar itens e variações. O que você adicionar fica guardado para os próximos cardápios (toque no × para esquecer um item). Também dá para ligar e desligar seções, renomear, editar a observação (ex.: "Escolher 3 opções") e criar seções novas.
5. Defina o **valor** (total, por pessoa, a combinar ou sem valor), as informações gerais e as observações.
6. Clique em **Baixar PDF**.

**Salvar** guarda o cardápio neste navegador. Para reabrir, use **Meus cardápios**. Os dados da empresa (nome, telefone, e-mail, site) ficam em **Dados da empresa**, no fim do formulário.

## Para desenvolvedores

- O código-fonte fica em `src/cardapio.html` e o catálogo de itens na constante `CAT`.
- `python3 build.py` (precisa do Pillow) embute `logo.png` e `talheres.png` e gera:
  - `index.html`: página completa para abrir direto no navegador;
  - `artifact.html`: a mesma página, sem o cabeçalho HTML, para publicar como Artifact do Claude.
- O PDF é gerado no próprio navegador com html2canvas + jsPDF, uma imagem A4 por página.

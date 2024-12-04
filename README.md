# Questões teoricas

1- Explique a diferença entre Selenium IDE e Selenium WebDriver
A ferramenta Selenium IDE é um ambiente de desenvolvimento integrado e é
executada como extensão de navegador e rastreia os clicks do usuário para realizar
o teste. O Selenium WebDriver é uma biblioteca utilizada em linguagens de
programação para fazer testes, utilizada em diversos navegadores.
2- Quais são os principais tipos de localizadores (locators) usados no
Selenium WebDriver para encontrar elementos na página? Explique dois
deles.
O Selenium WebDriver utiliza o localizador XPAth que procura o caminho na página
a partir da linguagem XPath e pode ser localizado a partir do inspecionar e por ID
que localiza o ID estabelecido no HTML.
3- O que é um WebElement no Selenium? Dê um exemplo de como interagir
com um WebElement usando Python.
São comandos que interagem com o site a partir do código selenium. o WebElement
element.click() é um comando em python utilizado para clicar no elemento
estabelecido.
4- No Selenium WebDriver, o que acontece se você tentar interagir com um
elemento que ainda não está visível ou carregado na página? Qual comando
você usaria para resolver isso?
O Selenium WebDriver indica que o elemento não foi encontrado. É possível utilizar
o WebElement time.sleep() para esperar a página estar completamente carregada.
5- Cite duas limitações do Selenium IDE que podem levar à escolha do
Selenium WebDriver em projetos maiores.
O Selenium IDE depende das versões dos navegadores, sendo mais suscetível a falhas de
instalação e não suporta testes mais complexos e que precisam de especificações,
utilizadas na linguagem de programação no webdrive

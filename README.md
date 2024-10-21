Scripts de Análise de Dados para Artigo Científico sobre Empregabilidade no Setor de Tecnologia da Informação
Este repositório contém os scripts desenvolvidos para a análise de dados utilizada no artigo científico que examina as dinâmicas de empregabilidade no setor de Tecnologia da Informação em Foz do Iguaçu, utilizando a base de dados RAIS (Registro Anual de Informações Sociais). O objetivo principal é identificar padrões, tendências e transformações no mercado de trabalho ao longo do tempo, com ênfase nas ocupações relacionadas à Tecnologia da Informação.

Conteúdo do Repositório
Este repositório contém os seguintes arquivos e scripts:

1. analise_estatistica_descritiva.R
Script em R utilizado para abrir o arquivo RAIS_SubClasse.csv, calcular as médias e medianas das subcategorias relacionadas à Tecnologia da Informação, e gerar gráficos de linha para visualizar a evolução desses dados ao longo dos anos.
Técnicas de estatística descritiva foram aplicadas para identificar padrões de empregabilidade ao longo da série histórica de 2002 a 2023.
2. histograma_vinculos_empregaticios.R
Este script cria um histograma para mostrar a distribuição dos vínculos empregatícios nas subcategorias do setor de TI.
Utiliza as bibliotecas Pandas, Matplotlib (ou Plotly para uma versão interativa).
Requisitos
Para rodar os scripts incluídos neste repositório, você precisará ter instalado:

R e as seguintes bibliotecas:
dplyr
ggplot2
tidyr
Alternativamente, para scripts em Python:
Python 3.x
Bibliotecas:
pandas
matplotlib
plotly (opcional para gráficos interativos)
Como Utilizar
Baixar o Repositório:

Clone este repositório em sua máquina local usando o seguinte comando:
git clone https://github.com/seuusuario/seurepositorio.git
Rodar os Scripts:

Abra os scripts em seu ambiente de desenvolvimento preferido (RStudio para scripts em R, Jupyter Notebook ou IDE de Python para scripts em Python).
Certifique-se de ajustar os caminhos de arquivos, caso necessário, conforme a estrutura do seu ambiente.
Modificações e Contribuições:

Fique à vontade para modificar os scripts ou contribuir com melhorias. Sugestões e pull requests são bem-vindos!
Dados
Os dados utilizados nos scripts são baseados na base de dados RAIS, extraída do portal BGCAGED (https://bi.mte.gov.br/bgcaged/). O arquivo principal analisado (RAIS_SubClasse.csv) contém informações de vínculos empregatícios agrupados por subclasse da CNAE 2.0, abrangendo o período de 2002 a 2023.

Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Contato
Para mais informações, entre em contato via email: flavio.monteiro@acad.ufsm.br ou abra uma issue neste repositório.

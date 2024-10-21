import pandas as pd
import plotly.express as px

# Montar o Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Carregar o arquivo CSV com a codificação 'latin1' e especificar delimitador
file_path = '/content/drive/MyDrive/Artigo Pós Ciências de Dados/Dados_Para_Analise/RAIS_SubClasse.csv'
df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')

# Subcategorias de interesse
subcategorias = [
    "Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet",
    "Portais, provedores de conteúdo e outros serviços de informação na internet",
    "Outras atividades de prestação de serviços de informação não especificadas anteriormente",
    "Consultoria em tecnologia da informação",
    "Suporte técnico, manutenção e outros serviços em tecnologia da informação",
    "Salas de acesso à internet",
    "web design",
    "Fabricação de equipamentos de informática",
    "Fabricação de periféricos para equipamentos de informática",
    "Comércio atacadista de equipamentos de informática",
    "Comércio varejista especializado de equipamentos e suprimentos de informática",
    "Recarga de cartuchos para equipamentos de informática",
    "Treinamento em informática"
]

# Filtrar o DataFrame para incluir apenas as subcategorias de interesse
df_filtered = df[df['CNAE_2_0_Subclasse'].isin(subcategorias)]

# Derreter o DataFrame para formato longo
df_melted = df_filtered.melt(id_vars=['CNAE_2_0_Subclasse'], value_vars=[str(year) for year in range(2002, 2024)],
                             var_name='Ano', value_name='Número de Vínculos Empregatícios')

# Converter a coluna 'Número de Vínculos Empregatícios' para numérico, forçando erros para NaN
df_melted['Número de Vínculos Empregatícios'] = pd.to_numeric(df_melted['Número de Vínculos Empregatícios'], errors='coerce')

# Adicionar uma coluna de números para identificação
df_melted['ID'] = df_melted['CNAE_2_0_Subclasse'].factorize()[0] + 1

# Criar o gráfico de bolhas interativo
fig = px.scatter(df_melted, x='Ano', y='Número de Vínculos Empregatícios', size='Número de Vínculos Empregatícios',
                 color='CNAE_2_0_Subclasse', hover_name='CNAE_2_0_Subclasse',
                 labels={'Número de Vínculos Empregatícios': 'Número de Vínculos Empregatícios', 'CNAE_2_0_Subclasse': 'Subclasse'},
                 title='Número de Vínculos Empregatícios por Subclasse ao Longo dos Anos')

# Ajustar o layout para um visual mais elegante
fig.update_layout(
    legend_title_text='Subclasse (ID)',
    xaxis_title='Ano',
    yaxis_title='Número de Vínculos Empregatícios',
    template='plotly_white'
)

# Mostrar o gráfico
fig.show()
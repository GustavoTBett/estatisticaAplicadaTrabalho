import pandas as pd

# Carregar o CSV (ajuste o caminho se necessário)
df = pd.read_csv("Developer Ecosystem Survey 2024_ Raw data sharing/2024_sharing_data_outside.csv", low_memory=False)

# Função auxiliar para converter "Yes"/"No" em 1/0
def to_binary(col):
    return col.notna().astype(int)

# ===============================
# 🧑‍💼 Perfil Profissional
# Análise de Frequência Relativa
# ===============================
print("\n📊 Distribuição de Status de Emprego:")
print(df['employment_status'].value_counts(normalize=True) * 100)

print("\n📊 Nível de Posição (Junior, Senior, etc):")
print(df['position_level'].value_counts(normalize=True) * 100)

print("\n🏢 Tamanho da Empresa:")
print(df['company_size'].value_counts(normalize=True) * 100)

print("\n👥 Tamanho da Equipe:")
print(df['team_size'].value_counts(normalize=True) * 100)

# ===============================
# 💻 Tecnologias e Ferramentas
# ===============================
# 🧠 Converter colunas proglang em dados binários
lang_cols = [col for col in df.columns if col.startswith('proglang::')]
lang_data = df[lang_cols].apply(to_binary)

# 📊 Calcular percentual de uso
lang_usage = (lang_data.mean().sort_values(ascending=False) * 100).round(2)

print("\n💻 Linguagens mais utilizadas pelos desenvolvedores:")
print(lang_usage.head(15))

# 🔍 Filtra colunas de linguagem principal
primary_lang_cols = [col for col in df.columns if col.startswith('primary_lang::')]

# 🧠 Converte presença em 1 e ausência em 0
primary_lang_data = df[primary_lang_cols].apply(to_binary)

# 📊 Contagem de cada linguagem como principal (soma das colunas)
primary_lang_usage = primary_lang_data.sum().sort_values(ascending=False)

# 📈 Percentual com base no total de respostas válidas
primary_lang_percent = (primary_lang_usage / primary_lang_data.sum().sum() * 100).round(2)

# 📋 Exibe o top 10
print("\n🏆 Linguagens mais usadas como PRINCIPAIS pelos devs:")
print(primary_lang_percent.head(10))


print("\n🛠️ IDE mais utilizada:")
print(df['ide_main'].value_counts(normalize=True) * 100)

print("\n🧪 Tipos de Testes Utilizados:")
test_cols = [col for col in df.columns if col.startswith('test_types::')]
test_data = df[test_cols].apply(to_binary)
print((test_data.mean().sort_values(ascending=False) * 100).round(2))

# ===============================
# 🌍 Localização
# ===============================
print("\n🌎 Países com mais respondentes:")
print(df['country'].value_counts().head(10))

# ===============================
# 🧠 Experiência e Educação
# ===============================
# Mapeia os valores para uma estimativa numérica
code_yrs_map = {
    "I don't have any professional coding experience": 0,
    "Less than 1 year": 0.5,
    "1–2 years": 1.5,
    "3–5 years": 4,
    "6–10 years": 8,
    "11–16 years": 13.5,
    "16+ years": 20
}

# Cria nova coluna com os valores numéricos
df['code_yrs_num'] = df['code_yrs'].map(code_yrs_map)

# Calcula média e distribuição
print("\n🧠 Média de anos de experiência:")
print(df['code_yrs_num'].mean().round(2))

print("\n📊 Distribuição das faixas de experiência:")
print(df['code_yrs'].value_counts(normalize=True).round(3) * 100)

# ===============================
# 📈 Interesses e Futuro
# ===============================
print("\n🚀 Linguagens que os devs pretendem adotar/migrar para:")
adopt_cols = [col for col in df.columns if col.startswith('adopt_proglang::')]
adopt_data = df[adopt_cols].apply(to_binary)
adopt_usage = (adopt_data.mean().sort_values(ascending=False) * 100).round(2)
print(adopt_usage.head(10))

# ===============================
# 💵 Informações Salariais (faixa)
# ===============================
if 'salary_satisfied' in df.columns:
    print("\n💵 Satisfação com o salário atual (%):")
    print(df['salary_satisfied'].value_counts(normalize=True).round(3) * 100)

# Filtra colunas com linguagem principal
primary_lang_cols = [col for col in df.columns if col.startswith('primary_lang::')]

# Transforma em binário
primary_lang_data = df[primary_lang_cols].apply(to_binary)

# Adiciona a coluna de satisfação
primary_lang_data['salary_satisfied'] = df['salary_satisfied']

# Agrupa por satisfação e soma por linguagem
cross_tab = primary_lang_data.groupby('salary_satisfied').sum()

# Calcula o percentual por linha (dentro de cada resposta de satisfação)
cross_tab_percent = cross_tab.div(cross_tab.sum(axis=1), axis=0) * 100

# Mostra os 5 principais casos por linguagem
print("\n📊 Cruzamento: Linguagem Principal vs Satisfação Salarial (%):")
print(cross_tab_percent.T.sort_values(by='Mostly satisfied', ascending=False).head(10).round(2))

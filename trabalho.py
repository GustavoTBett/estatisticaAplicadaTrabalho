import pandas as pd

# Carregar o CSV (ajuste o caminho se necessário)
df = pd.read_csv("Developer Ecosystem Survey 2024_ Raw data sharing/2024_sharing_data_outside.csv", low_memory=False)

# Função auxiliar para converter "Yes"/"No" em 1/0
def to_binary(col):
    return col.notna().astype(int)

# ===============================
# 🧑‍💼 Perfil Profissional
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

print([col for col in df.columns if 'education' in col.lower()])

print("\n🎓 Nível de escolaridade:")
if 'education_level' in df.columns:
    print(df['education_level'].value_counts(normalize=True) * 100)

# ===============================
# 📈 Interesses e Futuro
# ===============================
print("\n🚀 Tecnologias que os devs querem aprender:")
future_cols = [col for col in df.columns if col.startswith('future_technologies_interested_in::')]
future_data = df[future_cols].apply(to_binary)
print((future_data.mean().sort_values(ascending=False) * 100).round(2).head(10))

print([col for col in df.columns if 'future' in col.lower()])

print([col for col in df.columns if 'motivation' in col.lower()])


print("\n🎯 Motivação principal para aprender novas tecnologias:")
if 'main_motivation_to_learn_new_tech' in df.columns:
    print(df['main_motivation_to_learn_new_tech'].value_counts(normalize=True) * 100)

# ===============================
# 💵 Informações Salariais (faixa)
# ===============================
print([col for col in df.columns if 'income' in col.lower()])



if 'income_grouped' in df.columns:
    print("\n💵 Faixas salariais (grupo):")
    print(df['income_grouped'].value_counts(normalize=True) * 100)

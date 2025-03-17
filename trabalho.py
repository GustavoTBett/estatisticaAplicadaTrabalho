import pandas as pd
import numpy as np

# Definir o caminho do arquivo CSV
csv_file = "x/2024_sharing_data_outside.csv"  # Substitua pelo caminho correto

# Definir as colunas que queremos carregar
columns_to_load = [
    "response_id", "weight", "employment_status", "job_field_professional",
    "job_role::Architect", "job_role::Business Analyst", "job_role::CIO / CEO / CTO",
    "job_role::DBA", "job_role::Data Analyst / Data Engineer/ Data Scientist",
    "job_role::DevOps Engineer / Infrastructure Developer", "job_role::Developer / Programmer /  Software Engineer",
    "job_role::Developer Advocate", "job_role::Developer Productivity / Developer Experience Engineer",
    "job_role::Instructor / Teacher / Tutor", "job_role::Other", "job_role::Product Manager / Marketing Manager",
    "job_role::Systems Analyst", "job_role::Team Lead", "job_role::Technical Support",
    "job_role::Technical Writer", "job_role::Tester / QA Engineer", "job_role::UX / UI Designer",
    "position_level"
]

# Carregar o dataset usando pandas
df = pd.read_csv(csv_file, usecols=columns_to_load)

# Exibir as primeiras 5 linhas
print("Amostra dos dados:")
print(df.head())

# Informações gerais sobre os dados
print("\nInformações do dataset:")
print(df.info())

# Estatísticas das colunas numéricas
print("\nEstatísticas gerais:")
print(df.describe())

# Contar quantidade de profissionais em cada cargo
job_roles = [col for col in df.columns if col.startswith("job_role::")]
job_counts = df[job_roles].sum().sort_values(ascending=False)

print("\nQuantidade de profissionais por cargo:")
print(job_counts)

# Converter peso em NumPy para alguma análise matemática
weights = df["weight"].to_numpy()
print("\nPeso médio dos dados:", np.mean(weights))
print("Desvio padrão dos pesos:", np.std(weights))

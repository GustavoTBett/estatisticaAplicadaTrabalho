import pandas as pd
from llama_index.llms import Llama3
from llama_index.core import SimpleDirectoryReader, QueryEngine

# Carregar o CSV com as colunas necessárias
csv_file = "x/DevEcosystem 2024 questions_outside.csv"  # Substitua pelo caminho correto
df = pd.read_csv(csv_file, usecols=["shortname", "parent_shortname", "question_title"])

# Filtrar perguntas sobre salário
salary_keywords = ["salary", "compensation", "earnings", "income", "pay"]
df_salary = df[df["question_title"].str.contains("|".join(salary_keywords), case=False, na=False)]

# Filtrar perguntas sobre linguagens de programação
language_keywords = ["language", "programming", "tech stack", "framework"]
df_language = df[df["question_title"].str.contains("|".join(language_keywords), case=False, na=False)]

# Criar um conjunto de perguntas combinadas
df_combined = pd.merge(df_salary, df_language, on="parent_shortname", how="inner")

# Concatenar perguntas para o modelo Llama
questions_text = "\n".join(df_combined["question_title"].tolist())

# Inicializar o modelo Llama 3.1 8B
llm = Llama3(model="meta-llama/Meta-Llama-3-8B")

# Definir a consulta para encontrar as melhores perguntas
query = """
Given the following survey questions related to salary and programming languages, 
identify the most insightful ones for analyzing salary trends based on programming language usage.
Provide a ranked list of the top 5 most relevant questions.
"""

# Criar um engine de consulta e executar a análise
query_engine = QueryEngine(llm=llm)
response = query_engine.query(query + "\n\n" + questions_text)

# Exibir os resultados
print("Top 5 Relevant Salary-Programming Questions:")
print(response.text)

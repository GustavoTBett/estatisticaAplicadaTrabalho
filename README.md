# Estudos de Caso em Estatística Aplicada à Engenharia de Software

## Título do Estudo  
**Perfil e Práticas dos Desenvolvedores de Software: Um Estudo Estatístico com Base na Pesquisa JetBrains Developer Ecosystem 2024**

---

## 1. Introdução

A engenharia de software envolve decisões constantes sobre ferramentas, linguagens e metodologias. A estatística aplicada fornece uma base científica para entender o comportamento dos desenvolvedores e orientar essas decisões.

Este estudo de caso analisa os dados da pesquisa anual realizada pela JetBrains, com o objetivo de extrair insights sobre o perfil e práticas comuns dos profissionais da área.

---

## 2. Sobre a Fonte de Dados

### O Developer Ecosystem Survey 2024 da JetBrains disponibiliza dados brutos sob a licença CC-BY-4.0, permitindo compartilhamento e adaptação, desde que a fonte seja citada.

* Link para a pesquisa: [https://www.jetbrains.com/lp/devecosystem-2024/](https://www.jetbrains.com/lp/devecosystem-2024/)

Os arquivos fornecidos incluem:

- `2024_sharing_data_outside.csv.zip`: Dados amplos (6208 colunas, 23262 respostas), com identificador único e peso para ajuste de viés.
- `2024_sharing_data_outside_narrow.csv.zip`: Dados organizados em formato de banco de dados (4 colunas, 6 milhões de linhas).
- `DevEcosystem 2024 questions_outside.csv`: Lista de perguntas e seus identificadores (usado neste trabalho).
- `Developer_Ecosystem_2024_Survey_Structure.pdf`: Documento com a estrutura e lógica das perguntas.
- `LICENSE.txt`: Termos da licença de uso.

O conjunto de dados inclui informações sobre:

- Preferências de linguagem de programação
- Regiões e países
- Experiência profissional
- Posição ocupada
- Satisfação salarial (percepção)
- Tamanho da empresa e equipe
- Ferramentas utilizadas no dia a dia

Este conjunto atende a dúvidas comuns de pessoas que estão começando na área de tecnologia, como:

- **Qual linguagem paga mais?**
- **Quais são as tendências do mercado?**
- **Quais ferramentas são promissoras para o futuro?**
- **O que aprender para entrar no mercado?**

---

## 3. Objetivo

Investigar, por meio de análise estatística, os hábitos, preferências e características dos desenvolvedores de software com base em dados reais coletados na pesquisa JetBrains Developer Ecosystem 2024.

---

## 4. Metodologia

### 4.1 Coleta de Dados

- Os dados foram extraídos do arquivo público `2024_sharing_data_outside.csv`.

### 4.2 Seleção de Variáveis

As seguintes variáveis foram selecionadas para a análise:

- `employment_status`: situação de emprego do respondente.
- `primary_lang`: linguagens de programação principais.
- `proglang`: linguagens utilizadas no geral.
- `ide_main`: IDE mais utilizada.
- `code_yrs`: anos de experiência profissional.
- `test_types`: tipos de testes utilizados.
- `position_level`: nível de senioridade.
- `company_size` e `team_size`: estrutura das empresas.
- `salary_satisfied`: percepção sobre a satisfação salarial.

### 4.3 Técnicas Estatísticas Utilizadas

- Análise de frequência (absoluta e relativa)
- Gráficos de barras e pizza
- Medidas de tendência central (média, moda, mediana)
- Cruzamento de variáveis (Ex: linguagem principal × satisfação salarial)

Ferramentas utilizadas: Python (`pandas`)

---

## 5. Análise de Dados

### 5.1 Linguagens de Programação Mais Usadas

> Destaques:  
> JavaScript (62.12%), Python (54.97%), HTML/CSS (53.16%), SQL (52.27%) e Java (44.36%).

### 5.2 Linguagens Principais

> Mais escolhidas como linguagem principal:  
> Python (13.98%), Java (12.80%), JavaScript (11.61%), TypeScript (9.51%).

### 5.3 IDEs mais utilizadas

> As IDEs mais comuns são:  
> IntelliJ IDEA (25.86%), VS Code (22.43%), PyCharm (8.64%), Visual Studio (7.26%).

### 5.4 Experiência dos Desenvolvedores

> Média de experiência: **8,02 anos**  
> Faixa mais comum: **3 a 5 anos (22.7%)** seguida de **6 a 10 anos (20.7%)**.

### 5.5 Nível de Posição

> A maioria dos profissionais se identificam como:  
> **Senior (49.8%)**, **Middle (30.1%)** e **Junior (15.3%)**.

### 5.6 Situação de Emprego

> Status mais comum:  
> **Empregados em tempo integral (64.9%)**, **estudantes (10.8%)** e **trabalhadores autônomos ou freelancers (~10%)**.

### 5.7 Tamanho da Empresa e da Equipe

> A maioria trabalha em empresas de médio porte (51 a 500 funcionários) e times pequenos (2 a 7 pessoas).

### 5.8 Tipos de Testes Utilizados

> Unit Test (23.85%), Integration Test (19.32%), End-to-End Test (14.39%).

---

## 6. Cruzamento: Linguagem Principal × Satisfação Salarial

Este cruzamento mostra a distribuição da satisfação salarial para as 10 linguagens mais comuns como principais.

| Linguagem          | % Completamente Satisfeitos | % Mais Satisfeitos | % Insatisfeitos |
|--------------------|------------------------------|-------------------|------------------|
| Python             | 12.41%                       | 12.28%            | 14.05%           |
| Java               | 11.11%                       | 13.36%            | 14.19%           |
| TypeScript         | 10.75%                       | 10.83%            | 9.79%            |
| JavaScript         | 9.48%                        | 11.58%            | 14.05%           |
| SQL                | 7.39%                        | 8.23%             | 8.09%            |
| C#                 | 7.98%                        | 6.89%             | 5.25%            |
| HTML / CSS         | 6.81%                        | 7.36%             | 8.73%            |
| PHP                | 5.21%                        | 5.49%             | 4.83%            |
| Kotlin             | 4.27%                        | 4.37%             | 3.55%            |
| Shell scripting    | 4.14%                        | 3.18%             | 2.91%            |

> **Observação**: Linguagens como Python, Java e TypeScript apresentam maiores percentuais de satisfação total.

---

## 7. Desafios e Boas Práticas

### Desafios

- Coleta de dados com viés de autoseleção.
- Falta de dados exatos sobre salário.
- Grande volume e granularidade exigem tratamento cuidadoso.

### Boas Práticas

- Anonimização e privacidade dos dados.
- Visualização clara e objetiva.
- Adoção de cruzamentos para gerar insights mais profundos.

---

## 8. Conclusão

Este estudo demonstrou como a análise estatística pode fornecer uma visão clara sobre a realidade da engenharia de software atual. Ferramentas estatísticas aliadas a dados abertos oferecem oportunidades reais de aprendizado e tomada de decisão baseada em evidências.

Este estudo também é útil para orientar quem deseja entrar na área de tecnologia, ajudando a entender quais linguagens, ferramentas e práticas são mais adotadas no mercado atual.

---

## 9. Referências

- JetBrains Developer Ecosystem Survey 2024: [https://www.jetbrains.com/lp/devecosystem-2024/](https://www.jetbrains.com/lp/devecosystem-2024/)
- Python libraries: pandas
- Estatística Aplicada à Computação — Bibliografia da disciplina

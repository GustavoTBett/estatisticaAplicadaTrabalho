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
- Grupos salariais (sem valores exatos por motivos de privacidade)

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

- Os dados foram extraídos do arquivo público `DevEcosystem 2024 questions_outside.csv`.

### 4.2 Seleção de Variáveis

As seguintes variáveis foram selecionadas para a análise:

- `employment_status`: situação de emprego do respondente.
- `primary_lang`: linguagens de programação principais.
- `ide_main`: IDE mais utilizada.
- `code_yrs`: anos de experiência profissional.
- `test_types`: tipos de testes utilizados.
- `devops_use_docker`: uso de containers no desenvolvimento.
- `company_size` e `team_size`: estrutura das empresas.

### 4.3 Técnicas Estatísticas Utilizadas

- Análise de frequência (absoluta e relativa)
- Gráficos de barras e pizza
- Medidas de tendência central (média, moda, mediana)
- Cruzamento de variáveis (Ex: linguagem x IDE, experiência x tipo de teste)

Ferramentas utilizadas: Python (`pandas`, `seaborn`, `matplotlib`)

---

## 5. Análise de Dados

### 5.1 Linguagens de Programação Mais Usadas

> Gráfico de barras com as linguagens mais populares.

### 5.2 IDEs mais utilizadas

> Comparação entre JetBrains IDEs, VSCode, Sublime, etc.

### 5.3 Experiência dos Desenvolvedores

> Distribuição de anos de experiência por faixa etária ou por linguagem.

### 5.4 Relação entre Linguagem e Ferramentas de Teste

> Exemplo: Java + JUnit, Python + pytest, etc.

### 5.5 Uso de Containers e DevOps

> Percentual de desenvolvedores que usam Docker, Kubernetes e ferramentas de CI/CD.

---

## 6. Resultados e Discussão

Os dados revelam:

- Forte adoção de linguagens como Python, JavaScript e Java.
- Preferência por IDEs como VSCode e IntelliJ.
- Crescente uso de containers no desenvolvimento moderno.
- Adoção variada de testes automatizados, com destaque para testes unitários.

**Reflexão:** A estatística aplicada permite identificar padrões de comportamento, orientar a adoção de tecnologias e melhorar a organização de times de desenvolvimento.

---

## 7. Desafios e Boas Práticas

### Desafios

- Coleta de dados com viés de autoseleção.
- Grande volume de dados requer tratamento cuidadoso.

### Boas Práticas

- Anonimização dos dados.
- Visualização clara para facilitar a interpretação.
- Uso de amostragem balanceada em cruzamentos de variáveis.

---

## 8. Conclusão

Este estudo demonstrou como a análise estatística pode fornecer uma visão clara sobre a realidade da engenharia de software atual. Ferramentas estatísticas aliadas a dados abertos oferecem oportunidades reais de aprendizado e tomada de decisão baseada em evidências.

Este estudo também é útil para orientar quem deseja entrar na área de tecnologia, ajudando a entender quais linguagens, ferramentas e práticas são mais adotadas no mercado atual.

---

## 9. Referências

- JetBrains Developer Ecosystem Survey 2024: [https://www.jetbrains.com/lp/devecosystem-2024/](https://www.jetbrains.com/lp/devecosystem-2024/)
- Python libraries: pandas, matplotlib, seaborn
- Estatística Aplicada à Computação — Bibliografia da disciplina

# VII Desafio em Ciência de Dados

## Equipe

<div>
  
  [<img src="https://avatars.githubusercontent.com/u/98399932?v=4" alt="João Victor Porto" width="100">](https://github.com/Joao-vpf)
  [<img src="https://avatars.githubusercontent.com/u/104952737?v=4" alt="João Pedro Lemes" width="100">](https://github.com/Lixomensch)
  [<img src="https://avatars.githubusercontent.com/u/101851627?v=4" alt="João Henrique" width="100">](https://github.com/JoaoHMiranda)
  
</div>

## Sobre o Projeto

### Descrição do Desafio

A interação entre o vento solar e a magnetosfera da Terra pode causar clima espacial adverso e tempestades geomagnéticas, com o potencial de danificar tecnologias críticas, como sistemas de navegação, comunicações de rádio e redes elétricas. A gravidade de uma tempestade geomagnética é medida usando o índice Dst (Disturbance Storm Time).

O índice Dst é calculado pela média do componente horizontal do campo magnético observado em quatro observatórios quase equatoriais e é utilizado para conduzir modelos de perturbação geomagnética. Desde 1975, modelos de previsão foram propostos para prever o Dst somente a partir de observações do vento solar na posição Lagrangiana L1. Embora os modelos recentes de aprendizado de máquina geralmente tenham melhor desempenho do que outras abordagens, muitos são inadequados para uso operacional. O recente crescimento na pesquisa de ciência de dados e a democratização das ferramentas de aprendizado de máquina abriram a possibilidade de abordar este problema com novas técnicas e métricas de avaliação.

### Objetivo do Projeto

O objetivo deste projeto é desenvolver um modelo preditivo para o índice Dst utilizando técnicas de ciência de dados e aprendizado de máquina. Aplicamos conhecimentos teóricos e habilidades práticas para analisar uma base de dados pública, buscando encontrar soluções eficientes para o problema proposto.

### Motivação

O "Desafio em Ciência de Dados" visa avaliar o conhecimento prático e as habilidades dos participantes na resolução de problemas reais em ciência de dados. Realizado por equipes multidisciplinares, o desafio promove a interdisciplinaridade e o trabalho em equipe.

Além de incentivar a troca de experiências entre os participantes, o desafio busca desenvolver competências essenciais na área, como análise estatística, modelagem de dados, interpretação de resultados e comunicação dos achados.

Aqui está a versão corrigida do seu README:

### Dados:

[![Static Badge](https://img.shields.io/badge/Dados%20brutos-Link-green?style=for-the-badge&logo=googlesheets)](https://drive.google.com/file/d/1rgLAqDoHC7eZZahOMdqj73MTfpN2nGaA/view?usp=sharing)
[![Static Badge](https://img.shields.io/badge/Edital%20do%20projeto-PDF-red?style=for-the-badge&logo=files&logoColor=red)](<https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/readme/Roteiro/Edital-VII%20DESAFIO-CIÊNCIA%20DOS%20DADOS-VF-2024-2%20(1).pdf>)
[![Static Badge](https://img.shields.io/badge/Roteiro%20do%20projeto-PDF-red?style=for-the-badge&logo=files&logoColor=red)](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/readme/Roteiro/Roteiro%20para%20análise%20dos%20dados%20%20desafio%20V%20%20completo_1510.pdf)
[![Static Badge](https://img.shields.io/badge/Space%20Weather%20-PDF-red?style=for-the-badge&logo=files&logoColor=red)](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/readme/Roteiro/Space%20Weather%20-%202023%20-%20Nair%20-%20MagNet%20A%20Data‐Science%20Competition%20to%20Predict%20Disturbance%20Storm‐Time%20Inde.pdf)
[![Static Badge](https://img.shields.io/badge/Dicionário%20de%20dados-PDF-red?style=for-the-badge&logo=files&logoColor=red)](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/readme/Roteiro/dicionário%20de%20dados%20-%20VII%20desafio%20CD%202024.pdf)

### Código:

[![Static Badge](https://img.shields.io/badge/C%C3%B3digo%20do%20projeto-Link-orange?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/drive/1zkg6qAswrBDa1mRZnpakQDoR1mxd-gDu?usp=sharing)

## Implementação:

A implementação do desafio foi dividida em várias etapas para lidar com os dados brutos, uma vez que eles contêm muitos ruídos e informações desnecessárias que podem afetar o cálculo e, consequentemente, a qualidade da resposta. As etapas da implementação foram as seguintes:

1. Pre-processamento dos dados;
2. Completar/corrigir colunas;
3. EDA
4. Normalizar colunas;
5. Train Model

### 1. Pré-processamento dos dados:

1. A coluna `timedelta` foi convertida para o objeto `Timedelta` do pandas, garantindo um tratamento mais adequado de diferenças temporais.
2. As colunas `period` e `timedelta` foram definidas como índices do dataset para facilitar a organização e melhorar a eficiência das operações de análise.

### 2. Preenchimento e correção de colunas:

1. Os dados ausentes na coluna `solar_wilds` foram preenchidos utilizando o método de interpolação, garantindo uma transição suave entre os valores.
2. A coluna de manchas solares, `smoothed_ssn`, foi integrada ao dataset `solar_wilds`, e os valores faltantes foram preenchidos utilizando o método `fill`, assegurando a completude dos dados.

### 3. Análise Exploratória de Dados (EDA)

1. **Matriz de Correlação:**
   Foi gerada uma matriz de correlação entre as variáveis para analisar a relação entre elas.

   ![corr](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/main/images/corr.png)

   Observa-se que as variáveis `gsm` e `gse` apresentam uma forte correlação. Devido a essa alta correlação, é recomendável considerar a remoção de uma dessas variáveis para evitar redundância nos modelos subsequentes.

2. **Análise Temporal:**
   Foi realizada uma análise temporal dos dados `dsts` ao longo do tempo para identificar padrões e comportamentos.

   ![temporal](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/main/images/temporal_dst.png)

   - **Outliers e Eventos Extremos:**
     Quedas significativas, como as observadas no segmento em vermelho, podem ser classificadas como outliers ou eventos raros. Esses pontos geralmente representam grandes tempestades geomagnéticas.

   - **Segmentação e Transições:**
     As transições entre os períodos `Trem A`, `Trem B` e `Trem C` indicam diferentes fases ao longo do tempo.

### 3. Quantidade por Período:

A tabela abaixo mostra a quantidade de dados disponíveis para cada período (`train_a`, `train_b`, `train_c`):

| Período  | Train A   | Train B   | Train C   |
| -------- | --------- | --------- | --------- |
| Contagem | 1.575.012 | 3.084.130 | 3.407.290 |

### 4. Normalização de Colunas:

1. **Normalização dos Dados:**
   Foi realizada a normalização dos dados das colunas `solar_wild` e `sunspots` utilizando a função `StandardScaler()`, padronizando esses atributos para análise.

2. **Remoção de Colunas:**
   As colunas `"bx_gsm"`, `"by_gsm"`, `"bz_gsm"`, `"theta_gsm"`, `"phi_gsm"`, `"theta_gse"`, e `"phi_gse"`, relacionadas à variável `solar_wild`, foram removidas com base nas análises anteriores, por não agregarem valor ao modelo devido à sua alta correlação ou irrelevância.

3. **Ajuste da Frequência dos Dados:**
   Os dados da variável `dst` são coletados com frequência horária, enquanto os dados de `solar_wild` são coletados a cada minuto. Para ajustar essa diferença de granularidade, foi calculada a média e o desvio padrão dos dados de `solar_wild` para intervalos de uma hora. O resultado é apresentado na tabela a seguir, onde cada linha representa a média e o desvio padrão para as variáveis nesse período:

| Período | bx_gse_mean | bx_gse_std | by_gse_mean | by_gse_std | bz_gse_mean | bz_gse_std | bt_mean  | bt_std   | density_mean | density_std | speed_mean | speed_std | temperature_mean | temperature_std | smoothed_ssn |
| ------- | ----------- | ---------- | ----------- | ---------- | ----------- | ---------- | -------- | -------- | ------------ | ----------- | ---------- | --------- | ---------------- | --------------- | ------------ |
| 0h00min | -1.495610   | 0.195616   | 0.386310    | 0.308088   | 0.258776    | 0.173041   | 0.493174 | 0.516734 | -0.738481    | 0.114659    | -0.735688  | 0.156490  | -0.365926        | 0.292884        | 65.4         |
| 1h00min | -1.643940   | 0.084074   | 0.165197    | 0.228181   | 0.384224    | 0.218164   | 0.539745 | 0.104596 | -0.820192    | 0.162933    | -0.982174  | 0.168136  | -0.463491        | 0.446460        | 65.4         |
| 2h00min | -1.787911   | 0.027512   | 0.168886    | 0.083961   | 0.663165    | 0.097176   | 0.728812 | 0.020311 | -0.805470    | 0.109983    | -1.008617  | 0.129389  | -0.552849        | 0.137358        | 65.4         |
| 3h00min | -1.691628   | 0.103505   | -0.347757   | 0.389272   | 0.534932    | 0.294993   | 0.688780 | 0.096223 | -0.384938    | 0.253449    | -0.822949  | 0.062148  | -0.318572        | 0.277114        | 65.4         |
| 4h00min | -1.252354   | 0.171895   | 0.067172    | 0.568129   | 0.402752    | 0.231604   | 0.222640 | 0.104505 | -0.353707    | 0.213811    | -0.599416  | 0.169979  | -0.308009        | 0.243689        | 65.4         |

### 5. Treinamento do Modelo

1. **Divisão dos Dados:**
   Os dados foram cuidadosamente divididos nos conjuntos `X_train`, `X_val`, e `X_test`, assegurando que os três períodos (`train_a`, `train_b`, `train_c`) estivessem distribuídos de maneira equilibrada em todas as partes do dataset.

   ![Distribuição](https://github.com/SU4NE/VII-Desafio-em-Ciencia-de-Dados/blob/main/images/Distribution.png)

2. **Arquitetura do Modelo:**
   Uma combinação de diferentes tipos de camadas foi utilizada, incluindo `LSTM`, `Dense`, `GRU`, `Dropout`, `Bidirectional`, `Conv1D`, `BatchNormalization` e `MaxPooling1D`. As tabelas a seguir descrevem as camadas dos modelos testados e o número de parâmetros em cada uma delas:

   #### Modelo 1: Arquitetura Sequencial com LSTM e Camadas Conv1D

   | Layer (type)                  | Output Shape    | Param # |
   | ----------------------------- | --------------- | ------- |
   | conv1d (Conv1D)               | (None, 126, 64) | 2,944   |
   | dropout (Dropout)             | (None, 126, 64) | 0       |
   | max_pooling1d (MaxPooling1D)  | (None, 63, 64)  | 0       |
   | lstm (LSTM)                   | (None, 63, 64)  | 33,024  |
   | bidirectional (Bidirectional) | (None, 64)      | 18,816  |
   | dropout_1 (Dropout)           | (None, 64)      | 0       |
   | dense (Dense)                 | (None, 32)      | 2,080   |
   | dense_1 (Dense)               | (None, 16)      | 528     |
   | dense_2 (Dense)               | (None, 1)       | 17      |

   #### Modelo 2: Arquitetura Bidirecional com GRU

   | Layer (type)                               | Output Shape   | Param # |
   | ------------------------------------------ | -------------- | ------- |
   | conv1d_2 (Conv1D)                          | (None, 13, 64) | 256     |
   | max_pooling1d_2 (MaxPooling1D)             | (None, 6, 64)  | 0       |
   | bidirectional_4 (Bidirectional)            | (None, 6, 256) | 197,632 |
   | dropout_6 (Dropout)                        | (None, 6, 256) | 0       |
   | batch_normalization_2 (BatchNormalization) | (None, 6, 256) | 1,024   |
   | bidirectional_5 (Bidirectional)            | (None, 256)    | 296,448 |
   | dropout_7 (Dropout)                        | (None, 256)    | 0       |
   | dense_4 (Dense)                            | (None, 128)    | 32,896  |
   | dropout_8 (Dropout)                        | (None, 128)    | 0       |
   | dense_5 (Dense)                            | (None, 1)      | 129     |

   #### Modelo 3: CatBoost

Essas arquiteturas foram escolhidas para capturar padrões complexos em séries temporais e melhorar o desempenho do modelo com diferentes tipos de dados de entrada.

---

### 6. Resultados

Com base nas análises, o **Modelo 3 (CatBoost)** demonstrou alta eficácia na previsão do Dst. Seus resultados indicam que ele é capaz de fornecer previsões precisas e consistentes.

O modelo alcançou métricas satisfatórias, conforme descrito abaixo:

| Modelo   | R²       | RMSE     | MAE      |
| -------- | -------- | -------- | -------- |
| CatBoost | 0.649063 | 7.961570 | 5.826377 |

Esses resultados ressaltam a importância do pré-processamento dos dados, que pode melhorar significativamente a precisão do modelo. Contudo, é fundamental monitorar continuamente o desempenho do modelo e realizar ajustes conforme necessário, garantindo que ele permaneça uma ferramenta eficaz para previsões de Dst.

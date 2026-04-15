# Comparação de Consumo de Recursos: Ableton Live vs. FL Studio

Este projeto consiste em uma análise técnica detalhada sobre o gerenciamento de recursos por sistemas operacionais ao lidar com Digital Audio Workstations (DAWs). O trabalho faz parte da disciplina de **Sistemas Operacionais** do curso de Ciência da Computação - UFT.

##  Integrantes
* **Henrique Noronha**
* **Lauro Oliveira**
* **João Victor Melo do Nascimento**
* **Hátilan Caio Alves Fontes**

---

##  Objetivo do Trabalho
O objetivo principal é realizar um benchmark comparativo entre dois softwares equivalentes na área de produção musical (**Ableton Live** e **FL Studio**), focando em como cada arquitetura de software interage com o kernel do SO para gerenciar:
* **Uso de CPU:** Escalonamento de threads em processamento de áudio em tempo real.
* **Consumo de Memória (RAM):** Alocação dinâmica de memória para plugins e samples.
* **E/S de Disco e Latência:** Impacto do gerenciamento de buffer e interrupções de hardware.

##  Metodologia e Ferramentas
Para garantir a integridade dos dados, ambos os softwares serão testados sob as mesmas condições (plugins idênticos, mesma taxa de amostragem e mesmos arquivos de áudio).

As ferramentas utilizadas para coleta de evidências serão:
* **htop / Monitor de Recursos:** Para visualização da carga por núcleo de CPU.
* **LatencyMon:** Para medir a aptidão do kernel para processamento de tempo real.
*

##  Estrutura do Repositório

* `/imagens`: Capturas de tela (evidências) de consumo e gráficos.
* `/classe_uftex`: Arquivos de classe da UFT para compilação LaTeX.
* `main.tex`: Arquivo mestre do relatório acadêmico.

##  Evidências Esperadas
Ao final dos experimentos, o grupo apresentará:
1. **Tabelas Comparativas:** Comparação direta de consumo em estados de repouso (Idle) e carga máxima (Full Load).
2. **Discussão Técnica:** Análise sobre eficiência de escalonamento e overhead de drivers de áudio (ASIO vs DirectSound).
3. **Relatório Final:** Documento formatado conforme os padrões acadêmicos da UFT.

---
*Trabalho desenvolvido para a disciplina de Sistemas Operacionais, Curso de Ciência da Computação - Universidade Federal do Tocantins - 2026.1*
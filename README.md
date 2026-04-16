# Comparação de Consumo de Recursos: Ableton Live vs. FL Studio

Este projeto consiste em uma análise técnica detalhada sobre o gerenciamento de recursos por sistemas operacionais ao lidar com Digital Audio Workstations (DAWs). O trabalho faz parte da disciplina de **Sistemas Operacionais** do curso de Ciência da Computação - Universidade Federal do Tocantins (UFT).

## Integrantes
* **Henrique Noronha**
* **Lauro Oliveira**
* **João Victor Melo do Nascimento**
* **Hátilan Caio Alves Fontes**

---

## Objetivo do Trabalho
O objetivo principal é realizar um benchmark comparativo entre dois softwares equivalentes na área de produção musical (**Ableton Live** e **FL Studio**), analisando como diferentes arquiteturas de software interagem com o kernel do Sistema Operacional para gerenciar:
* **Uso de CPU:** Escalonamento de threads e tratamento de interrupções em processamento de áudio em tempo real.
* **Consumo de Memória (RAM):** Estratégias de alocação de memória (isolamento de objetos vs. ponteiros de memória compartilhada).
* **Gerenciamento de E/S e Latência:** Impacto de drivers de baixa latência (ASIO) no desvio do Kernel Mixer e monitoramento de DPC (Deferred Procedure Call).

## Metodologia e Instrumentação
A coleta de dados é realizada em níveis de kernel e processo, utilizando ferramentas de inspeção profunda para isolar o comportamento do software do hardware físico.

### Ferramentas de Coleta e Análise:
* **Performance Monitor (PerfMon):** Captura de contadores nativos do kernel em formato binário (.blg) para análise de % Tempo de Processador e Bytes Particulares.
* **Process Explorer (Sysinternals):** Inspeção granular de threads internas (Audio Engine, GUI, VST Bridge) e análise de prioridades de execução.
* **LatencyMon:** Monitoramento de latência de interrupções de kernel e aptidão do sistema para processamento em tempo real.
* **htop / CLI Tools:** Utilizados em ambientes virtualizados para monitoramento de processos em kernels Unix-like.

### Cenários de Teste:
1. **Baseline (I/O-Bound):** Reprodução de 20 trilhas simultâneas de áudio AIFF (não comprimido) para observar o gerenciamento de buffer e redundância de memória física.
2. **Estresse (CPU-Bound):** Introdução de algoritmos de convolução (Reverbs) e síntese granular para testar o escalonador sob carga intensa de ponto flutuante (FPU).
3. **Análise Multiplataforma:** Replicação dos testes em Máquinas Virtuais (VMs) rodando Linux (JACK/PipeWire) e macOS (Core Audio) para comparação entre arquiteturas de kernel NT e Unix-like.

## Estrutura do Repositório
* `/images`: Capturas de tela dos logs binários do PerfMon e diagramas de alocação.
* `/dados`: Arquivos de log brutos (.blg) e relatórios de latência.
* `/classe_uftex`: Arquivos de classe da UFT para compilação LaTeX.
* `main.tex`: Arquivo mestre do relatório acadêmico contendo a fundamentação teórica.

## Evidências Esperadas
1. **Análise de Endereçamento de Memória:** Demonstração da diferença entre alocações independentes (Ableton) e otimização por ponteiros compartilhados (FL Studio).
2. **Métricas de Escalonamento:** Comparação da distribuição de threads entre núcleos lógicos durante o processamento de plugins pesados.
3. **Relatório Técnico Final:** Documento detalhando os pontos de ruptura (buffer underrun) e a eficiência de cada arquitetura sob a ótica da Ciência da Computação.

---
*Trabalho desenvolvido para a disciplina de Sistemas Operacionais, Curso de Ciência da Computação - Universidade Federal do Tocantins - 2026.1*
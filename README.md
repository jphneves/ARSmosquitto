Beleza, paizão, vou te dar uma descrição curta e na moral pra botar no teu GitHub, explicando como executar o teu projeto de mensageria com Eclipse Mosquitto (os scripts sensor.py e dashboard.py pra monitoramento de casa inteligente). É direto, simples e perfeito pra galera da faculdade entender como rodar a demo. Tô ligado que tu quer algo enxuto, então bora!
Como Executar o Projeto

Este projeto usa Eclipse Mosquitto (MQTT) com Python para simular um sistema de casa inteligente. O sensor.py publica dados de temperatura e umidade, e o dashboard.py recebe e exibe esses dados em tempo real.
Pré-requisitos

    Mosquitto:
        Windows: Baixe e instale do site oficial.
        Linux: sudo apt-get install mosquitto
        macOS: brew install mosquitto
    Python: Versão 3.6+.
    Biblioteca Paho MQTT: Instale com:
    bash

    pip install paho-mqtt

Instruções

    Iniciar o Mosquitto:
        No Windows, abra o Prompt de Comando:
        cmd

cd "C:\Program Files\mosquitto"
mosquitto -v
Se a porta 1883 estiver em uso, mate o processo:
cmd
netstat -ano | find "1883"
taskkill /PID <PID> /F
Ou use outra porta:
cmd
mosquitto -v -p 1884
(Atualize PORT = 1884 em sensor.py e dashboard.py).
No Linux/macOS:
bash

    mosquitto -v

Rodar o Dashboard:

    Navegue até a pasta do projeto:
    cmd

cd caminho/para/projeto
Execute:
cmd

    python dashboard.py

Rodar o Sensor:

    Em outro terminal, na mesma pasta:
    cmd

        python sensor.py

Saída Esperada

    Mosquitto: Mostra logs de conexões e mensagens.
    dashboard.py: Exibe dados recebidos (ex.: Sensor: sala_001 | Temp: 22.5°C | Umidade: 65.2%).
    sensor.py: Envia dados a cada 5 segundos (ex.: {"temperatura": 22.5, "umidade": 65.2}).

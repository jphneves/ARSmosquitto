import paho.mqtt.client as mqtt
import json

# Configurações do Mosquitto
BROKER = "localhost"
PORT = 1883  # Muda pra 1884 se usou outra porta
TOPIC = "casa/sala/ambiente"

# Função pra processar mensagens
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[Recebido] Sensor: {payload['SENSOR_TOP']} | Temp: {payload['TEMPERATURA_CALIENTEE']}°C | Umidade: {payload['UMIDADE_AGUA_PAIZAO']}% | Hora: {payload['HORA_QUAL_HORA_FOI_MERMAO']}")
    except Exception as e:
        print(f"Erro na mensagem: {e}")

# Função de conexão
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Dashboard conectado ao Mosquitto! Na moral!")
        client.subscribe(TOPIC, qos=1)
        print(f"Inscrito em {TOPIC}")
    else:
        print(f"Falha na conexão: {rc}")

# Configura o cliente MQTT
client = mqtt.Client(client_id="dashboard_sala_001", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, keepalive=60)

print("Dashboard ligado, aguardando dados da casa inteligente...")
client.loop_forever()
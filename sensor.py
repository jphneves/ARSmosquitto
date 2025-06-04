import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do Mosquitto
BROKER = "localhost"
PORT = 1883  # Muda pra 1884 se usou outra porta
TOPIC = "casa/sala/ambiente"

# Função de conexão
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Sensor conectado ao Mosquitto! Tô na área, mermão!")
    else:
        print(f"Falha na conexão: {rc}")

# Configura o cliente MQTT
client = mqtt.Client(client_id="sensor_sala_001", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.connect(BROKER, PORT, keepalive=60)

# Loop pra publicar
client.loop_start()
try:
    while True:
        # Simula dados de temperatura (18-28°C) e umidade (40-80%)
        temperatura = round(random.uniform(18.0, 50.0), 1)
        umidade = round(random.uniform(40.0, 80.0), 1)
        payload = json.dumps({
            "SENSOR_TOP": "sala_001",
            "TEMPERATURA_CALIENTEE": temperatura,
            "UMIDADE_AGUA_PAIZAO": umidade,
            "HORA_QUAL_HORA_FOI_MERMAO": time.strftime("%H:%M:%S")
        })
        client.publish(TOPIC, payload, qos=1)
        print(f"[Enviado] {payload}")
        time.sleep(1)  # Envia a cada 5 segundos
except KeyboardInterrupt:
    print("Sensor desligado, mermão!")
    client.loop_stop()
    client.disconnect()
from network.communication import Communication
from network.mqtt_service import MQTTService

mqtt_service = MQTTService()
mqtt_service.connect()

comm = Communication('http://192.168.18.111:65525')
data = {
    'litterbot_id': '1',
    'status': 'active',
    # ...
}
response = comm.send_data('data', data)
print(response)

mqtt_service.disconnect()

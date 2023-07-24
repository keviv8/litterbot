from network.communication import Communication
from network.mqtt_service import MQTTService


def main():
    mqtt_service = MQTTService()
    mqtt_service.connect()

    comm = Communication('http://<ip_of_the_server>:5000')
    data = {
        'litterbot_id': '1',
        'status': 'active',
        # ...
    }
    response = comm.send_data('data', data)
    print(response)

    mqtt_service.disconnect()


if __name__ == "__main__":
    main()

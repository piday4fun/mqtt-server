import paho.mqtt.client as mqtt

HOST = "solasolo.oicp.net"
PORT = 1883

def test():
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)

    client.publish("topic", "hello World", 2)
    
    client.loop_forever()

if __name__ == '__main__':
    test()
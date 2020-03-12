import paho.mqtt.client as mqtt

HOST = "solasolo.oicp.net"
PORT = 1883

def OnMessage(client, userdata, msg):
  print(msg.topic + ": " + str(msg.payload))

def test():
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)

    client.subscribe("topic", 1)
    client.on_message = OnMessage

    client.loop_forever()

if __name__ == '__main__':
    test()
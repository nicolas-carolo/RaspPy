import paho.mqtt.client as mqtt


client = mqtt.Client()
client.connect("192.168.1.14",1883,60)
client.publish("topic/test", "Hello world, Nicolas!");
client.disconnect();

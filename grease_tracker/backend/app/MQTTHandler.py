from WorkerThread import WorkerThread
import paho.mqtt.client as mqtt
import logging
import time

class MQTTHandler(WorkerThread):
    privateRun = False
    isConnected = False
    msg_payload = None
    payload_len = 0
    host = ''
    port = ''

    def __init__(self, host, port, userName, password, keepAlive, subTopic):
        WorkerThread.__init__(self)
        self.setName("MQTTHandler")
        self.privateRun = False
        self.host = host
        self.port = port

        self.connect(host, port, userName, password, keepAlive, subTopic)

    def connect(self, host, port, userName, password, keepAlive, subTopic):
        self.subTopic = subTopic

        self.client = mqtt.Client()
        # self.client.username_pw_set(userName, password)
        # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        # self.client.tls_set_context(context)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        logging.debug("Initialize MQTT client -> host[" + str(host) + "], port[" + str(port) + "], subTopic[" + str(subTopic) + "]")
        try:
            self.client.connect(host, port, keepAlive)
            #self.client.reconnect_delay_set(1,1)
        except Exception as e:
            logging.error("Could not connect to MQTT host broker [" + str(host) + "], port[" + str(port) + "].")
            logging.error(e)
            return 1

        return 0

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        logging.debug("Connected to MQTT broker with result code "+str(rc))
        self.isConnected = True
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        client.subscribe(self.subTopic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        self.msg_payload = msg.payload
        self.payload_len = len(msg.payload)
        logging.debug("Received message of length " + str(self.payload_len))

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            logging.debug("Unexpected MQTT disconnection.")
        self.isConnected = False
    
    def run(self):
        logging.debug("running thread MQTTHandler")
        self.privateRun = True
        while(self.privateRun == True):
            if (self.stopped() == True):
                logging.debug("Stopping thread MQTTHandler")
                self.privateRun = False
            else:
                self.client.loop()
                if self.isConnected == False:
                    logging.debug('MQTT broker not connected')
                    try:
                        logging.debug("Trying to reconnect to MQTT host broker [" + str(self.host) + "], port[" + str(self.port))
                        self.client.reconnect()
                    except Exception as e:
                        # logging.error("Unable to reconnect to MQTT host broker [" + str(self.host) + "], port[" + str(self.port) + "], exception:" + e)
                        logging.error("Unable to reconnect to MQTT host broker [" + str(self.host) + "], port[" + str(self.port) + "].")
                        logging.error(e)
                    time.sleep(5)
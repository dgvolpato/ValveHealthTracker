from backend.app.WorkerThread import WorkerThread
from backend.app.MQTTHandler import MQTTHandler
import time
import logging
import json

class AppWorker(WorkerThread):
    privateRun = False
    privateBusClient = None
    privateDataOutEndpoint = ""
    mqtt_handler = None

    # MQTT params temporary initialization
    broker_ip = ""
    broker_port = 1883
    username = ""
    password = ""
    keep_alive = 60
    pubTopic_fractreestructure = ""
    pubTopic_valvestateupdate = ""
    pubTopic_pressuresensorreadings = ""
    subTopic = ""

    def __init__(self):
        WorkerThread.__init__(self)
        self.setName("AppWorker")
        self.privateRun = False
        self.Configure()

    def Configure(self):
        logging.debug("Config setup")
        
        self.broker_ip = "localhost"
        self.broker_port = 1883
        self.username = "admin"
        self.password = "admin123"
        self.keep_alive = 60
        self.pubTopic = "test"
        self.subTopic = "pressure_level"

    def run(self):
        logging.debug("running thread AppWorker")
        self.privateRun = True

        self.mqtt_handler = MQTTHandler(self.broker_ip, self.broker_port, self.username, self.password, self.keep_alive, self.subTopic)
        self.mqtt_handler.start()
        
        # To run valve actuation test sequence
        '''
        test_obj = ValveUpdateTest(status_update_json, frac_tree_json)
        test_obj.run_test(self.privateBusClient, self.privateDataOutEndpoint)
        '''
        
        while(self.privateRun == True):
            if (self.stopped() == True):
                logging.debug("Stopping thread AppWorker")
                self.privateRun = False
            else:
                time.sleep(10)
                logging.debug("Main thread running")
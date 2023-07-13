from enum import Enum
from tracemalloc import take_snapshot
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
# from backend.app.db import database, PressureReadings
from fastapi.middleware.cors import CORSMiddleware
from MQTTHandler import MQTTHandler
from WorkerThread import WorkerThread
import logging
import json
import time
from AppWorker import AppWorker



class Main():

    def __init__(self):
        self.privateAppWorker = None
        self.privateRun = False

    def Initialize(self):
        self.privateAppWorker = AppWorker()

    def Execute(self):
        logging.debug("Calling Execute, will sleep for test purpose")
        self.privateAppWorker.start()

        while(self.privateRun == True):
            time.sleep(60)

        return 0


    def Terminate(self):
        logging.debug("Calling Terminate")

        self.privateAppWorker.stop()

        if (self.privateAppWorker.getThreadId() != None):
            self.privateAppWorker.join()

        self.privateRun = False

        return 0

    def HandleData(self, payload):
        logging.debug("Data received")

        if (self.privateAppWorker):
            logging.debug("Sending to client")
            self.privateAppWorker.HandleData(payload)

        return 0

    def run(self):
        logging.debug("running thread AppWorker")
        self.privateRun = True

        self.mqtt_handler = MQTTHandler(self.broker_ip, 
                                        self.broker_port, 
                                        self.username, 
                                        self.password, 
                                        self.keep_alive, 
                                        self.subTopic)
        self.mqtt_handler.start()
        
        while(self.privateRun == True):
            # if (self.stopped() == True):
            #     logging.debug("Stopping thread AppWorker")
            #     self.privateRun = False
            # else:
                time.sleep(10)
                logging.debug("Main thread running")



if __name__ == "__main__":
    main = Main()
    main.Initialize()
    main.Execute()




app = FastAPI(title="Hackathon2023_Backend")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "http://localhost:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/pressure")
# async def get_pressure():
#     today_string = "{:%m/%d/%Y}".format(datetime.now())
#     HARDCODED_VALVE_ID = 1
    
#     try:
#         valve_pressure_history = await PressureReadings.objects.filter(valve_id=HARDCODED_VALVE_ID).get()
#     except:
#         valve_pressure_history = None
    
#     return valve_pressure_history


# @app.put("/pressure")
# async def put_pressure():
#     today_string = "{:%m/%d/%Y}".format(datetime.now())

#     try:
#         today_intake = await PillIntake.objects.filter(intake_date=today_string).get()
#         today_intake.intake = True
#         await today_intake.update()
#     except:
#         today_intake = await PillIntake.objects.get_or_create(intake_date=today_string, intake=True)
#     return today_intake

# @app.post("/pressure")
# async def post_pressure():

#     try:
#         pressure_reading = PressureReadings()
#     except:
#     return:


# @app.get("/daily-status")
# async def get_daily_status():

#     today_intake = await get_pill_intake()

#     if today_intake.intake == True:
#         return {"status" : DailyStatus.good_for_today}
#     else:
#         return {"status" : DailyStatus.take_pill}


# @app.delete("/pill-intake")
# async def delete_pill_intake():
#     today_string = "{:%m/%d/%Y}".format(datetime.now())
#     try:
#         today_intake = await PillIntake.objects.delete(intake_date=today_string)
#     except:
#         today_intake = {}

#     return today_intake


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.on_event("startup")
# async def startup():
#     if not database.is_connected:
#         await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()
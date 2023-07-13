# Intro

The simulator will publish grease level as a string using mqtt protocol.
The application Grease tracker will subscribe to the "grease_level" topic, store its value.
Grease tracker frontend will generate a plot, and provide an indicator about when grease level is low.

During a greasing event, the valve cavity information will be used to monitor how much grease is used and a signal will be sent out to point out too much grease is being used in that valve.

# MQTT installation
https://mosquitto.org/download/

# Running simulator (Windows):

* grease level simulator
  `python .\hackathon_simulator\hackathon_simulator.py -t g`


* pressure simulator
  `python .\hackathon_simulator\hackathon_simulator.py -t p`


* run backend
```
cd grease_tracker
bash scripts/docker-build.sh
bash scripts/docker-run.sh
```

* minor test: `python .\grease_tracker\backend\app\main.py`

* frontend url: `http://localhost:80/`

# Test requests

`curl -X GET http://localhost:8008/pressure`
import subprocess
import argparse
import logging
import random
import time
import sys

def run_mosquitto_pub(topic, value_message, broker_address="localhost"):
    subprocess.run(["resources\\mosquitto_pub.exe", "-m", str(round(value_message,2)), "-t", topic, "-h", broker_address])

def get_grease_level_state(grease_level):
    if (grease_level <= 0.3):
        grease_level = 55
    else:
        grease_level -= 0.45

    return grease_level

def run_grease_level_simulator():
    
    grease_level = 55
    while True:
        run_mosquitto_pub(topic="grease_level", value_message=grease_level)
        grease_level = get_grease_level_state(grease_level)
        time.sleep(3)

def get_pressure_level_state(pressure_level, step):
    STEP_DECREASE_CONSTANT= 230
    LIMIT_CONSTANT= 13000
    PRESSURE_INCREASE_FACTOR = 350

    if step < 60:
        if pressure_level + step * STEP_DECREASE_CONSTANT >= LIMIT_CONSTANT :
            pressure_level= 0
            step += 1
        else:
            random_factor = random.randint(-3,9)
            pressure_level += random_factor * PRESSURE_INCREASE_FACTOR
    else:
        step = 0
    
    return pressure_level, step

def run_pressure_simulator():
    pressure_level = 0
    step = 0
    while True:
        print("sent value: ", str(pressure_level))
        run_mosquitto_pub(topic="pressure_level", value_message=pressure_level)
        pressure_level, step = get_pressure_level_state(pressure_level, step)
        time.sleep(0.5)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='hackathon simulator.')
    parser.add_argument('--type', '-t', type=str, 
                        help='type g from grease or p for pressure')
    
    args = parser.parse_args()
    print(args.type)
    simulator_type = args.type

    formatter = '%(asctime)s %(levelname)-8s %(message)s'
    dateformat='%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename="GreaseLevelSimulatorLog.txt", format = formatter, datefmt = dateformat)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    try:
        log.info("Welcome to Grease Level Digital Hackathon Simulator")
        if simulator_type == "g":
            log.info("selected grease simulator")
            run_grease_level_simulator()
        elif simulator_type == "p":
            log.info("selected pressure simulator")
            run_pressure_simulator()
        else:
            print("Invalid simulator type")
            print("Exiting program...")
            sys.exit
    except:
        log.info("Unexpected error:", sys.exc_info()[0])
    finally:
        log.info("Closing the Grease Level Digital Hackathon Simulator...")
        log.info("Exiting program...")
        sys.exit()

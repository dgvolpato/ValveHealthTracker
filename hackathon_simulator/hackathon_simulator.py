import subprocess
import argparse
import logging
import random
import time
import sys

def run_mosquitto_pub(topic, value_message, broker_address="localhost"):
    subprocess.run(["resources\\mosquitto_pub.exe", "-m", str(round(value_message,2)), "-t", topic, "-h", broker_address])

def run_grease_simulator(type):
    grease_level = 0
    step = 0
    while True:
        # print("sent value: ", str(grease_level))
        print(str(grease_level))
        run_mosquitto_pub(topic="grease_level", value_message=grease_level)
        if type == "gh":
            grease_level, step = run_grease_level_simulator_healthy(grease_level, step)
        elif type == "gum":
            grease_level, step = run_grease_level_simulator_unhealthy_maintenance_needed(grease_level, step)
        elif type == "gus":
            grease_level, step = run_grease_level_simulator_unhealthy_spill(grease_level, step)
        else:
            grease_level = 0
            step = 0
        time.sleep(0.1)

def run_grease_level_simulator_healthy(grease_level, step):
    
    STEP_INCREASE_CONSTANT= 0
    LIMIT_CONSTANT= 3
    GREASE_INCREASE_FACTOR = 0.16

    if step < 30:
        if grease_level + step * STEP_INCREASE_CONSTANT >= LIMIT_CONSTANT :
            grease_level= 0
            step += 1
        else:
            random_factor = random.randint(-2,9)
            grease_level += random_factor * GREASE_INCREASE_FACTOR
    else:
        step = 0

    return round(grease_level,2), step

def run_grease_level_simulator_unhealthy_maintenance_needed(grease_level, step):
    
    
    LIMIT_CONSTANT= 3
    GREASE_INCREASE_FACTOR = 0.16

    if step < 30:
        LIMIT_CONSTANT= 3
        STEP_INCREASE_CONSTANT= 0.13
        if grease_level >= LIMIT_CONSTANT + step * STEP_INCREASE_CONSTANT:
            grease_level= 0
            step += 1
        else:
            random_factor = random.randint(1,9)
            grease_level += random_factor * GREASE_INCREASE_FACTOR
    # elif step < 15:
    #     STEP_INCREASE_CONSTANT= 0.3
    #     LIMIT_CONSTANT= 3
    #     if grease_level >= LIMIT_CONSTANT :
    #         grease_level= 0
    #         step += 1
    #     else:
    #         random_factor = random.randint(-2,9)
    #         grease_level += random_factor * GREASE_INCREASE_FACTOR
    else:
        step = 0

    if grease_level < 0:
        grease_level = 0

    return round(grease_level,2), step

def run_grease_level_simulator_unhealthy_spill(grease_level, step):
    
    STEP_INCREASE_CONSTANT= 0.3
    LIMIT_CONSTANT= 3
    GREASE_INCREASE_FACTOR = 0.16

    if step >= 25 and step < 30:
        if grease_level >= LIMIT_CONSTANT + step * STEP_INCREASE_CONSTANT:
            grease_level= 0
            step += 1
        else:
            random_factor = random.randint(-2,6)
            grease_level += random_factor * GREASE_INCREASE_FACTOR
    elif step < 25:
        if grease_level >= LIMIT_CONSTANT :
            grease_level= 0
            step += 1
        else:
            random_factor = random.randint(-2,9)
            grease_level += random_factor * GREASE_INCREASE_FACTOR
    else:
        step = 0

    if grease_level < 0:
        grease_level = 0

    return round(grease_level,2), step

def get_pressure_level_state(pressure_level, step):   # DEPRECATED
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
    
    if pressure_level < 0:
        pressure_level = 0

    return pressure_level, step


def run_pressure_level_simulator_healthy(pressure_level, step):   
    STEP_DECREASE_CONSTANT= 230
    LIMIT_CONSTANT= 13000
    PRESSURE_INCREASE_FACTOR = 350

    if step < 60:
        if pressure_level >= LIMIT_CONSTANT :
            pressure_level= 0
            step += 1
        else:
            random_factor = random.randint(-3,9)
            pressure_level += random_factor * PRESSURE_INCREASE_FACTOR
    else:
        step = 0
    
    if pressure_level < 0:
        pressure_level = 0

    return pressure_level, step


def run_pressure_level_simulator_unhealthy_maintenance_needed(pressure_level, step):   
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
    
    if pressure_level < 0:
        pressure_level = 0

    return pressure_level, step


def run_pressure_level_simulator_unhealthy_spill(pressure_level, step):  
    STEP_DECREASE_CONSTANT= 300
    LIMIT_CONSTANT= 13000
    PRESSURE_INCREASE_FACTOR = 350

    if step < 25:
        if pressure_level >= LIMIT_CONSTANT :
            pressure_level= 0
            step += 1
        else:
            random_factor = random.randint(-3,9)
            pressure_level += random_factor * PRESSURE_INCREASE_FACTOR
    elif step >= 25:
        if pressure_level + step * STEP_DECREASE_CONSTANT >= LIMIT_CONSTANT :
            pressure_level= 0
            step += 1
        else:
            random_factor = random.randint(-3,9)
            pressure_level += random_factor * PRESSURE_INCREASE_FACTOR
    else:
        step = 0
    
    if pressure_level < 0:
        pressure_level = 0

    return pressure_level, step

def run_pressure_simulator(type):
    pressure_level = 0
    step = 0
    while True:
        print(str(pressure_level))
        run_mosquitto_pub(topic="pressure_level", value_message=pressure_level)
        # pressure_level, step = get_pressure_level_state(pressure_level, step)
        if type == "ph":
            pressure_level, step = run_pressure_level_simulator_healthy(pressure_level, step)
        elif type == "pum":
            pressure_level, step = run_pressure_level_simulator_unhealthy_maintenance_needed(pressure_level, step)
        elif type == "pus":
            pressure_level, step = run_pressure_level_simulator_unhealthy_spill(pressure_level, step)
        else:
            pressure_level = 0
            step = 0
        time.sleep(0.005)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='hackathon simulator.')
    parser.add_argument('--type', '-t', type=str, 
                        help='type gh, gum, gus from grease or ph, pum, pus for pressure')
    
    args = parser.parse_args()
    print(args.type)
    simulator_type = args.type

    formatter = '%(asctime)s %(levelname)-8s %(message)s'
    dateformat='%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename="GreaseLevelSimulatorLog.txt", format = formatter, datefmt = dateformat)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    try:
        print("simulator type: ", simulator_type)
        log.info("Welcome to Grease Level Digital Hackathon Simulator")
        if simulator_type == "gh":
            log.info("selected grease simulator (healthy)")
            run_grease_simulator(simulator_type)
        if simulator_type == "gum":
            log.info("selected grease simulator (unhealthy - maintenance needed)")
            run_grease_simulator(simulator_type)
        if simulator_type == "gus":
            log.info("selected grease simulator (healthy - spill)")
            run_grease_simulator(simulator_type)
        if simulator_type == "ph":
            log.info("selected pressure simulator (healthy)")
            run_pressure_simulator(simulator_type)
        if simulator_type == "pum":
            log.info("selected pressure simulator (unhealthy - maintenance needed)")
            run_pressure_simulator(simulator_type)
        if simulator_type == "pus":
            log.info("selected pressure simulator (healthy - spill)")
            run_pressure_simulator(simulator_type)
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

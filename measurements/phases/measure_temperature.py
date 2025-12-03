import random
import time


def measure_temperature(measurements, log):
    temperature = round(random.uniform(18.0, 32.0), 1)

    log.info(f"Measuring temperature: {temperature}Â°C")
    measurements.ambient_temperature = temperature
    time.sleep(10)
    log.info("Temperature measurement complete")

import sys


def run_test(phase, unit):
    print("Running test...")
    unit.serial_number = "SN-324"
    unit.revision_number = "RN-324"
    return


def main(phase):
    return phase.fail("Main failure")
    # raise Exception("Main error")


def use_plug(counter, measurements):
    val = counter.get_value()
    measurements.initial_value = val


def should_not_run(failingplug, log, measurements):
    log.info("Hi there !")
    measurements.ran = True

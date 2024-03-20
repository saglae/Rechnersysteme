#!/usr/bin/python3

#Das hier soll aus dem Internet kopiert werden!

from ctypes import CDLL, CFUNCTYPE, POINTER, c_int, c_uint, pointer, c_ubyte, c_uint8, c_uint32
import sysconfig
import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    #print(dist.project_name, dist.version)
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus
import site


class Vl53l0xError(RuntimeError):
    pass


class Vl53l0xAccuracyMode:
    GOOD = 0        # 33 ms timing budget 1.2m range
    BETTER = 1      # 66 ms timing budget 1.2m range
    BEST = 2        # 200 ms 1.2m range
    LONG_RANGE = 3  # 33 ms timing budget 2m range
    HIGH_SPEED = 4  # 20 ms timing budget 1.2m range


class Vl53l0xDeviceMode:
    SINGLE_RANGING = 0
    CONTINUOUS_RANGING = 1
    SINGLE_HISTOGRAM = 2
    CONTINUOUS_TIMED_RANGING = 3
    SINGLE_ALS = 10
    GPIO_DRIVE = 20
    GPIO_OSC = 21


class Vl53l0xGpioAlarmType:
    OFF = 0
    THRESHOLD_CROSSED_LOW = 1
    THRESHOLD_CROSSED_HIGH = 2
    THRESHOLD_CROSSED_OUT = 3
    NEW_MEASUREMENT_READY = 4


class Vl53l0xInterruptPolarity:
    LOW = 0
    HIGH = 1


# Read/write function pointer types.
_I2C_READ_FUNC = CFUNCTYPE(c_int, c_ubyte, c_ubyte, POINTER(c_ubyte), c_ubyte)
_I2C_WRITE_FUNC = CFUNCTYPE(c_int, c_ubyte, c_ubyte, POINTER(c_ubyte), c_ubyte)

# Load VL53L0X shared lib
suffix = sysconfig.get_config_var('EXT_SUFFIX')
if suffix is None:
    suffix = ".so"
_POSSIBLE_LIBRARY_LOCATIONS = ['../bin'] + site.getsitepackages() + [site.getusersitepackages()]
for lib_location in _POSSIBLE_LIBRARY_LOCATIONS:
    try:
        _TOF_LIBRARY = CDLL(lib_location + '/vl53l0x_python' + suffix)
        break
    except OSError:
        pass
else:
    raise OSError('Could not find vl53l0x_python' + suffix)


#Read Data


# Create a VL53L0X object
tof = VL53L0X(i2c_bus=1,i2c_address=0x29)
# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof.open()
# Start ranging
tof.start_ranging(Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))

for count in range(1, 101):
    distance = tof.get_distance()
    if distance > 0:
        print("%d mm, %d cm, %d" % (distance, (distance/10), count))

    time.sleep(timing/1000000.00)

tof.stop_ranging()
tof.close()

import RPi.GPIO as GPIOimport dht11import timeimport datetime
# initialize GPIOGPIO.setwarnings(False)GPIO.setmode(GPIO.BCM)GPIO.cleanup()
# read data using pin 14instance = dht11.DHT11(pin=14)
while True:    result = instance.read() if result.is_valid(): print("Last valid input: " + str(datetime.datetime.now())) print("Temperature: %d C" % result.temperature) print("Humidity: %d %%" % result.humidity)
    time.sleep(1)
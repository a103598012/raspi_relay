import RPi.GPIO as GPIO
import getopt, sys, time

# Pin Definitons:
n1Pin = 27
n2Pin = 17
n3Pin = 24
n4Pin = 23

def rpi_pin_init():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
  GPIO.setup(n1Pin, GPIO.OUT)
  GPIO.setup(n2Pin, GPIO.OUT)
  GPIO.setup(n3Pin, GPIO.OUT)
  GPIO.setup(n4Pin, GPIO.OUT)
  GPIO.output(n1Pin, GPIO.LOW)
  GPIO.output(n2Pin, GPIO.LOW)
  GPIO.output(n3Pin, GPIO.LOW)
  GPIO.output(n4Pin, GPIO.LOW)


def reboot(index):
  print("reboot device on relay %s" % index)
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
  GPIO.setup(n1Pin, GPIO.OUT)
  GPIO.setup(n2Pin, GPIO.OUT)
  GPIO.setup(n3Pin, GPIO.OUT)
  GPIO.setup(n4Pin, GPIO.OUT)
  if index in ('1', 'n1'):
     GPIO.output(n1Pin, GPIO.HIGH)
     time.sleep(2)
     GPIO.output(n1Pin, GPIO.LOW)
  if index in ('2', 'n2'):
     GPIO.output(n2Pin, GPIO.HIGH)
     time.sleep(2)
     GPIO.output(n2Pin, GPIO.LOW)
  if index in ('3', 'n3'):
     GPIO.output(n3Pin, GPIO.HIGH)
     time.sleep(2)
     GPIO.output(n3Pin, GPIO.LOW)
  if index in ('4', 'n4'):
     GPIO.output(n4Pin, GPIO.HIGH)
     time.sleep(2)
     GPIO.output(n4Pin, GPIO.LOW)


def shutdown(index):
  print("shutdown device on relay %s" % index)
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
  GPIO.setup(n1Pin, GPIO.OUT)
  GPIO.setup(n2Pin, GPIO.OUT)
  GPIO.setup(n3Pin, GPIO.OUT)
  GPIO.setup(n4Pin, GPIO.OUT)
  if index in ('1', 'n1'):
     GPIO.output(n1Pin, GPIO.HIGH)
  if index in ('2', 'n2'):
     GPIO.output(n2Pin, GPIO.HIGH)
  if index in ('3', 'n3'):
     GPIO.output(n3Pin, GPIO.HIGH)
  if index in ('4', 'n4'):
     GPIO.output(n4Pin, GPIO.HIGH)

def poweron(index):
  print("shutdown device on relay %s" % index)
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
  GPIO.setup(n1Pin, GPIO.OUT)
  GPIO.setup(n2Pin, GPIO.OUT)
  GPIO.setup(n3Pin, GPIO.OUT)
  GPIO.setup(n4Pin, GPIO.OUT)
  if index in ('1', 'n1'):
     GPIO.output(n1Pin, GPIO.LOW)
  if index in ('2', 'n2'):
     GPIO.output(n2Pin, GPIO.LOW)
  if index in ('3', 'n3'):
     GPIO.output(n3Pin, GPIO.LOW)
  if index in ('4', 'n4'):
     GPIO.output(n4Pin, GPIO.LOW)




opts, args = getopt.getopt(sys.argv[1:], '-h-f:-v-i-r-s-p', ['help', 'filename=','version', 'init', 'reboot=', 'shutdown=', 'poweron='])
for opt_name, opt_value in opts:
  if opt_name in ('-i', '--init'):
      print("init pin")
      rpi_pin_init()
      exit()
  if opt_name in ('-r', '--reboot'):
      reboot(opt_value)
      exit()
  if opt_name in ('-s', '--shutdown'):
      shutdown(opt_value)
      exit()
  if opt_name in ('-p', '--poweron'):
      poweron(opt_value)
      exit()
  if opt_name in ('-h', '--help'):
      print("help info")
      print("sudo python relay.py --init" )
      print("sudo python relay.py --reboot=1")
      exit()


#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import optparse
import sys

PIN_MAKERBOT = 24
PIN_FRONT_LIGHT = 23
PIN_SIDE_LIGHT = 25

KEYWORD_LIGHT = "light"
KEYWORD_BOT = "bot"
KEYWORD_ON = "on"
KEYWORD_OFF = "off"

def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)

  GPIO.setup(PIN_MAKERBOT, GPIO.OUT)
  GPIO.setupPIN_FRONT_LIGHT, GPIO.OUT)
  GPIO.setup(PIN_SIDE_LIGHT, GPIO.OUT)

  # parse command line arguments
  parser = optparse.OptionParser()
  parser.add_option(
    '-d', '--device',
    dest="device",
    type="string")
  parser.add_option(
    '-s', '--state',
    dest="state",
    type="string")
  options, remainder = parser.parse_args()

  if options.device.lower() == KEYWORD_LIGHT:
    if options.state.lower() == KEYWORD_ON:
      GPIO.output(light, GPIO.HIGH)
      GPIO.output(light2, GPIO.HIGH)
    elif options.state.lower() == KEYWORD_OFF:
      GPIO.output(light, GPIO.LOW)
      GPIO.output(light2, GPIO.LOW)
  elif options.device.lower() == KEYWORD_BOT:
    if options.state.lower() == KEYWORD_ON:
      GPIO.output(makerbot, GPIO.HIGH)
    elif options.state.lower() == KEYWORD_OFF:
      GPIO.output(makerbot, GPIO.LOW)
  else:
    print "Not a valid command"

if __name__ == "__main__":
  main()

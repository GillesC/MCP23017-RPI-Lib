#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017

import time
import random
try:
	mcp = MCP23017(address = 0x20, num_gpios = 16) # MCP23017

	for pin in range(5,11):
		mcp.pinMode(pin, mcp.OUTPUT)
	while (True):
		pin = random.randint(5,10)
		mcp.output(pin, mcp.HIGH)  # Pin 0 High
		time.sleep(.1)
		mcp.output(pin, mcp.LOW)  # Pin 0 Low
except KeyboardInterrupt:
	print ("\n Keyboard interrupt!")
finally:
	for pin in range(5,11):
		mcp.output(pin, 0)
	print("Powered down")

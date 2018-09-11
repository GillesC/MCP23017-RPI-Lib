#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017

import time
try:
	pin = 10
	mcp = MCP23017(address = 0x20, num_gpios = 16) # MCP23017

	mcp.pinMode(pin, mcp.OUTPUT)

	while (True):
		mcp.output(pin, 1)  # Pin 0 High
		time.sleep(1)
		mcp.output(pin, 0)  # Pin 0 Low
		time.sleep(1)
except KeyboardInterrupt:
	print ("\n Keyboard interrupt!")
finally:
	mcp.output(pin, 0)
	print("Powered down")

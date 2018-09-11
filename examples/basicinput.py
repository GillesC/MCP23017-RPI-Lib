#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017

import time

mcp = MCP23017(address = 0x20, num_gpios = 16) # MCP23017

inpin=15
mcp.pinMode(inpin, mcp.INPUT)
mcp.pullUp(inpin, 1)

ledpin=8
mcp.pinMode(ledpin, mcp.OUTPUT)

# Read input pin and display the results
#print "Pin 3 = %d" % (mcp.input(3) >> 3)

while (True):
	mcp.output(ledpin, 1)  # Pin 0 High
	time.sleep(.1)
	print("Pin %d = %d" % (inpin, mcp.input(inpin)))
	mcp.output(ledpin, 0)  # Pin 0 Low
	time.sleep(1)

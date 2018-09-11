#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
from MCP23017 import MCP23017
import RPIO as GPIO

import time

# interrupt callback function
# just get the pin and values and print them
def inthappened(pin, val):
	pin, value = mcp.readInterrupt()
	print("%s    %s" % (pin, value))
try:
	mcp = MCP23017(address = 0x20, num_gpios = 16) # MCP23017

	inpin = 14
	mcp.pinMode(inpin, mcp.INPUT)
	mcp.pullUp(inpin, 1)

	ledpin = 8
	mcp.pinMode(ledpin, mcp.OUTPUT)
	# mirror on, int pin high indicates interrupt
	mcp.configSystemInterrupt(mcp.INTMIRRORON, mcp.INTPOLACTIVEHIGH)
	# for the input pin, enable interrupts and compare to previous value rather than default
	mcp.configPinInterrupt(inpin, mcp.INTERRUPTON, mcp.INTERRUPTCOMPAREPREVIOUS)

	# use a builting GPIO pin from the Pi to detect any change on the mcp23017
	# specify the callback function
	# edge must be set to rising - rising to high indicates the interrupt happened,
	# while falling is just the pin resetting
	# set the pin to pull down to act as a sink when the mcp23017 int pin goes high
	# do not thread - the mcp23017 int pin stays high until cleared even if multiple 
	# interrupts occur. there is a risk that we'll miss an interrupt if they happen 
	# very quickly together
	# set a very small debounce. 5ms seems good. higher and you could end up with
	# the int pin getting "stuck"
	GPIO.add_interrupt_callback(4, inthappened, edge='rising', pull_up_down=GPIO.PUD_DOWN, threaded_callback=False, debounce_timeout_ms=5)
	# regular GPIO wait for interrupts
	GPIO.wait_for_interrupts(threaded=True)
	while (True):
		mcp.output(ledpin, 1)
		time.sleep(.1)
		#mcp.output(ledpin, 0)
		time.sleep(2)
		# this is a failsafe for the instance when two interrupts happen before 
		# the debounce timeout expires. it will check for interrupts on the pin 
		# three times in a row, .5 seconds apart. if it gets to the end of 3 
		# iterations, we're probably stuck so it will reset
		mcp.clearInterrupts()
except Exception as e:
	print("Error in main: " + format(e))
finally:
	mcp.cleanup()
	GPIO.cleanup()

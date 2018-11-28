# MCP23017-RPI-Lib

Original source code: https://bitbucket.org/dewoodruff/mcp23017-python-3-library-with-interrupts.

---

**New in this repo**

Resolve bug where multiple pins on the same bank cause an interrupt. The original code assumed that only one pin is high of the INTCAP register. More details of the chip can be found here: http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf.

---

This library implements a python 3 library for the MCP23017 port expander chip. It is intended to be used on a Raspberry Pi in conjunction with the built in GPIO pins.

Requirements:

* python 3 port of Adafruit's I2C library, which is included in this repo
* python 3 smbus module. See [wiki](https://bitbucket.org/dewoodruff/mcp23017-python-3-library-with-interrupts/wiki/smbus%20python%203) for instructions to install on a Raspberry Pi.

Features:

* Simple digital input and output via all pins
* Input interrupts
* Interrupt port mirroring is configurable – either INTA and INTB can trigger independently for their respective GPIO port banks, or both INTA and INTB can trigger at the same time regardless of what GPIO pin causes the interrupt
* Configurable interrupt polarity – INT could pull the pin high or push it low
* Each GPIO pin can be configured for interrupts independently to either compare against the previous value or against a default pin value
* A utility method cleanupInterrupts that can be called periodically to clear the interrupt if it somehow gets stuck on.



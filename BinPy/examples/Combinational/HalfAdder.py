from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for Half Adder class """
print ("\n---Initializing the HalfAdder class--- ")
print ("ha = HalfAdder(0, 1)")
ha = HalfAdder(0, 1)
print ("\n---Output of HalfAdder")
print ("ha.output()")
print (ha.output())
print("The output is of the form [SUM, CARRY]")
print ("\n---Input changes---")
print ("ha.setInput(1, 0) #Input at index 1 is changed to 0")
ha.setInput(1, 0)
print ("\n---New Output of the HalfAdder---")
print (ha.output())
print ("\n---Changing the number of inputs---")
print ("No need to set the number, just change the inputs")
print ("Input length must be two")
print ("ha.setInputs(1, 1)")
ha.setInputs(1, 1)
print ("\n---To get the input states---")
print ("ha.getInputStates()")
print (ha.getInputStates())
print ("\n---New output of HalfAdder---")
print (ha.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output at index to Connector conn---")
print ("ha.setOutput(0, conn)")
ha.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
print ("Information about ha instance can be found by")
print ("ha")
print (ha)

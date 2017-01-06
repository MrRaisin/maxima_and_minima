# This problem involves testing an algorithm
# the 'program' takes an integer input, called x
# and carries out a calculation using x
# the evaluation [the result] is returned to the
# calling program.

# to import the library is shown below
import afunction2
# an input value of 10 is shown below
#x = 10
# and now call the function [test it]
#y = afunction2.calc(x)
# the output is shown below
#print(y)

for x in range (-300, 300, 20):
    print('x:',str(x),'y:', str(afunction2.calc(x)))


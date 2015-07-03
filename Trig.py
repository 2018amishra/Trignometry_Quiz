from __future__ import division
from sympy import symbols
from random import choice
from sympy import *

numOfRight = 0
numOfWrong = 0

trig_funcs = [sin, cos, tan]

angles = range (-330,360,30) + range (-315,360,90)
def sin_test(degrees):
    answer = input('What is sin %d: ' % degrees)
    # answer = input(degrees)
    if eval(str(answer)) ==  simplify(sin(rad(degrees))):
        print "Correct!"
        numOfRight + 1
        degrees = choice(angles)
        test = choice(type_of_test)
        #sin_and_cos_test(degrees,test)
        sin_test(degrees)
    else:
        print "Sorry that is incorrect"
        numOfWrong + 1
        degrees = choice(angles)
        test = choice(type_of_test)
        #sin_and_cos_test(degrees,test)
        sin_test(degrees)
        
def cos_test(degrees):
    answer = input('What is cos %d: ' % degrees)
    # answer = input(degrees)
    if eval(str(answer)) ==  simplify(cos(rad(degrees))):
        print "Correct!"
        numOfRight + 1
        degrees = choice(angles)
        #sin_and_cos_test(degrees,test)
        cos_test(degrees)
    else:
        print "Sorry that is incorrect"
        numOfWrong + 1
        degrees = choice(angles)
        #sin_and_cos_test(degrees,test)
        cos_test(degrees)

def tan_test(degrees):
    answer = input('What is tan %d: ' % degrees)
    # answer = input(degrees)
    if eval(str(answer)) ==  simplify(tan(rad(degrees))):
        print "Correct!"
        numOfRight + 1
        degrees = choice(angles)
        #sin_and_cos_test(degrees,test)
        tan_test(degrees)
    else:
        print "Sorry that is incorrect"
        numOfWrong + 1
        degrees = choice(angles)
        #sin_and_cos_test(degrees,test)
        tan_test(degrees)
        
def trig_test():
    func = choice(trig_funcs)
    degrees = choice(angles)
    att = input ("What is %s %d ? "  % (repr(func),degrees))
    ans = simplify(func(rad(degrees)))
    if eval(str(att)) == ans:
        print "Correct!"
        numOfRight + 1
        degrees = choice(angles)
        #sin_and_cos_test(degrees,test)
        cos_and_sin_test()
    else:
        print "Sorry that is incorrect. It was %s" % ans
        numOfWrong + 1
        degrees = choice(angles)
        
def radian_test():
    radian_list = [rad(x) for x in angles]
    types = [deg,rad]
    typeof = choice(types)
    if typeof == rad:
        radia = choice(radian_list)
        att = input ("What is %s %s in degrees? "  % (typeof.__name__,radia))
        if att == simplify(deg(radia)):
            print "Correct"
        else:
            print "Failure, this was supposed to be easy"
    if typeof == deg:
        degre = choice(angles)
        att = input ("What is %s %s in radians? "  % (typeof.__name__,degre))
        if att == simplify(rad(degre)):
            print "Correct"
        else:
            print "Nice job, you got it WRONG"
    radian_test()      
    



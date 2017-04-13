import time;
import math;
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
def fpm(b,n,m):
	return pow(b,n)%m
def dec(a):
	for t in range (0,127):
		if((t**17-a)%629==0):
			return t
		
# def gcd1 ( a , b ):
#      if (b == 0):
#          return 1, 0, a
#      else:
#          x , y , q = gcd1( b , a % b )
#          x , y = y, ( x - (a // b) * y )
#          return x, y, q
	
#ticks=time.time()
#print(fpm(2,17,629))
print(fpm(1,17,629))
#print(dec(337))
#print(fpm(1234223432,56789101112,24123456789101112))
#ticks1=time.time()
#print(ticks1-ticks)
print(chr(dec(247))+
	chr(dec(337))+
	chr(dec(322))+
	chr(dec(463))+
	chr(dec(15))+
	chr(dec(342))+
	chr(dec(323))+
	chr(dec(435))

	)
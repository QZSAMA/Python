def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
def pr(a):
	ar=[];
	for i in range(2,a):
		if(is_prime(i)):
			ar.append(i);
	return ar;
def fu(x):
	re=[]
	c=pr(x/2)
	while(x>1):
		for i in range (0,len(c)):
			if x%c[i]==0:
				re.append(c[i])
				x=x/c[i]

	return re


print(fu(129))
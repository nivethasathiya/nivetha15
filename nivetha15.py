lowerlimit = input()
upperlimit = input()
lowerlimit = int(lowerlimit)
upperlimit = int(upperlimit)
num = lowerlimit
while num <= upperlimit :
	p = list(str(num))
	count = 0
	for a in p:
		count += int(a)**3
	if count == num :
		print("Armstrong Number = " , num)

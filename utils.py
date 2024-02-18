def fact(n):
	if n==0:
		return 1
	m=1
	for i in range(1,n+1):
		m*=i
	return m
def isprime(n):
	prime = True
	while i<=n**0.5:
		prime = prime and n%i!=0
		i+=1
	return prime
def fivepower(n):
	while n%5==0:
		n=n//5
	return n=1
def twopower(n):
        while n%2==0:
                n=n//2
        return n=1

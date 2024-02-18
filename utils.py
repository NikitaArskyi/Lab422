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

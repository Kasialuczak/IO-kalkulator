# To będzie plik na którym będziemy pracowali 
def hello(name):
  return "Hello" + str(name)

def minus(a,b):
	return a-b

def plus(a,b):
	wynik= float(a) + float(b)
	return wynik

pierwsza = input()
druga = input()

print (plus(pierwsza, druga))

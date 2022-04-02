# To będzie plik na którym będziemy pracowali 
def hello(name):
  return "Hello" + str(name)

def minus(a,b):
	wynik = float(a) - float(b)
	return wynik

def plus(a,b):
	wynik= float(a) + float(b)
	return wynik

pierwsza = input()
druga = input()

print (plus(pierwsza, druga))

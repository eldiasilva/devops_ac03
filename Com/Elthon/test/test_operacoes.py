def func(x):
	return x + 10

def test_positivo():
	assert func(6) == 16

def test_negativo():
	assert func(-21) == -11

def test_zero():
	assert func(-10) == 0

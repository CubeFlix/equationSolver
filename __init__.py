# One variable linear and quadratic equation solver
# Simplifies expressions to terms mx + b or ax^2 + bx + c, then solves.
# Using ints, floats, and Fractions.

from fractions import Fraction
from collections.abc import Iterable
import cmath

def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

class Symbol:
	def __init__(self, name):
		self.name = name
	def __add__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return Term(2, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other.symbol) == Symbol:
				return Term(other.coefficient + 1, self)
			elif other.symbol.name == self.name and type(other.symbol) == Square:
				return Add(other, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, other])
		elif type(other) == Add:
			return Add([self] + other.items)
		elif type(other) == Square:
			return Add([self, other])
	def __radd__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return Term(2, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other.symbol) == Symbol:
				return Term(other.coefficient + 1, self)
			elif other.symbol.name == self.name and type(other.symbol) == Square:
				return Add(other, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, other])
		elif type(other) == Add:
			return Add([self] + other.items)
		elif type(other) == Square:
			return Add([self, other])
	def __sub__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return 0
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other) == Symbol:
				return Term(1 - other.coefficient, self)
			elif other.symbol.name == self.name and type(other) == Square:
				return Add([self, -other])
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, -other])
		elif type(other) == Add:
			return Add([self] + list(flatten(other.get_negative())))
		elif type(other) == Square:
			return Add([self, -other])
	def __rsub__(self, other):
		if other == 0:
			return Term(-1, self)
		else:
			return Add([-self, other])
	def __neg__(self):
	    return Term(-1, self)
	def __mul__(self, other):
		if type(other) in (int, float, Fraction):
			return Term(other, self)
		elif type(other) == Symbol:
			return Square(self.name)
		elif type(other) == Term:
			return Term(other.coefficient, Square(self))
		elif type(other) == Add:
			new = []
			for i in other.items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				new.append(i * self)
			return Add(new)
	def __rmul__(self, other):
		if type(other) in (int, float, Fraction):
			return Term(other, self)
		elif type(other) == Symbol:
			return Square(self.name)
		elif type(other) == Term:
			return Term(other.coefficient, Square(self))
		elif type(other) == Add:
			new = []
			for i in other.items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				new.append(i * self)
			return Add(new)
	def __truediv__(self, number):
		if type(number) in (Fraction, int, float):
			return Term(Fraction(1, number), self)
		elif type(number) == Symbol:
			if number.name == self.name:
				return 1
			else:
				return TypeError("Only use one variable!")
		elif type(number) == Term:
			if number.name == self.name:
				return Fraction(1, number.coefficient)
			else:
				return TypeError("Only use one variable!")
	def __pow__(self, n):
		if n == 2:
			return Square(self.name)
	def __repr__(self):
		return self.name

class Square:
	def __init__(self, name):
		self.name = name
	def __add__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return Term(2, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other.symbol) == Square:
				return Term(other.coefficient + 1, self)
			elif other.symbol.name == self.name and type(other.symbol) == Symbol:
				return Add([other, self])
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, other])
		elif type(other) == Add:
			return Add([self] + other.items)
		elif type(other) == Symbol:
			return Add([self, other])
	def __radd__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return Term(2, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other.symbol) == Square:
				return Term(other.coefficient + 1, self)
			elif other.symbol.name == self.name and type(other.symbol) == Symbol:
				return Add(other, self)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, other])
		elif type(other) == Add:
			return Add([self] + other.items)
		elif type(other) == Symbol:
			return Add([self, other])
	def __sub__(self, other):
		if type(other) == type(self):
			if other.name == self.name:
				return 0
			else:
				raise TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other) == Square:
				return Term(1 - other.coefficient, self)
			elif other.symbol.name == self.name and type(other) == Symbol:
				return Add([self, -other])
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, -other])
		elif type(other) == Add:
			return Add([self] + list(flatten(other.get_negative())))
		elif type(other) == Symbol:
			return Add([self, -other])
	def __rsub__(self, other):
		if other == 0:
			return Term(-1, self)
		else:
			return Add([-self, other])
	def __neg__(self):
	    return Term(-1, self)
	def __mul__(self, other):
		if type(other) in (int, float, Fraction):
			return Term(other, self)
	def __rmul__(self, other):
		if type(other) in (int, float, Fraction):
			return Term(other, self)
	def __truediv__(self, other):
		if type(other) in (Fraction, int, float):
			return Term(Fraction(1, other), self)
		elif type(other) == Symbol:
			if other.name == self.name:
				return other
			else:
				return TypeError("Only use one variable!")
		elif type(other) == Square:
			if other.name == self.name:
				return 1
			else:
				return TypeError("Only use one variable!")
		elif type(other) == Term:
			if other.symbol.name == self.name and type(other.symbol) == Square:
				return Fraction(1, other.coefficient)
			elif other.symbol.name == self.name and type(other.symbol) == Symbol:
				return Term(Fraction(1, other.coefficient), other.symbol)
			else:
				return TypeError("Only use one variable!")
	def __repr__(self):
		return self.name + '^2'

class Term:
	def __init__(self, coefficient, symbol):
		self.coefficient = coefficient
		self.symbol = symbol
	def __repr__(self):
		return str(self.coefficient) + ' * ' + str(self.symbol)
	def __add__(self, other):
		if type(other) == type(self):
			if other.symbol == self.symbol:
				return Term(other.coefficient + self.coefficient, self.symbol)
			elif type(other.symbol) != type(self.symbol) and other.symbol.name == self.symbol.name:
				return Add(other, self)
			else:
				raise TypeError("Only use one variable!")
		if type(other) in (Symbol, Square):
			if other == self.symbol:
				return Term(self.coefficient + 1, other)
			elif other != self.symbol and other.name == self.symbol.name:
				return Add(self, other)
			else:
				raise TypeError("Only use one variable!")
		if type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, other])
		if type(other) == Add:
			return Add([[self]+ other.items])
	def __sub__(self, other):
		if type(other) == type(self):
			if other.symbol == self.symbol:
				return Term(-other.coefficient + self.coefficient, self.symbol)
			elif type(other.symbol) != type(self.symbol) and other.symbol.name == self.symbol.name:
				return Add([-other, self])
			else:
				raise TypeError("Only use one variable!")
		if type(other) in (Symbol, Square):
			if other == self.symbol:
				return Term(self.coefficient - 1, other)
			elif other != self.symbol and other.name == self.symbol.name:
				return Add(self, -other)
			else:
				raise TypeError("Only use one variable!")
		elif type(other) in (Fraction, int, float):
			if other == 0:
				return self
			else:
				return Add([self, -other])
		elif type(other) == Add:
			return Add([self, list(flatten(other.get_negative()))])
	def __mul__(self, other):
		if type(other) in (int, float, Fraction):
			return Term(self.coefficient * other, self.symbol)
		elif type(other) == Symbol:
			if other.name == self.symbol.name:
				return Term(self.coefficient, Square(self.symbol.name))
			else:
				raise TypeError("Only use one variable!") 
		elif type(other) == Term:
			if other.symbol == self.symbol and type(other.symbol) != Square and type(self.symbol) != Square:
				return Term(self.coefficient * other.coefficient, Square(self.symbol.name))
		elif type(other) == Add:
			new = []
			for i in other.items:
				if (type(i) == Square or type(self.symbol) == Square):
					raise TypeError("No cubes.")
				new.append(i * self)
			return Add(new)
	def __neg__(self):
	    return Term(-1 * self.coefficient, self.symbol)
	def __truediv__(self, other):
		if type(other) in (Fraction, int, float):
			return Term(Fraction(self.coefficient, other), self.symbol)
		elif type(other) == Symbol:
			if number.name == self.symbol.name:
				return self.coefficient
			else:
				return TypeError("Only use one variable!")
		elif type(number) == Term:
			if number.symbol == self.symbol:
				return Fraction(self.coefficient, number.coefficient)
			else:
				return TypeError("Only use one variable!")

class Add:
	def __init__(self, items):
		self.items = items
		self.simplify()
	def __repr__(self):
		output = ""
		for i in self.items[:-1]:
			output += str(i) + ' + '
		output += str(self.items[-1])
		return output
	def __add__(self, other):
		if type(other) == type(self):
			return Add(self.items + other.items)
		else:
			return Add(self.items + [other])
	def __radd__(self, other):
		if type(other) == type(self):
			return Add(self.items + other.items)
		else:
			return Add(self.items + [other])
	def __sub__(self, other):
		if type(other) == type(self):
			return Add([self.items, list(flatten(other.get_negative()))])
		else:
			return Add(self.items + [-other])
	def __rsub__(self, other):
		if type(other) == type(self):
			return Add([list(flatten(self.get_negative())), other])
		else:
			return Add([list(flatten(self.get_negative())), other])
	def __mul__(self, other):
		if type(other) in (int, float, Fraction):
			for i in range(len(self.items)):
				self.items[i] *= other
			return self
		elif type(other) == Symbol:
			for i in self.items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and type(i.symbol) == Square:
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Square:
			for i in self.items:
				if type(i) == Symbol or type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and (type(i.symbol) == Symbol or type(i.symbol) == Square):
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Term and type(other.symbol) == Symbol:
			for i in self.items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and type(i.symbol) == Square:
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Term and type(other.symbol) == Square:
			for i in self.items:
				if type(i) == Symbol or type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and (type(i.symbol) == Symbol or type(i.symbol) == Square):
					raise TypeError("No cubes.")
				i *= other
		return self
	def __rmul__(self, other):
		if type(other) in (int, float, Fraction):
			for i in range(len(self.items)):
				self.items[i] *= other
			return self
		elif type(other) == Symbol:
			for i in items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and type(i.symbol) == Square:
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Square:
			for i in items:
				if type(i) == Symbol or type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and (type(i.symbol) == Symbol or type(i.symbol) == Square):
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Term and type(other.symbol) == Symbol:
			for i in items:
				if type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and type(i.symbol) == Square:
					raise TypeError("No cubes.")
				i *= other
		elif type(other) == Term and type(other.symbol) == Square:
			for i in items:
				if type(i) == Symbol or type(i) == Square:
					raise TypeError("No cubes.")
				elif type(i) == Term and (type(i.symbol) == Symbol or type(i.symbol) == Square):
					raise TypeError("No cubes.")
				i *= other
		return self
	def __truediv__(self, other):
		if type(other) in (int, float, Fraction):
			for i in range(len(self.items)):
				self.items[i] *= Fraction(1, other)
			return self
	def expand(self):
		expanded = []
		for i in self.items:
			if type(i) == Add:
				expanded.append(i.expand())
			else:
				expanded.append(i)
		return expanded
	def simplify(self):
		expanded = list(flatten(self.expand()))
		simplified = []
		types = []
		for i in expanded:
			if type(i) == Symbol:
				if 'symterm' in types:
					simplified[types.index('symterm')] += i
				else:
					types.append('symterm')
					simplified.append(i)
			elif type(i) == Square:
				if 'squterm' in types:
					simplified[types.index('squterm')] += i
				else:
					types.append('squterm')
					simplified.append(i)
			elif type(i) == Term:
				if type(i.symbol) == Symbol:
					if 'symterm' in types:
						simplified[types.index('symterm')] += i
					else:
						types.append('symterm')
						simplified.append(i)
				elif type(i.symbol) == Square:
					if 'squterm' in types:
						simplified[types.index('squterm')] += i
					else:
						types.append('squterm')
						simplified.append(i)
			elif type(i) in (int, float, Fraction):
				if 'num' in types:
					simplified[types.index('num')] += i
				else:
					types.append('num')
					simplified.append(i)
		self.items = simplified
	def get_negative(self):
		negative_add = []
		for i in self.items:
			if type(i) == Add:
				negative_add.append(i.get_negative())
			else:
				negative_add.append(-i)
		return negative_add

def _solve_quad(exp, solvefor):
	a = 0
	b = 0
	c = 0
	for i in exp.items:
		if type(i) == Term:
			if type(i.symbol) == Square:
				a = i.coefficient
			elif type(i.symbol) == Symbol:
				b = i.coefficient
		elif type(i) == Square:
			a = 1
		elif type(i) == Symbol:
			b = 1
		elif type(i) in (int, float, Fraction):
			c = i
	answers = [(-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a), (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)]
	return answers

def _solve_linear(exp, solvefor, retm=False):
	assert type(exp) == Add
	assert len(exp.items) == 2
	for i in exp.items:
		if type(i) in (int, float, Fraction):
			b = i
		elif type(i) == Term:
			m = i.coefficient
		elif type(i) == Symbol:
			m = 1
	answer = -b/m
	if retm:
		return answer, m
	else:
		return answer

def solve(exp1, exp2=0, solvefor=None):
	side = exp1 - exp2
	if type(side) == Symbol:
		side = Add([side, 0])
	elif type(side) == Term:
		side = Add([side, 0])
	elif type(side) == Square:
		side = Add([side, 0])
	assert type(side) == Add
	if solvefor == None:
		for i in side.items:
			if type(i) == Symbol:
				solvefor = i
			elif type(i) == Term:
				solvefor = Symbol(i.symbol.name)
			elif type(i) == Square:
				solvefor = Symbol(i.name)
	assert solvefor != None
	for i in side.items:
		if type(i) == Term and type(i.symbol) == Square:
			return _solve_quad(side, solvefor)
		elif type(i) == Square:
			return _solve_quad(side, solvefor)
	return _solve_linear(side, solvefor)

def solve_inequality(exp1, exp2, direction, equals, solvefor=None):
	# Direction of True means a > b, if direction is False, then a < b.
	# Equals argument means if it is <= and >=, or < and >.
	side = exp1 - exp2
	if type(side) == Symbol:
		side = Add([side, 0])
	elif type(side) == Term:
		side = Add([side, 0])
	elif type(side) == Square:
		side = Add([side, 0])
	assert type(side) == Add
	if solvefor == None:
		for i in side.items:
			if type(i) == Symbol:
				solvefor = i
			elif type(i) == Term:
				solvefor = Symbol(i.symbol.name)
			elif type(i) == Square:
				solvefor = Symbol(i.name)
	assert solvefor != None
	answ, b = _solve_linear(side, solvefor, retm=True)
	if b < 0:
		direction = not direction
	if direction:
		if equals:
			return '[' + str(answ) + ', inf)'
		else:
			return '(' + str(answ) + ', inf)'
	else:
		if equals:
			return '(-inf, ' + str(answ) + ']' 
		else:
			return '(-inf, ' + str(answ) + ')'

def simplify(exp):
	if not type(exp) in (Term, Symbol, Add):
		raise TypeError("Only simplify expressions")
	else:
		return Add([exp, 0])
	return exp

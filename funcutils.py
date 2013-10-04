# I Combinator (Identity) - Equivalent to id in Haskell
# Function that returns its argument always.
# May seem trivial, but can be a powerful utility function
# when composing higher-order functions.
def I(x): 
	return x

# K Combinator (Kestrel) - Equivalent to const in Haskell
# Practical application: "Tap" function in Ruby, that allows
# operations on intermediate results of a large function chain.
# In lambda calculus: K x y = x

def K(x): 
	return lambda y: x # Always return x.

# S Combinator (Starling) - Equivalent to <*> in Haskell.
# "Substitution" Combinator
def S(x, y):
	return lambda z: x(z(y(z)))

# B Combinator (Bluebird) - Equivalent to function composition in Haskell.
# Practical application: Compose smaller functions with higher-order functions.
# This leads to a more expressive and declarative style of programming.
# In lambda calculus: B x y z = x (y z)

def B(x, y): 
	return lambda z: x(y(z))

# C Combinator (Cardinal) - Equivalent to flip in Haskell.
# The C Combinator is a permuting combinator. It flips the arguments of a function.
# It is generally used when passing a partially applied function
# to another higher-order function like map or filter.
# In lambda calculus: C x y z = x z y
def C(x, y):
	return lambda z: y(x(z))
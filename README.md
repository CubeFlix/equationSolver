equationSolver
==============

An minimal equation solver written in python. This can solve single-variable linear and quadratic equations.

This design was heavily inspired by sympy, but does not use sympy. Rather, this design uses plain python, with built-in helper libraries.


How to use
==========

To use this module, `import equationSolver`, and then create a Symbol object by doing the following:

```
from equationSolver import *
x = Symbol('x') 
```

Then, this should let you simplify expressions like this:

``` print(2 * (x + 1 + 3*x)) ```

You can then solve an equation by using the solve function, as follows:

```print(solve((5*x + 1) / 2 + (2 * x + 1) / 3, 2-x)) # 7/25```

You can also solve quadratic equations:

```
print(solve(x**2 + 7*x + 6, 0)) # [-1, -6]
```

How it works
============

The way this works is that we have an object, called a `Symbol`. With the symbol, we can add and multiply, just as we do with numbers. For example, with the expression `x + x`, we get the answer `2*x`,
which really isn't a symbol anymore, but a `Term`. A term is just something like `2*x` which can be represented as `Term(2, x)`. Then, if we add something like `2` to it, we get a new object called an `Add`. The add can have infinitely many things in it, but on creation, it will attempt to simplify it's items by combining like terms. When you add `(x + 1) + (x + 2)` we get `Add([x, 1]) + Add([x, 2])`, which turns into `Add([x, 1, x, 2])` which is then simplified into `Add([2*x, 3])`. This forms the basis of all of the expressions in here. 
	To solve, for instance if we have `2*x + 1 = x`, we put it into the solve function as `solve(2*x + 1, x)`. The solve function will then turn it into the form mx+b = 0 by subtracting the right side from the left. This is `x + 1 = 0`, so we can then find the values for m and b via a loop, and come to the conclusion that x = (-1/1) = -1. 
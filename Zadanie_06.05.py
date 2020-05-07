import math
n = int(input('n = '))  # number of white balls
m = int(input('m = '))  # number of black balls
k = int(input('k = '))  # number of trials

t = n + m  # total number of balls
omega = math.factorial(t)/(math.factorial(k) * math.factorial(t - k))  # total number of elements in probability space

if n > 1:
    white = math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
else:
    white = 0  # white - possibilities for white
if m > 1:
    black = math.factorial(m) / (math.factorial(k) * math.factorial(m - k))
else:
    black = 0  # black - possibilities for black

A = white + black  # total number of possibilities
p = A/omega  # probability
print(p)

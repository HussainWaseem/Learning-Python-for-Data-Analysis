''' Cross Operations between int and float'''

# Arithmetic

a = 5 + 3.5
print(a)  # returns float. Python always retains higher representation.

b = 3 * 5.6  # Py returns with 15 decimal point precision.
print(b)

c = 3.0/2
print(c)

alfloat = 3/3
print(alfloat) # Standard Division always returns a FLOAT!!

d = 3.0//2
print(d)  # Here also float is retained but truncation is done!!
print(type(d))

e = 3.0**2
f = 2**3.0
print(e,f)  # Here also in both cases float is retained.

g = int(3.8)
h = round(3.8)  # both will return int but g will be truncated and h rounded.


print(g,h)

# comma (,) is used as a separator of values/objects.
# comma also adds a space in between while printing those objects.


''' More on Round'''
a = 158.0625
print(round(a,2)) # round a to 2 decimal places
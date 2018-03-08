''' This is Doc String '''
''' This will also work
'''

"""This Also """
"""This one too
"""

# Note there is a color difference between the doc string and a plain comment.

print("Hello" + "World")

# Concats without spacing.

new_var = 5    # decimal, base10
print(new_var)


''' Converting Different bases to decimal'''
new_var = 0b100  # 0b used for base 2 (Binary)
print(new_var)

new_var = 0o235147  #0o for base8 (Oct)
print(new_var)

new_var = 0x01265789ACDEF  #0x for base 16 (heX)
print(new_var)


''' Converting decimal to different bases'''
new_var = 256

# These functions "Return" the required value. We used print because they only returned.
print(hex(new_var))

print(oct(new_var))

print(bin(new_var))
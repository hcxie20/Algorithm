a = 0xffffffffffff
b = 0x0000000000f0
c = a | b
d = 2 & c
e = 2 & a

print("{:#x}".format(c))
print("{:#x}".format(d))
print("{:0>12x}".format(e))
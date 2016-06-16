from binascii import hexlify, unhexlify
import re
import sys
import os.path
 
def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
 
def file_len(fileName):
	with open(fileName) as f:
		return sum(1 for _ in f)

#usage: cribdragging.py inputFile 
if(len(sys.argv) != 2):
	print "Incorrect usage! Try again"
 	sys.exit()
elif(os.path.isfile(sys.argv[1])):
 	file = open(sys.argv[1], "r").read()
 	print "File succesfully opened!"
else:
	print "File not found"
	sys.exit()

ciphertexts = []
line = ""

for char in file:
	if(char != '\n'):
		line += char
	else:
		ciphertexts.append(line)
		line = ""
ciphertexts.append(line)

print "Enter line number you want to use as target:"
Targetnumber = int(raw_input())

target = ciphertexts[Targetnumber]

print "Enter index of ciphertext:"
CipherNumber = int(raw_input())

x = strxor(unhexlify(ciphertexts[CipherNumber]),unhexlify(target))
print "Ciphertext[" + str(CipherNumber) + "] xor Target (" + str(Targetnumber) + ")\n"
crib = raw_input("Enter Crib:>")
print "Crib\n~%s~"%crib

# Crib Drag
for i in range(len(x)):
    z = x[i:]
    print "\n[%d]"%i
    print "%s"%strxor(z,crib)

while True:
    print "Choose number:"
	x = strxor(unhexlify(ciphertexts[CipherNumber]),unhexlify(target))
	print "Ciphertext[" + str(CipherNumber) + "] xor Target (" + str(Targetnumber) + ")\n"
	crib = raw_input("Enter Crib:>")
	print "Crib\n~%s~"%crib

	# Crib Drag
	for i in range(len(x)):
		z = x[i:]
		print "\n[%d]"%i
		print "%s"%strxor(z,crib)
 

# if(os.path.isfile(sys.argv[1])):
# 	file = open(sys.argv[1], "r").read()
# else:
# 	print "File " + sys.argv[1] + " could not be found."
# 	sys.exit()

# print "Number of lines: " + str(file_len(sys.argv[1]))

# ciphertexts = ["",

# "",

# "",

# "",

# ""]

# target = ""

# x = strxor(unhexlify(ciphertexts[3]),unhexlify(target))
# print "Ciphertext[3] xor Target\n"
# crib = raw_input("Enter Crib:>")
# print "Crib\n~%s~"%crib

# # Crib Drag
# for i in range(len(x)):
# 	z = x[i:]
# 	print "\n[%d]"%i
# 	print "%s"%strxor(z,crib)
#  
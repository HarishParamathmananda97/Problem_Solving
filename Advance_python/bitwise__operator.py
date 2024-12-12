"""Learning bytes type and bitwise operators """
#OR ->  |
#AND -> &
#XOR -> ^
#NOT -> ~
#LeftShift ->  <<
#RightShift -> >>
 


print(0b11110000)
print(bin(240))
print(bin(0b11100100 ^ 0b00100111)) # XOR operator
print(bin(143))
print(bin(-143))
print("LeftShift")
for i in range(0, 8):
    print(f"1 << {i} = {1<< i}")

print("RightShift")
for i in range(0, 10):
    print(f"128 >> {i} = {128 >> i}")

print(bin(~0b11110000 & 0b11111111))

print(bin(~0b11110000 & 0b111111111))

print(int(32).bit_length())
print(int(143).bit_length())
print(int(256).bit_length())
print(int(-256).bit_length())

print(int(0xcafebabe).to_bytes(length=4, byteorder='big'))
print(int(0xcafebabe).to_bytes(length=4, byteorder='little'))

import sys
print(sys.byteorder)

little_cafebabe = int(0xcafebabe).to_bytes(length = 4, byteorder = sys.byteorder)
print(little_cafebabe)

int.from_bytes(little_cafebabe, byteorder = sys.byteorder)

# print(hex('_'))
try:
#overflow error:
    print(int(-241).to_bytes(2, byteorder='big'))
#can't convert negative int to unsigned 
except OverflowError as e:
    print("can't convert negative int to unsigned of 2bytes ")
else: #nobreak
    print("Learning bytes...")
finally:
    print("Pluralsight.")

print(int(-241).to_bytes(2, byteorder='little', signed=True))

print(bin((~0b11110000).to_bytes(2, byteorder='little', signed=True)[0])) #'0b1111

print(b"This is OK because it's 7-bit ASCII")

print(b"Norwegian characters like \xc5 and \xd8 which are not 7-bit ASCII") # throws syntaxError: bytes can only contain ASCII literal characters. 

#even vscode itself throws error Å, Ø Norwegian characters to print on the editor.

# over come this we use \
print(b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII")

#decoding to get the actual value of \xc5
norsk = b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII"
print(norsk.decode('latin1')) 
print(norsk[0], norsk[1], norsk[2]) # returns the bytes instead of the characters.

print(norsk[20:25]) # returns the characters while slicing.  

print(bytes())
print(bytes(5))
#A to Z
print(bytes(range(65, 65 + 26)))
#a to z
print(bytes(range(65 + 26 + 6, 65 + 26 + 6 + 26)))

try:
    print(bytes([63, 127, 255, 511]))
except ValueError as e:
    # raise ValueError from e
    print("this Value error araised becoz of overflowing 511/ 256 bits")
finally:
    print("we are mastering Advance Python.")

print(bytes('Norwegian Characters \xc5 and \xd8','utf16'))
# b'\xff\xfeN\x00o\x00r\x00w\x00e\x00g\x00i\x00a\x00n\x00 \x00C\x00h\x00a\x00r\x00a\x00c\x00t\x00e\x00r\x00s\x00 \x00\xc5\x00 \x00a\x00n\x00d\x00 \x00\xd8\x00'

print(bytes.fromhex('54686520717569636b2062726f776e20666f78206a756d7073206f7665722061206c617a7920646f67')) # print("The quick brown fox jumps over a lazy dog")

print(''.join(hex(c)[2:] for c in b'The quick brown fox jumps over a lazy dog'))

print(bytearray())
print(bytearray(5))
print(bytearray(b'Construct from a sequence of bytes'))
print(bytearray.fromhex('54686520717569636b2062726f776e20666f78206a756d7073206f7665722061206c617a7920646f67'))
pangram = bytearray(b'The quick brown fox')
pangram.extend(b' jumps over the lazy dog')

print(pangram)
print(type(pangram))

pangram[40:43] = b'god'

print(pangram[40:43])

#using list
print(pangram.upper())

words = pangram.split()
print(words)

print(bytearray(b' ').join(words))



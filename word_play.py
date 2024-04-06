""" Playing with File words.txt """

fin = open('words.txt')
# print(fin.readline()) # read single line

# print lines which has word more than 20
# for line in fin: 
#     word = line.strip()
#     if len(word) > 20:
#         print(word)

#has_no_e returns true if e doesn't present in the given word
def has_no_e(word):
    if 'e' in word:
        return False
    return True

count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        count += 1
        print(word)
print("the overall count present in the file is: ", count)
print("nothing.")

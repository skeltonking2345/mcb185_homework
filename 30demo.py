#30demo.py by skeltonking2345
import math
import sys

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print('hey' + 'buddy')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{"butt"}')
print(f'{"hello world":>20}') #puts 20 paces before hellow
print(f'{"hello world":.>20}') #puts 20 periods before hellow
print(f'{"hey":<10} {"wow"}') #puts 10 spaces after hey
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{10000000:e}')

print(s.endswith('d'))

print('%s %.3f' % ('printf', math.pi))
print('%s %.3f' % ('printf', 300.46789))

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
    print(nt, end='') #to combine the multiple letters into one line
print() #to start a new line

for i in range(len(seq)):
    print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[2:8]) #2 to 8 in sequence s

print(s[0:8:2]) #0 to 8 in sequence s skipping by 2

print(s[8:]) #everything after 8th letter

print(s[:5]) #start from beginning until 5

print(s, s[::], s[::1], s[::-1]) #-1 starts at the end and goes downward sequentually

dna = 'ATGCTGAA'
for i in range(0, len(dna), 3): #within dna, from range 0 to total number, skipping by 3s
    codon = dna[i:i+3] #codon will display the letter coresponding with i , i+1, i+2, i+3
    print(i, codon) #print i (number), and the foresponging 3 values for codon

#tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts): # i acts as the position, like len, and nt acts like nts[i]
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(i, nts[i], names[i])

for nt, name in zip(nts, names):# the for loop assigns things to the zip, so it would have a, b, c, ...n (with n being the number of things in the zip)
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name) 

nts = ['A', 'T', 'C']
print(nts)

nts[2] = 'G' #mutable means it can be changed as opposed to tuples, in this case C->G
print(nts)

nts.append('C')#append adds to the end of the list
print(nts)

last = nts.pop()
print(last)
print(nts)

nts.sort()
print(nts) #sorted in ascii order
nts.sort(reverse=True)
print(nts) #sorted in reverse ascii order

nucleotides = nts #this is not copying it is just assigning another name
nucleotides.append('C') #this is also appending nts
nucleotides.sort() #also sorting nts
print(nts, nucleotides) #both are the exact same because you edit both

items = list() #empty list
print(items)
items.append('eggs') #adds eggs to end of list
print(items)

stuff = [] #empty list
stuff.append(3) #add 3 to end of list
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRS'
print(alph) #just some randm string
aas = list(alph) #convert entire string into list with each letter separated
print(aas)

text = 'good day    to you'
print(text)
words = text.split()
print(words) #all spaces are considered

line = '1.41,2.72,3.14'
print(line.split(',')) #set what the split uses

s = '-'.join(aas) #().join sets how lists are joined together, in this case with a (-)
print(s)
s = ''.join(aas) #this list is joined by nothing so they are just put together seamlessly
print(s)

if 'A' in alph: print('yaaaay') #if A exists in alph, print yay
if 'a' in alph: print('naaaay') #if a exists in alph print nay

print('index G', alph.index('G'))
#print('index Z', alph.index('Z')) [this does not work due to z not existing in this list]

print('find G?', alph.find('G')) #finds first occurance of G, and outputs the index
print('find Z?', alph.find('Z')) #if it cannot find anything, displays -1

#practice problems

#i cheated with this first one

def minimum(vals):
    min = vals[0]
    for val in vals[1:]:
        if val < min: min = val
    return min
num = [5, 2, 6, 7, 8]
print(minimum(num))

def minandmax(vals):
    min = vals[0]
    max = vals[-1]
    for val1 in vals[1:]:
        if val1 < min: min = val1
    for val2 in vals[-2::-1]:
        if val2 > max: max = val2
    return min, max

print(minandmax(num))

def mean(vals):
    #men = sum(vals) / len(vals)
    #without using sum
    sums = 0
    for i in vals: sums += i
    men = sums / len(vals)
    return men

print(mean(num))

curve = [.3, .6, .2, .5, .7]

def entropy(prob):
    total = 0
    for i in prob:
        total += (i * math.log2(i))
    return -total

print(entropy(curve))

def kuleib(prob1, prob2):
    total = 0
    for i, j in zip(prob1, prob2):
        total += i * math.log2(i / j)
    return total

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(kuleib(p1, p2))

print(sys.argv)

i = int('42')
#x = float('0.61803')
x = float('hello')

print(i * x)


# print("Enter production like this S:aA|b|è\nTo stop enter done")
# data = []

# while True:
#     t = input("Enter Production : ")
#     if(t.strip().lower() == "done"):
#         break
#     left, r = t.split(':')
#     right = r.split('|')

#     data.append([left, right])

def find(arr , value):
    for i in arr:
        if i == value:
            return True
    
    return False


# data = [ ['S', ['aBh', 'Ce']], ['B', ['cC']], ['C', ['bd', 'è']] ]

# first = {
#     "aBh" : ['a'],
#     "Ce" : ['b', 'e'],
#     'cC': ['c'],
#     'bd' : ['b'], 
# }

# follow = {
#     "S" : ['$'],
#     'B' : ['h'],
#     'C' : ['e', 'h']
# }

data = [ ['E', ['TA']], ['A', ['aTA', 'è']], ['T', ['FB']], ['B', ['bFB', 'è']], ['F', ['c', 'dEf']] ]

first = {
    "TA" : ['d', 'c'],
    "aTA" : ['a'],
    'FB': ['c', 'd'],
    'bFB' : ['b'],
    'c' : ['c'],
    'dEf' : ['d'] 
}

follow = {
    "E" : ['$', 'f'],
    'A' : ['$', 'f'],
    'T' : ['a', '$', 'f'],
    'B' : ['a', '$', 'f'],
    'F' : ['b', 'a' , '$', 'f']

}

terminals = []
nonT = []

for i in range(len(data)):
    nonT.append(data[i][0])
    
    for j in data[i][1]:
        for k in j:
            if k.islower() and k != 'è' and not find(terminals, k):
                terminals.append(k)

terminals.append("$")

print("Terminals : ", " ".join(terminals))
print("\nFirst :")
for k, v in first.items():
    print(k, " -> " ," ,".join(v))

print("\nFollow :")

for k, v in follow.items():
    print(k, " -> " , " ,".join(v))

table = {}

for i in range(len(nonT)):
    table[nonT[i]] = {}
    for j in terminals:
        table[nonT[i]][j] = []

# print(table)

for i in range(len(data)):
    
    left = data[i][0]
    right = data[i][1]

    for j in right:
        if j == "è":
            for itr in follow[left]:
                table[left][itr].append(f'{left}->{j}')
        else:
            for itr in first[j]:
                table[left][itr].append(f'{left}->{j}')


print("\nParsing Table :")


for i in terminals:
    print(f" \t{i}", end="")

print()

for non_term in nonT:
    print(non_term, end="\t")
    for term in terminals:
        productions = table[non_term][term]
        if productions:
            print(" ".join(productions), end="")
        print("\t", end="")
    print()

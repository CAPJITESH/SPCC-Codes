import re

start_sym=""
productions={}
first_table={}
follow_table={}
table={}

file='/Users/jiteshgogia/Desktop/Books/SPCC/Codes/first.txt'
grammer=open(file,"r")

def createProductions(grammer):
  global start_sym
  for production in grammer:
    lhs,rhs=production.split("->")
    rhs=re.split("\||\n",rhs)
    productions[lhs]=set(rhs)-{''}
    print(productions)
    if not start_sym:
      start_sym=lhs


def isNonTerminal(sym):
  if sym.isupper():
    return True
  else:
    return False

def firstFunc(sym):
    if sym in first_table:
        return first_table[sym]
    if isNonTerminal(sym):
        first = set()
        for x in productions[sym]:
          if x == '#':
                first = first.union('#')
          else:
                for i in x:
                    fst = firstFunc(i)
                    if i != x[-1]:
                        first = first.union(fst - {'#'})
                    else:
                        first = first.union(fst)
                    if '#' not in fst:
                        break
        return first
    else:
        return set(sym)

def follow_func(sym):
    if sym not in follow_table:
        follow_table[sym] = set()

    for nt in productions.keys():

        for rule in productions[nt]:

            pos = rule.find(sym)
            if pos != -1:
                while pos < len(rule):
                    if pos == len(rule) - 1:
                        if nt != sym:
                            follow_table[sym] = follow_table[sym].union(follow_func(nt))
                            break
                    else:
                        pos += 1
                        next_symbol = rule[pos]
                        if isNonTerminal(next_symbol):
                            if '#' not in firstFunc(next_symbol):
                                follow_table[sym] = follow_table[sym].union(firstFunc(next_symbol))
                                break
                            
                            if '#' in firstFunc(next_symbol):
                                follow_table[sym] = follow_table[sym].union(firstFunc(next_symbol) - {'#'})
                           
                        else:
                            follow_table[sym].add(next_symbol)
                            break
    return follow_table[sym]



def printTable():
  print("First")
  for nt in productions:
    print(nt+":"+str(first_table[nt]))
    print("\n")
  print("Follow")
  for nt in productions:
    print(nt+':'+str(follow_table[nt]))



createProductions(grammer)
for nt in productions:
  first_table[nt]=firstFunc(nt)
print(first_table)
follow_table[start_sym]=set('$')
for nt in productions:
  follow_table[nt]=follow_func(nt)
printTable()
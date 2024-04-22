# print("Enter production like this S:aA|b|è\nTo stop enter done")
# data = []

# while True:
#     t = input("Enter Production : ")
#     if(t.strip().lower() == "done"):
#         break
#     left, r = t.split(':')
#     right = r.split('|')

#     data.append([left, right])


data = [  ['E',['TA']],
    ['A',['aTA','è']],
    ['T',['FB']],
    ['B',['bFB','è']],
    ['F',['c','dEf']],
]
# data = [['S', ['ACB', 'CbD', "Ba"]], ['A', ['da', 'BC']], ['B',['g', "è"]], ['C',['h', "è"]]]

first = {}

for i in range(len(data) - 1 , -1, -1):
    l = data[i][0]
    r = data[i][1]

    temp_f = set()

    for j in r:
        for count,k in enumerate(j):
            if(k.islower() or k == 'è'):
                temp_f.add(k)
                break
            else:
                if 'è' not in first[k]:
                    for itr in first[k]:
                        temp_f.add(itr)
                    break
                else:
                    for itr in first[k]:
                        temp_f.add(itr)
                    if count == len(k) - 1 :
                        temp_f.add("è")
    
    first[l] = temp_f
print("First")
print(first)


follow = {}

for i in range(len(data)):
    left = data[i][0]
    temp_follow = set()

    if(i == 0):
        temp_follow.add("$")

    for j in range(len(data)):
        for k in data[j][1]:
            index = k.find(left)

            if index == -1:
                continue

            # NT at end
            if index == len(k) - 1:
                if left != data[j][0]:
                    for ele in follow[data[j][0]]:
                        temp_follow.add(ele)

            # T after NT in follow
            elif k[index + 1].islower():
                temp_follow.add(k[index + 1])

            # NT after NT in follow
            else:
                next_index = index + 1
                while next_index < len(k):
                    next_symbol = k[next_index]
                    if next_symbol.islower():
                        temp_follow.add(next_symbol)
                        break
                    else:
                        for ele in first[next_symbol]:
                            if ele != 'è':
                                temp_follow.add(ele)
                        if 'è' not in first[next_symbol]:
                            break
                        next_index += 1
                if next_index == len(k):
                    if left != data[j][0]:
                        for ele in follow[data[j][0]]:
                            temp_follow.add(ele)

    follow[left] = temp_follow

print("Follow : ")
print(follow)
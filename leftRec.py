# print("Enter production like this S:aA|b|è\nTo stop enter done")
# data = []

# while True:
#     t = input("Enter Production : ")
#     if(t.strip().lower() == "done"):
#         break
#     left, r = t.split(':')
#     right = r.split('|')

#     data.append([left, right])

# data = [ ['X', ['X1','Y1','0']], ['Y', ['Y0', 'X1', '0']]]

# for i in range(len(data)):

#     left = data[i][0]
#     right = data[i][1]

#     alpha = []
#     beta = []   

#     for j in right:
#         index = j.find(left)
#         print(left, j[0])
#         if index == -1:
#             beta.append(j)
#         else:
#             alpha.append(j[1:len(j):])

#     temp = []
#     temp1 = []

#     if len(alpha) > 0:
#         for itr in beta:
#             temp.append(f"{itr}{left}^")
        
#         for itr in alpha:
#             temp1.append(f"{itr}{left}^")
        
#         temp1.append("è")

#         data[i][1] = temp
#         data.append([f"{left}^", temp1])

#         for itr in range(len(data)):

#             l = data[itr][0]
#             r = data[itr][1]

#             for k in r:
#                 index = k.find(f'{left}')
#                 if index != -1 and k.find(f'{left}^') == -1:
#                     temp_data = k

#                     for u in data[i][1]:
#                         temp_data.replace(left, u)
#                         uniq = {}
#                         for c,t in enumerate(temp_data):
#                             if t not in uniq:
#                                 uniq[t] = c

#                         data[itr][1].append("".join(uniq.keys()))

# print(data)
            

data = [['X', ['X1', 'Y1', '0']], ['Y', ['Y0', 'X1', '0']]]

for i in range(len(data)):

    left = data[i][0]
    right = data[i][1]

    alpha = []
    beta = []

    for j in right:
        index = j.find(left)
        if index == -1:
            beta.append(j)
        elif index == 0:
            alpha.append(j[1:])

    temp = []
    temp1 = []

    if len(alpha) > 0:
        for itr in beta:
            temp.append(f"{itr}{left}^")

        for itr in alpha:
            temp1.append(f"{itr}{left}^")

        temp1.append("è")

        data[i][1] = temp
        data.append([f"{left}^", temp1])

        for itr in range(i,len(data)):

            l = data[itr][0]
            r = data[itr][1]

            for k in r:
                index = k.find(left)
                if index != -1 and k.find(f'{left}^') == -1:
                    # temp_data = k.replace(left, f"{left}^")

                    for g in data[i][1]:
                        temp_data = k.replace(left, g)

                        uniq = {}
                        for c, t in enumerate(temp_data):
                            if t not in uniq:
                                uniq[t] = c
                        data[itr][1].append("".join(uniq.keys()))

                    data[itr][1].remove(k)
                    # print('\n',left,data[itr][1], "\n")

print(data)




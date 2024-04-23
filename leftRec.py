data = [
    ['A', ['C','d']],
    ['B', ['C','e']],
    ['C', ['A','B','f']],
]

def timepass(left,ind):

    copy = {}
    for i in range(ind + 1, len(data)):

        if data[i][0] == left:
            continue
        else:
            l = data[i][0]
            r = data[i][1]

            for itr in r:
                if left == itr[0] and itr.find(f'{left}^') == -1:
                    # print(left, itr[0])
                    for g in data[ind][1]:

                        temp_data = itr.replace(left, g)
                        # print(temp_data)

                        uniq = {}
                        for c, t in enumerate(temp_data):
                            if t not in uniq:
                                uniq[t] = c
                        # print(" ".join(uniq.keys()))
                        
                        if i not in copy.keys():
                            copy[i] = []
                        
                        copy[i].append("".join(uniq.keys()))
                    
                    data[i][1].remove(itr)
    
    for k, v in copy.items():
        for j in v:
            if j not in data[k][1]:
                data[k][1].append(j)
                    
    


# data = [['X', ['X1', 'Y1', '0']], ['Y', ['Y0', 'X1', '0']]]

for i in range(len(data)):

    left = data[i][0]
    right = data[i][1]

    alpha = []
    beta = []

    timepass(left, i)

    # print(data)

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

        # for itr in range(i,len(data)):

        #     l = data[itr][0]
        #     r = data[itr][1]

        #     for k in r:
        #         index = k.find(left)
        #         # For not replacing anything from ^ wale productions
        #         if index != 0 and k.find(f'{left}^') == -1 and k.find('^') == -1:
        #             # temp_data = k.replace(left, f"{left}^")

        #             for g in data[i][1]:
        #                 temp_data = k.replace(left, g)

        #                 uniq = {}
        #                 for c, t in enumerate(temp_data):
        #                     if t not in uniq:
        #                         uniq[t] = c
        #                 data[itr][1].append("".join(uniq.keys()))

        #             data[itr][1].remove(k)
        #             # print('\n',left,data[itr][1], "\n")

print(data)




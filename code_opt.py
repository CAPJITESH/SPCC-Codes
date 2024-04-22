# data = []
# print("Format is t1=a + b")
# while True:

#     t = input("Enter production : ")
#     if t.strip().lower() == "done":
#         break
#     data.append(t)

# Common subexpression removal technique

data = [
    't1=a+b',
    't2=5',
    't3=a+b',
    't4=5+t3',
    't5=a+b',
    't6=a+t2',
]

def tempF(code, removed):

    for k, v in removed.items():
        if k not in code:
            continue
        else:
            return [k, v]

    return []
            
def solve(data):

    temp = {}

    removed = {}

    for i in data:

        index = i.find('=')
        name = i[0:index:].strip()
        code = i[index + 1:len(i):]

        t = tempF(code, removed)
        if len(t) != 0:
            code = code.replace(t[0], t[1])

        if code not in temp.values():
        
            temp[name] = code
        else:

            key = ""
            for k, v in temp.items():
                if v == code:
                    key = k
                    break
            # print(name, '  ', key)

            removed[name] = key
    
    return temp

ans = solve(data)
count = int(0)
for k, v in ans.items():
    print(f't{count + 1}=', end='')
    
    for k1, v1 in ans.items():
        ans[k1] = ans[k1].replace(k, f"t{count + 1}")
    count = count + 1
    print(f' {v}')

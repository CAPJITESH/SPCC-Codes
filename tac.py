def is_expression(c):
    return c in ['+', '-', '/', '*']

def main():
    exp = "a*-b+c"
    st = []
    mp = {}
    n = len(exp)
    count = 1
    
    for i in range(n - 1, -1, -1):
        
        if is_expression(exp[i]) and len(st) > 0 and is_expression(st[0]):
            e = st.pop(0)
            c = st.pop(0)

            temp = e+c
            key = 't' + str(count)
            count += 1
            mp[key] = temp
            st.insert(0, key)
            st.insert(0, exp[i])

        elif not is_expression(exp[i]) and len(st) > 0 and is_expression(st[0]):
            e = st.pop(0)
            c = st.pop(0)
            key = 't' + str(count)
            count += 1
            mp[key] = exp[i] + e + c
            st.insert(0, key)
        else:
            st.insert(0, exp[i])
    
    for key, value in mp.items():
        print(key, value)

if __name__ == "__main__":
    main()

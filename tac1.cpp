#include <bits/stdc++.h>
using namespace std;

unordered_map<char, int> op;

bool isVariable(char c)
{
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z');
}

bool isOperator(char c)
{
    return op.count(c);
}

int main()
{
    // freopen("input.txt", "r", stdin);



    op['('] = 5;
    op['*'] = 4;
    op['/'] = 3;
    op['+'] = 2;
    op['-'] = 1;
    op['$'] = 0;

    string input;
    cin >> input;

    int n = input.size();

    int counter = 0;

    string newInput = "";
    // handeling the uniary minus
    int i;
    for (i = 0; i < n - 1; i++)
    {
        if (i == 0 and input[i] == '-' and isVariable(input[i + 1]))
        {
            newInput.push_back(char('A' + counter++));
            cout << newInput.back() << " = "
                 << "-" << input[i + 1] << endl;
            i++;
        }
        else if (i + 2 < n and input[i + 1] == '-' && isOperator(input[i]) && isVariable(input[i + 2]))
        {
            newInput.push_back(input[i]);
            newInput.push_back(char('A' + counter++));
            cout << newInput.back() << " = "
                 << "-" << input[i + 2] << endl;
            i += 2;
        }
        else
        {
            newInput.push_back(input[i]);
        }
    }
    if (i < n)
        newInput.push_back(input.back());
    input = newInput;

    cout << input << endl;

    // infix to postfix
    stack<char> st;
    st.push('$');
    string postfix = "";

    for (int i = 0; i < input.size(); i++)
    {
        if (input[i] == '(')
        {
            st.push(input[i]);
            continue;
        }
        if (input[i] == ')')
        {
            while (st.top() != '(')
            {
                postfix.push_back(st.top());
                st.pop();
            }
            st.pop();
            continue;
        }
        if (isVariable(input[i]))
        {
            postfix.push_back(input[i]);
            continue;
        }

        while (st.size() > 1 and st.top() != '(' and op[st.top()] >= op[input[i]])
        {
            postfix.push_back(st.top());
            st.pop();
        }
        st.push(input[i]);
    }
    while (st.size() > 1)
    {
        postfix.push_back(st.top());
        st.pop();
    }

    // cout << postfix << endl;

    for (int i = 0; i < postfix.size(); i++)
    {
        if (isVariable(postfix[i]))
        {
            st.push(postfix[i]);
            continue;
        }

        char op = postfix[i];
        char c2 = st.top();
        st.pop();
        char c1 = st.top();
        st.pop();

        st.push('A' + counter);
        cout << char('A' + counter++) << " = " << c1 << op << c2 << endl;
    }
}
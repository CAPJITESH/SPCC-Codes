// #include <bits/stdc++.h>


// using namespace std;

// unordered_map<char, int> op;

// bool isVariable(char c)
// {
//     return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z');
// }

// bool isOperator(char c)
// {
//     return op.count(c);
// }


// bool isExpression(char c) {
//     return c == '+' || c == '-' || c == '/' || c == '*' || c == '=';
// }

// int main() {

//     op['('] = 5;
//     op['*'] = 4;
//     op['/'] = 3;
//     op['+'] = 2;
//     op['-'] = 1;
//     op['$'] = 0;


//     string exp = "a*-b+c";
//     stack<char> st;
//     vector<pair<string,string> > mp;
//     int n = exp.size();
//     int count = 1;

//     unordered_map<char, string> temp;


//     int temp_counter = 0;
//     for (int i = n - 1; i >=0; i--) {
//         if (i - 1 >= 0 && isExpression(exp[i]) && isExpression(exp[i - 1])) {
//             char key = 'z' - temp_counter;
            
//             // Convert the character key to a string
//             string key_str(1, key);

//             temp[key] = exp.substr(i, 2);

//             // Replace the substring with the string key
//             exp.replace(i, 2, key_str);

//             temp_counter++;
//         }
//     }
//     cout<<exp<<endl;

//     string postfix = "";

//     for(int i = 0; i < exp.size(); i++){

//         if(exp[i] == '('){
//             st.push(exp[i]);
//             continue;
//         }
//         else if (exp[i] == ')'){
//             while(st.top() != '('){
//                 postfix.push_back(st.top());
//                 st.pop();
//                 continue;
//             }
//         }
//         else if (isVariable(exp[i])){
//             postfix.push_back(exp[i]);
//             continue;
//         }

//         while(!st.empty() && st.top() != '(' and op[st.top()] >= op[exp[i]]){
//             postfix.push_back(st.top());
//             st.pop();
//         }
//         st.push(exp[i]);
//     }

//     while(!st.empty()){
//         postfix.push_back(st.top());
//         st.pop();
//     }

//     cout<<postfix<<endl;

//     int counter = 1;
//     stack<string> s;

//     for(int i = 0; i < postfix.size(); i++){
        
//         char c2 = st.top();  st.pop();
        
//         if(temp.find(c2) != temp.end()){
//             string key = "t" + to_string(counter++);
//             cout<< key<< " : " << temp[c2]<<endl;
//             s.push(key);
//             continue;
//         }
//         else{
//             s.push(string(1, c2));
//         }
//         char c1 = st.top();  st.pop();

//         if(temp.find(c1) != temp.end()){
//             string key = "t" + to_string(counter++);
//             cout<< key<< " : " << temp[c1]<<endl;
//             s.push(key);
//             continue;
//         }
//         else{
//             s.push(string(1, c1));
//         }
//         if(isVariable(postfix[i])){
//             s.push(string(1, postfix[i]));
//             continue;
//         }
       
//         char op = postfix[i];
//         string k = "t" + to_string(counter++); 
//         s.push(k);

//         cout<<k << " : "<<c1<<op<<c2<<endl;  

//     }


//     return 0;
// }

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


bool isExpression(char c) {
    return c == '+' || c == '-' || c == '/' || c == '*' || c == '=';
}

int main() {

    op['('] = 5;
    op['*'] = 4;
    op['/'] = 3;
    op['+'] = 2;
    op['-'] = 1;
    op['$'] = 0;


    string exp = "a*-b+c";
    stack<char> st;
    vector<pair<string,string> > mp;
    int n = exp.size();
    int count = 1;

    unordered_map<char, string> temp;


    int temp_counter = 0;
    for (int i = n - 1; i >=0; i--) {
        if (i - 1 >= 0 && isExpression(exp[i]) && isExpression(exp[i - 1])) {
            char key = 'z' - temp_counter;
            
            // Convert the character key to a string
            string key_str(1, key);

            temp[key] = exp.substr(i, 2);

            // Replace the substring with the string key
            exp.replace(i, 2, key_str);

            temp_counter++;
        }
    }
    cout<<exp<<endl;

    string postfix = "";

    for(int i = 0; i < exp.size(); i++){

        if(exp[i] == '('){
            st.push(exp[i]);
            continue;
        }
        else if (exp[i] == ')'){
            while(st.top() != '('){
                postfix.push_back(st.top());
                st.pop();
            }
            st.pop(); // Pop the '('
            continue;
        }
        else if (isVariable(exp[i])){
            postfix.push_back(exp[i]);
            continue;
        }

        while(!st.empty() && st.top() != '(' and op[st.top()] >= op[exp[i]]){
            postfix.push_back(st.top());
            st.pop();
        }
        st.push(exp[i]);
    }

    while(!st.empty()){
        postfix.push_back(st.top());
        st.pop();
    }

    cout<<postfix<<endl;

    int counter = 1;
    stack<string> s;

    for(int i = 0; i < postfix.size(); i++){
        if(isVariable(postfix[i])){
            string variable(1, postfix[i]);
            s.push(variable);
            continue;
        }
        string c2 = s.top();  s.pop();
        string c1 = s.top();  s.pop();

        if(temp.find(c2[0]) != temp.end()){
            string key = "t" + to_string(counter++);
            cout<< key<< " : " << temp[c2[0]]<<endl;
            s.push(key);
            
        }
        else{
            s.push(c2);
        }

        if(temp.find(c1[0]) != temp.end()){
            string key = "t" + to_string(counter++);
            cout<< key<< " : " << temp[c1[0]]<<endl;
            s.push(key);
        }
        else{
            s.push(c1);
        }

        string op = string(1, postfix[i]);
        string k = "t" + to_string(counter++); 
        s.push(k);

        cout<<k << " : "<<c1<<op<<c2<<endl;  
    }

    return 0;
}

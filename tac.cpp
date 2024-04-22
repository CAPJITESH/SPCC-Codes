// #include <bits/stdc++.h>
// using namespace std;

// bool isExpression(char c) {
//     return c == '+' || c == '-' || c == '/' || c == '*';
// }

// int main() {
//     string exp = "a*-b+c";
//     stack<string> st;
//     unordered_map<string, string> mp;
//     int n = exp.size();
//     int count = 1;

//     for (int i = n - 1; i >= 0; i--) {
//         if (!st.empty() && isExpression(exp[i]) && isExpression(st.top()[0])) {
//             string e = st.top();    st.pop();
//             string c = st.top();    st.pop();

//             string temp = e + c;
            
//             string key = "t" + to_string(count++);
            
//             mp[key] = temp;
            
//             st.push(key);
//             st.push(string(1, exp[i]));
        
//         } else if (!st.empty() && !isExpression(exp[i]) && isExpression(st.top()[0])) {
        
//             string e = st.top(); st.pop();
//             string c = st.top(); st.pop();
        
//             string key = "t" + to_string(count++);
        
//             mp[key] = exp[i] + e + c;
//             st.push(key);
        
//         } else {
//             st.push(string(1, exp[i]));
//         }
//     }

//     for (const auto i : mp) {
//         cout << i.first << " " << i.second << endl;
//     }

//     return 0;
// }

#include <bits/stdc++.h>


using namespace std;

bool isExpression(char c) {
    return c == '+' || c == '-' || c == '/' || c == '*' || c == '=';
}

int main() {
    string exp = "a*-b+c";
    stack<string> st;
    vector<pair<string,string> > mp;
    int n = exp.size();
    int count = 1;

    for (int i = n - 1; i >= 0; i--) {
        if (!st.empty() && isExpression(exp[i]) && isExpression(st.top()[0])) {
            string e = st.top();    st.pop();
            string c = st.top();    st.pop();

            string temp = e + c;
            
            string key = "t" + to_string(count++);
            
            mp.push_back(make_pair(key, temp));
            // mp[key] = temp;
            
            st.push(key);
            st.push(string(1, exp[i]));
        
        } else if (!st.empty() && !isExpression(exp[i]) && isExpression(st.top()[0])) {
        
            string e = st.top(); st.pop();
            string c = st.top(); st.pop();
        
            string key = "t" + to_string(count++);

            mp.push_back(make_pair(key, exp[i] + e + c));
            // mp[key] = exp[i] + e + c;
            st.push(key);
        
        } else {
            st.push(string(1, exp[i]));
        }
    }
    
   for ( int i = 0; i < mp.size(); i++){
    cout<< mp[i].first << "\t" << mp[i].second << endl;
   }

    return 0;
}


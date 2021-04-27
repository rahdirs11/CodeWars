/*
This is basically a cipher problem where the key is rot13
i.e. you shift the letters by 13 to the right, and the key is
for exclusively for letters!
*/

#include <iostream>
#include <string>
// #include <cctype>

using namespace std;

string rot13(string msg) {
    string result {};
    for (int x = 0; x < msg.length(); ++x) {
        int i = msg[x];
        if (i >= 65  && i <= 90) {
            if (i > 77) {
                result.push_back(i + 13 - 26);
            } else {
                result.push_back(i + 13);
            }
        } else if (i >= 97 && i <= 122) {
            if (i > 109) {
                result.push_back(i + 13 - 26);
            } else {
                result.push_back(i + 13);
            }
        } else {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    string msg {};
    getline(cin, msg);
    cout << rot13(msg) << endl;
    return 0;
}

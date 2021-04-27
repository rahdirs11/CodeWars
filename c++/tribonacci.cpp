#include <vector>
#include <iostream>
using namespace std;

vector<int> tribonacci(vector<int> signauture, int n) {
    if (n == 0) return NULL;
    vector<int> output;
    if (n <= 3) {
        for (int i = 0; i < n; ++i) {
            output.push_back(signature.at(i));
        }
        return output;
    }
    for (int i = 0; i < 3; ++i) output.push_back(signature.at(i));
    int f{signature.at(0)}, s{signature.at(1)}, t{signature.at(2)}, next{};
    for (int i = 0; i < n - 3; ++i) {
        next = f + s + t;
        int temp1 = s, temp2 = t;
        t = next;   s = temp2;  f = temp1;
        output.push_back(next);
    }
    return output;
}

/*
This is basically finding the sum of the digits repeatedly,
as long as the sum is not a single-digit number
*/

#include <iostream>
using namespace std;

int digitalRoot(int n) {
    int temp{n}, sum{};
    while (temp > 0) {
        sum += temp % 10;
        temp /= 10;
    }
    return (sum / 10 == 0)? sum: digitalRoot(sum);
}

int main() {
    int n{};
    cin >> n;
    cout << digitalRoot(n) << endl;
    return 0;
}

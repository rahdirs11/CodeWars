/*
This is basically 4 * (sum of n + 1 fibonacci terms starting with 1)
*/
#include <vector>
#include <iostream>
using namespace std;

typedef unsigned long long ull;
class SumFct
{
  public:
  static ull perimeter(int n);
};
int fibSum(int n) {

    if (n + 1 <= 1) return 1;
    ull first {1}, second {1}, sum {};
    int t {n + 1};
    sum += first + second;
    // cout << first << ' ' << second << ' ';
    while (t > 2) {
        ull temp = first + second;
        first = second; second = temp;
        sum += temp;
        // cout << second << ' ';
        --t;
    }
    // cout << endl;
    return sum;

}

ull SumFct::perimeter(int n) {

    return 4 * fibSum(n);
}

int main() {
    int n{};
    cin >> n;
    // cout << fibSum(n) << endl;
    SumFct obj;
    cout << obj.perimeter(n) << endl;
    return 0;
}

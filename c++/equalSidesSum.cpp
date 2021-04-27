#include <vector>
#include <iostream>
using namespace std;

int findSum(size_t low, size_t high, const vector<int> numbers) {
  int sum{};
  for (size_t i = low; i <= high; ++i)
    sum += numbers.at(i);
  cout << "Sum :\t" << sum << endl;
  return sum;
}


int find_even_index (const vector <int> numbers) {
  size_t length = numbers.size();
  size_t n = (length - 1) / 2;

  while (!(n > numbers.size() || n < 0)) {
    cout << "Index n:\t" << n << endl;
    int leftSum = findSum(0, n - 1, numbers);
    int rightSum = findSum(n + 1, length - 1, numbers);
    cout << "Left sum:\t" << leftSum << "\nRight sum:\t" << rightSum << endl;
    if (leftSum == rightSum) return n;
    else if (leftSum < rightSum)  n += 1;
    else  n -= 1;
  }
  return -1;
}

int main() {
    int n{}, num{};
    cin >> n;
    vector<int> numbers(n);
    for (size_t i = 0; i < n; ++i) {
        cin >> numbers.at(i);
    }
    cout << "Elements ->\n";
    for (auto itr: numbers) cout << itr << ' ';
    cout << endl;
    cout << find_even_index(numbers) << endl;
    return 0;
}

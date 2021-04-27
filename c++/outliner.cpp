#include <iostream>
#include <vector>
using namespace std;

int FindOutlier(vector<int> arr) {
	int l{}, r{arr.size() - 1};
	if (arr.at(l) % 2 != 0 && arr.at(r) % 2 == 0) {
		if (arr.at(r - 1) % 2 == 0) return arr.at(l);
		else	return arr.at(r);
	} else if (arr.at(l) % 2 == 0 && arr.at(r) % 2 != 0) {
		if (arr.at(r - 1) % 2 != 0)	return arr.at(l);
		else	return arr.at(r);
	}
	if (arr.size() % 2 == 0) {
		++l;	--r;
		while (l < r) {
			if (arr.at(l) % 2 == 0 && arr.at(r) % 2 != 0) {
				return arr.at(l + 1) % 2 == 0? arr.at(r): arr.at(l);
			} else if (arr.at(l) % 2 != 0 && arr.at(r) % 2 == 0) {
				return arr.at(l + 1) % 2 != 0? arr.at(r): arr.at(l);
			}		
			++l;	--r;
		}
	} else {
		int mid = n / 2, l{mid - 1}, r{mid + 1};
		

	}
}

int main() {
	// vector<int> one = {2, 3, 4}

	cout << "Outliner :\t" << FindOutlier({2, 4, 0, 100, 4, 11, 2602, 36}) << endl;

	return 0;
}
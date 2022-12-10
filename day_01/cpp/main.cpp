#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int total_cal = 0, i = 0;
    string s;

    vector<int> elves;

    while (getline(cin, s))
    {
        if (s.empty())
        {
            elves.push_back(total_cal);
            total_cal = 0;
        }
        else
        {
            total_cal += stoi(s);
        }
    }

    elves.push_back(total_cal);
    total_cal = 0;

    sort(elves.begin(), elves.end(), greater<>());

    // Part 1
    cout << elves[0] << endl;

    // Part 2
    cout << elves[0] + elves[1] + elves[2] << endl; 
}
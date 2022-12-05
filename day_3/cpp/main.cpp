#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int total_points = 0;
    string s, s1, s2;
    

// Part 1
    // while (getline(cin, s))
    // {
    //     s1 = s.substr(0, s.length()/2);
    //     s2 = s.substr(s.length()/2, s.length()/2);

    //     map<char, int> count;
    //     for (int i=0; i < s1.length(); i++)
    //         count[s1[i]] = 1;
        
    //     for (int i=0; i < s2.length(); i++)
    //         if(count.count(s2[i]) != 0) {
    //             count[s2[i]] += 1;
    //             total_points += (!islower(s2[i]))*26 + tolower(s2[i]) - 'a' + 1;
    //             break;
    //         }
    // }

// Part 2
    while (getline(cin, s))
        {
            getline(cin, s1);
            getline(cin, s2);

            map<char, int> count;
            for (int i=0; i < s.length(); i++)
                count[s[i]] = 1;

            
            
            for (int i=0; i < s1.length(); i++)
                if(count.count(s1[i]) != 0) {
                    count[s1[i]] = 2;
                }

            
            for (int i=0; i < s2.length(); i++)
                if(count[s2[i]] == 2) {
                    count[s2[i]] = 3;
                    cout << s2[i] << endl;
                    total_points += (!islower(s2[i]))*26 + tolower(s2[i]) - 'a' + 1;
                    break;
                }
        }

    cout << total_points << endl;
}
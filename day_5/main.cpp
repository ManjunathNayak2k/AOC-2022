#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int total_points = 0;
    string s;
    vector<stack<char>> stacks = vector<stack<char>> (10);

    stacks[1].push('S');
    stacks[1].push('C');
    stacks[1].push('V');
    stacks[1].push('N');

    stacks[2].push('Z');
    stacks[2].push('M');
    stacks[2].push('J');
    stacks[2].push('H');
    stacks[2].push('N');
    stacks[2].push('S');

    stacks[3].push('M');
    stacks[3].push('C');
    stacks[3].push('T');
    stacks[3].push('G');
    stacks[3].push('J');
    stacks[3].push('N');
    stacks[3].push('D');
    
    stacks[4].push('T');
    stacks[4].push('D');
    stacks[4].push('F');
    stacks[4].push('J');
    stacks[4].push('W');
    stacks[4].push('R');
    stacks[4].push('M');

    stacks[5].push('P');
    stacks[5].push('F');
    stacks[5].push('H');
    
    stacks[6].push('C');
    stacks[6].push('T');
    stacks[6].push('Z');
    stacks[6].push('H');
    stacks[6].push('J');

    stacks[7].push('D');
    stacks[7].push('P');
    stacks[7].push('R');
    stacks[7].push('Q');
    stacks[7].push('F');
    stacks[7].push('S');
    stacks[7].push('L');
    stacks[7].push('Z');

    stacks[8].push('C');
    stacks[8].push('S');
    stacks[8].push('L');
    stacks[8].push('H');
    stacks[8].push('D');
    stacks[8].push('F');
    stacks[8].push('P');
    stacks[8].push('W');

    stacks[9].push('D');
    stacks[9].push('S');
    stacks[9].push('M');
    stacks[9].push('P');
    stacks[9].push('F');
    stacks[9].push('N');
    stacks[9].push('G');
    stacks[9].push('Z');

    while (getline(cin, s))
    {
        char *len = strtok(strdup(s.c_str()), " ");
        vector<int> nums;
        int counter = 0;
        while(len != NULL) {
            len = strtok(NULL, " ");
            counter++;
            if (counter == 1 || counter == 3 || counter == 5){
                nums.push_back(stoi(len));
                // cout<< len<< " ";
            }
        }
        // cout<<endl;

// part 1
        // for(int i=0; i<nums[0]; i++)
        // {
        //     stacks[nums[2]].push(stacks[nums[1]].top());
        //     stacks[nums[1]].pop();
        // }

// part 2
        stack<char> temp_stack;

        for(int i=0; i<nums[0]; i++)
        {
            temp_stack.push(stacks[nums[1]].top());
            stacks[nums[1]].pop();
        }
        for(int i=0; i<nums[0]; i++)
        {
            stacks[nums[2]].push(temp_stack.top());
            temp_stack.pop();
        }
    }

    for(int i=1; i<10; i++)
    cout<<stacks[i].top();

    // cout << total_points << endl;
}
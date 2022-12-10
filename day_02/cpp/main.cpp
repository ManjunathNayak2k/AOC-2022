#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int total_points = 0;
    string s;

    map<char, int> opponent;
    opponent['A'] = 1;
    opponent['B'] = 2;
    opponent['C'] = 3;

    map<char, int> player;
    player['X'] = 1;
    player['Y'] = 2;
    player['Z'] = 3;

// part 1
    // while (getline(cin, s))
    // {
    //     char opponent_move = s[0];
    //     char player_move = s[2];
    //     int game_point;

    //     if ((player[player_move] == 1 && opponent[opponent_move] == 3) ||
    //         (player[player_move] == 2 && opponent[opponent_move] == 1) || 
    //         (player[player_move] == 3 && opponent[opponent_move] == 2))
    //     {
    //         game_point = 6;
    //     }
    //     else if ((player[player_move] == 3 && opponent[opponent_move] == 1) ||
    //             (player[player_move] == 1 && opponent[opponent_move] == 2) || 
    //             (player[player_move] == 2 && opponent[opponent_move] == 3))
    //     {
    //         game_point = 0;
    //     }
    //     else
    //     {
    //         game_point = 3;
    //     }

    //     total_points += game_point + player[player_move];
    // }

    // cout << total_points << endl;

// part 2

    while (getline(cin, s))
    {
        char opponent_move = s[0];
        char to_do = s[2];
        int game_point, player_point;

        if (to_do == 'X')
        {
            game_point = 0;
            player_point = opponent[opponent_move] - 1;
            if (player_point == 0)
                player_point = 3;
        }
        else if (to_do == 'Y')
        {
            game_point = 3;
            player_point = opponent[opponent_move];
        }
        else
        {
            game_point = 6;
            player_point = opponent[opponent_move] + 1;
            if (player_point == 4)
                player_point = 1;
        }

        total_points += game_point + player_point;
    }

    cout << total_points << endl;
}
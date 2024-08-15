#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    if (s.length() <= 50 && all_of(s.begin(), s.end(), [](char c){ return isalpha(c);})){
        int P = count(s.begin(), s.end(), 'p') + count(s.begin(), s.end(), 'P');
        int Y = count(s.begin(), s.end(), 'y') + count(s.begin(), s.end(), 'Y');
        if (P != Y){
            answer = false;
        }
    }

    return answer;
}
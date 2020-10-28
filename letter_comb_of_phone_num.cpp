// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// Difficulty - medium
// Problem description can be found on above link.
// Input is provied to function "letterCombinations(string digits)" directly by the 
// leetcode interface.


class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, vector <char>> keymap;
        vector<string> result;
        keymap.insert( {{'2',{'a','b','c'}}, {'3',{'d','e','f'}}, {'4', {'g','h','i'}} , {'5', {'j','k','l'}} , {'6', {'m','n','o'}} , {'7',{'p','q','r','s'}} , {'8', {'t','u','v'}} , {'9', {'w', 'x' ,'y' , 'z'}}} );
        
        unordered_map<char, vector <char>> :: iterator found;
        int length = digits.length();
        for(int i = 0 ; i < length ; ++i)
        {
            if(!result.empty())
            {
                int size = result.size();
                for(int j = 0 ; j < size ; ++j)
                {
                    found = keymap.find(digits[i]);
                    if(found != keymap.end())
                    {
                        int ksize = (found->second).size();
                        string temp (result[0]);
                        result.erase(result.begin());
                        for(int k = 0 ; k < ksize ; ++k)
                        {
                            string put = temp + (found->second)[k];
                            result.push_back(put);
                        }
                    }
                    else
                    {
                        return {};
                    }
                }
            }
            else
            {
                
                found = keymap.find(digits[i]);
                if(found != keymap.end())
                {
                    int ksize = (found->second).size();
                    for(int k = 0 ; k < ksize ; ++k)
                    {
                        string put;
                        put.append(&((found->second)[k]),1);
                        result.push_back(put);
                    }
                }
                else
                    {
                        return {};
                    }
            }
        }
        return result;
    }

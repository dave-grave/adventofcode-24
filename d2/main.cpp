#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
    // read in file
    ifstream fin("input.txt");
    string line;
    int num_safe = 0;

    // parse thru each row of the input file
    while (getline(fin, line))
    {
        istringstream ss(line);
        vector<int> nums;
        for (string num; getline(ss, num, ' ');)
        {
            nums.push_back(stoi(num));
        }

        // create set of differences
        // create sets of allowed differences, then compare
        set<int> diff;
        set<int> inc_diff = {1, 2, 3};
        set<int> dec_diff = {-1, -2, -3};

        // find consecutive differences of each row
        for (int i = 1; i < nums.size(); i++)
        {
            diff.insert(nums[i] - nums[i - 1]);
        }

        // check if diff is a subset of inc_diff or dec_diff
        if (includes(inc_diff.begin(), inc_diff.end(), diff.begin(), diff.end()) || includes(dec_diff.begin(), dec_diff.end(), diff.begin(), diff.end()))
        {
            num_safe++;
        }
        // take an element out of nums and check if nums is safe again
        else
        {
            bool is_safe = false;
            for (int i = 0; i < nums.size(); i++)
            {
                vector<int> nums_copy = nums;
                nums_copy.erase(nums_copy.begin() + i);

                diff.clear();
                for (int i = 1; i < nums_copy.size(); i++)
                {
                    diff.insert(nums_copy[i] - nums_copy[i - 1]);
                }

                if (includes(inc_diff.begin(), inc_diff.end(), diff.begin(), diff.end()) || includes(dec_diff.begin(), dec_diff.end(), diff.begin(), diff.end()))
                {
                    is_safe = true;
                }
            }
            if (is_safe)
            {
                num_safe++;
            }
        }
    }
    cout << "total number of safe rows: " << num_safe << endl;
}
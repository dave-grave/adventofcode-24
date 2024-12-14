#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");

    string line;
    int num_safe = 0;
    while (getline(fin, line))
    {
        istringstream ss(line);
        vector<int> nums;
        for (string num; getline(ss, num, ' ');)
        {
            nums.push_back(stoi(num));
        }

        bool is_increasing = true
                                 ? (3 >= nums[1] - nums[0]) && (nums[1] - nums[0] >= 1)
                                 : false;
        bool is_decreasing = true
                                 ? (-3 <= nums[1] - nums[0]) && (nums[1] - nums[0] <= -1)
                                 : false;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            int difference = nums[i + 1] - nums[i];
            if (!(is_increasing && difference >= 1 && difference <= 3))
            {
                is_increasing = false;
            }
            if (!(is_decreasing && difference <= -1 && difference >= -3))
            {
                is_decreasing = false;
            }
        }

        if (is_increasing || is_decreasing)
        {
            num_safe++;
        }
    }
    cout << "num safe " << num_safe;
}
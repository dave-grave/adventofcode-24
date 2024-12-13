#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
int part_one()
{
   ifstream file("input.txt");
   int first;
   int second;
   vector<int> list_first;
   vector<int> list_second;

   while (file >> first >> second)
   {
      list_first.push_back(first);
      sort(list_first.begin(), list_first.end());

      list_second.push_back(second);
      sort(list_second.begin(), list_second.end());
   }

   int total = 0;
   for (int i = 0; i < list_first.size(); ++i)
   {
      total += abs(list_first[i] - list_second[i]);
   }

   return total;
}

int part_two()
{
   ifstream file("input.txt");
   int first;
   int second;
   set<int> left;
   map<int, int> right;

   while (file >> first >> second)
   {
      left.insert(first);

      if (!right.insert({second, 1}).second)
      {
         right[second]++;
      }
   }

   int similarity = 0;
   for (auto it = left.begin(); it != left.end(); ++it)
   {
      auto it_right = right.find(*it);
      if (it_right != right.end())
      {
         similarity += (*it) * it_right->second;
      }
   }
   // test set and map
   // for (auto it = left.begin(); it != left.end(); ++it)
   // {
   //    cout << *it << endl;
   // }

   // for (auto it = right.begin(); it != right.end(); ++it)
   // {
   //    cout << (*it).first << " " << (*it).second << endl;
   // }

   return similarity;
}

int main()
{
   cout << part_one() << endl;

   cout << part_two() << endl;
}

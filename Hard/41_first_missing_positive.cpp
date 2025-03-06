/*
Because we need to solve the problem in O(1) memory and we need an occurance table, we need to use the original one.
So we need to find a way to mark the indexes in a way that we still keep the orignal value of it.
The best way for this, is to make it negative. Of course at the beginning we need to remove all the negative numbers from the list.
*/ 

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for(int i=0; i < n; i++){
            if( nums[i] <= 0 || nums[i] > n){
                nums[i] = n + 1;
            }
        }

        int ind;
        for(int i = 0; i < n; i++){
            if(abs(nums[i]) <= n) {
                ind = abs(nums[i]) - 1;
                if(nums[ind] > 0){
                    nums[ind] = -nums[ind];
                }
            }
        }

        int i = 0;
        while(i < n && nums[i] < 0){
            i++;
        }
        if( i == n){
            return n+1;
        }
        return i + 1;
    }
};
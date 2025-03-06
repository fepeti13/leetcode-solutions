//math solution O(1) memory

class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        long long sum_act = 0, sum_norm = 0, sum_sq_act = 0, sum_sq_norm = 0;
        int len = grid[0].size();
        long long n = len * len;
        sum_norm = n*(n+1) / 2;
        sum_sq_norm = n*(n+1)*(2*n+1)/6;
        
        for(int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                sum_act += grid[i][j];
                sum_sq_act += grid[i][j] * grid[i][j];
            }
        }

        vector<int> ans;
        int y_min_x = sum_act - sum_norm;
        int y_min_x_sq = sum_sq_act - sum_sq_norm;
        int y_plus_x = y_min_x_sq / y_min_x;
        ans.push_back((y_min_x + y_plus_x) / 2);
        ans.push_back(y_plus_x - ans[0]);
        return ans;
    }
};
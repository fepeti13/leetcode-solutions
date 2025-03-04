class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) { return false;}
        long long y = 0;
        long long x_copy = x;
        while(x > 0){
            y = y * 10 + x % 10;
            x/=10;
        }
        return x_copy==y;
    }
};

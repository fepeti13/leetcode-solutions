/*
Using the same logic when you convert to ternery
*/

class Solution {
public:
    bool checkPowersOfThree(int n) {
        while( n > 1){
            if( n % 3 == 2 ){
                return false;
            }
            n = n / 3;
        }
        return true;
    }
};

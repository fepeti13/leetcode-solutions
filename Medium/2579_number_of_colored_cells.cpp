//both of the formulas are correct

class Solution {
public:
    long long coloredCells(int n) {
        long long m = n;
        //return (2*m-3)*(2*m-2) - 2*(m-2)*(m-1) + 2*m -1;
        return 2*(m-1)*m+1;
    }
};
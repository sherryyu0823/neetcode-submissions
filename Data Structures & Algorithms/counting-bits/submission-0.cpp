class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>ans(n+1, 0);
        int cnt = 0;
        for(int i = 0; i<=n;i++){
            cnt = 0;
            int tmp = i;
            while(tmp){
                if (tmp%2==1) cnt++;
                tmp/=2;
            }
            ans[i] = cnt;
            cnt = 0;
        }
        return ans;
    }
};

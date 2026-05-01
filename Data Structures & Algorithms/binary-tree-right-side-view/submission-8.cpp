/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        dfs(root, ans, 0);
        return ans;
    }
private:
    
    void dfs(TreeNode* node, vector<int>&ans, int dep){
        if (!node) return;
        if (dep == ans.size()){
            ans.push_back(node->val);
        }
        dfs(node->right, ans, dep+1);
        dfs(node->left, ans, dep+1);

    }
};

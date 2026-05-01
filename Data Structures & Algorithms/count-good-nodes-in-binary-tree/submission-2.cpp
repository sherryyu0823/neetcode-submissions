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
#include <algorithm>
class Solution {
public:
    int ans = 0;
    int goodNodes(TreeNode* root) {
        ans = 0;
        dfs(root, -2147483647);
        return ans;
        
    }
    void dfs(TreeNode* node, int last){
        if (node->val>=last) ans++;
        if (node->left == NULL && node->right == NULL ) return;
        last = std::max(last, node->val);
        if (node->left) dfs(node->left, last);
        if (node->right) dfs(node->right, last);
    }
};

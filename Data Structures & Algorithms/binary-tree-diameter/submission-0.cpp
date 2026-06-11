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
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        DFS(root, ans);
        return ans;

    }
private:
    int DFS(TreeNode* node, int &ans){
        if(node == nullptr) return 0;
        int lh = DFS(node->left, ans);
        int rh = DFS(node->right, ans); 

        ans = max(ans, lh+rh);
        return max(lh, rh)+1;
    }
};

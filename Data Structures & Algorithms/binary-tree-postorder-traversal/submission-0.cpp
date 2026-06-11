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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        TreeNode* node = root;
        DFS(root, ans);
        return ans;

    }
private:
    void DFS(TreeNode* node, vector<int> &ans){
        if (node == nullptr) return;
        
        DFS(node->left, ans);
        DFS(node->right, ans);
        ans.push_back(node->val);

    }
};
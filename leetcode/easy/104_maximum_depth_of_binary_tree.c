int maximum(int first, int second) {
    return (first >= second) ? first : second;
}

int maxDepthHelper(struct TreeNode* root, int startingDepth){
    startingDepth++;
    return maximum(
        ((root->left != NULL)  ? maxDepthHelper(root->left, startingDepth) : startingDepth),
        ((root->right != NULL) ? maxDepthHelper(root->right, startingDepth) : startingDepth)
    );
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
    return (root != NULL) ? maxDepthHelper(root, 0) : 0;
}
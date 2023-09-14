/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
  const int LAST_INDEX = numsSize-1;
  int* solutions = (int*)malloc(2 * sizeof(int));
  int c = 0; // current index being summed with each "nums" element
  
  for(int i = 0; c != LAST_INDEX; i = (i+1) % numsSize) {
    if (i <= c) continue; // invalid solutions (summed with current position or a position previously visited)
    else if (target == nums[c]+nums[i])
    {
      // set the solution pair
      solutions[0] = c;
      solutions[1] = i;
      break;
    }

    if (i == LAST_INDEX) c++; // advance current index when "nums" array exhausted
  }

  *returnSize = 2;
  return solutions;
}
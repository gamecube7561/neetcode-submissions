class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if (seen.get(diff) != null) {

                return new int[] {seen.get(diff), i};
            }
            seen.put(nums[i], i);
        }
        return new int[] {};
    }
}

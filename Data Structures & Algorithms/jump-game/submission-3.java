class Solution {
    public boolean canJump(int[] nums) {
        boolean[] canRead = new boolean[nums.length];
        canRead[0] = true;
        
        for(int i = 0; i < nums.length; i++) {
            if (canRead[i]) {
                for (int j = 0; j <= nums[i]; j++) {
                    if (i+j < nums.length) {
                        canRead[i+j] = true;
                    }   
                }
            }
        }

        return canRead[canRead.length-1];
    }
}

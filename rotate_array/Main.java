package rotate_array;

public class Main {
    public static void main(String[] args) {
        
        Solution s = new Solution();
        int[] nums = {1,2,3,4,5,6,7};  
        int k = 3;

        s.rotate(nums, k);
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
        

    
}

}
package longest_substring;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] map = new int[128];
        int start = 0, end = 0, counter = 0, d = 0;
        while (end < s.length()) {
            if (map[s.charAt(end++)]++ > 0) {
                counter++;
            }
            while (counter > 0) {
                if (map[s.charAt(start++)]-- > 1) {
                    counter--;
                }
            }
            d = Math.max(d, end - start);
        }
        return d;
        
    }
}
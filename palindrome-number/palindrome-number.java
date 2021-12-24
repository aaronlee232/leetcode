class Solution {
    public boolean isPalindrome(int x) {
        String num = ""+x;
        StringBuilder reverseSB = new StringBuilder();
        reverseSB.append(num);
        reverseSB.reverse();
        
        if(reverseSB.toString().equals(num)) {
            return true;
        }else {
            return false;
        }
    }
}
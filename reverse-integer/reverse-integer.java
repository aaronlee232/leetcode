class Solution {
    public int reverse(int x) {
        String stringX = ""+x;
        boolean negative = false;
        boolean overflow = false;
        if(stringX.charAt(0)=='-') {
            negative = true;
            stringX = stringX.substring(1,stringX.length());
        }  
        
        String stringXRev = "";
        if(negative) {
            stringXRev += "-";
        }
        for(int i = stringX.length()-1; i >= 0;i--) {
            stringXRev+=stringX.charAt(i);
        }
        System.out.println(stringX);
        System.out.println(stringXRev);
        try {
            return Integer.parseInt(stringXRev);
        } catch (Exception e) {
            return 0;
        }
        
    }
}
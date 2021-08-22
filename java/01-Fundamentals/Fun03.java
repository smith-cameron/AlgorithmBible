public class Fun03 {
    public static void main(String[] args) {
        int[] inputRH = {2,4,3,8,5,7};
        System.out.println(returnHigh(inputRH));

    }
    // 1 & 2 Not able to mix array data types in java
    // 3
    public static int returnHigh(int[] input){
        int max = input[0];
        int min = input[0];
        for(int i = 0; i < input.length; i++){
            if(input[i] > max){
                max = input[i];
            }
            else if(input[i] < min){
                min = input[i];
            }
        }
        System.out.println(min);
        return max;
    }
}

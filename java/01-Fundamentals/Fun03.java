import java.util.ArrayList;
public class Fun03 {
    // 1 & 2 Not able to mix array data types in java
    // 3
    public int returnHigh(int[] input){
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
    // 4
    public ArrayList<Integer> addSeven(int[] input){
        ArrayList<Integer> output = new ArrayList<Integer>();
        for(int i = 1; i < input.length; i++){
            output.add(input[i] + 7);
        }
        return output;
    }
    // 5
    public int printAreturnB(int[] input){
        int firstOdd = 0;
        for(int i = 0; i < input.length; i++){
            if(input[i] % 2 != 0){
                firstOdd = input[i];
                break;
            }
        }
        System.out.println(input[input.length-2]);
        return firstOdd;
    }
    
}

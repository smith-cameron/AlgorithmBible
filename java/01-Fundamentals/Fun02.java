import java.util.ArrayList;
public class Fun02 {
    // 1
    public ArrayList<Integer> countDown(int input){
        ArrayList<Integer> output = new ArrayList<Integer>();
        for (int i = input; i >= 0; i--){
            output.add(i);
        }
        return output;
    }
    // 2
    public int printReturn(int num1, int num2){
        System.out.println(num1);
        return num2;
    }
    // 3
    public int firstPlusInt(int[] input){
        return input[0] + input.length;
    }
    public String firstPlus(String[] input){
        return input[0] + input.length;
    }
    // 
}

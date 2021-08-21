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
    // 4
    public int greaterThan(int[] input){
        int count = 0;
        for(int i = 0; i < input.length; i++){
            if(input[i] > input[1]){
                count += 1;
            }
        }
        return count;
    }
    // 5
    public ArrayList<Integer> greaterThanAgain(int[] input){
        ArrayList<Integer> output = new ArrayList<Integer>();
        int count = 0;
        if( input.length < 2){
            System.out.println("Get a longer array!");
        }
        else{
            for(int i = 0; i < input.length; i++){
                if(input[i] > input[1]){
                    output.add(input[i]);
                    count += 1;
                }
            }
        }
        System.out.println(count);
        return output;
    }
    // 6
    public ArrayList<Integer> jinx(int num1, int num2){
        ArrayList<Integer> output = new ArrayList<Integer>();
        if(num1 == num2){
            System.out.println("Jinx!");
        }
        else{
            for(int i = 0; i < num1; i++){
                output.add(num2);
            }
        }
        return output;
    }
    // 7
    public void goldiLocks(int[] input){
        if(input[0] > input.length){
            System.out.println("Too big!");
        }
        else if(input[0] < input.length){
            System.out.println("Too small!");
        }
        else{
            System.out.println("Just right!");
        }
    }
    // 8
    public int fahrenheitToCelsius(int dFarenheit){
        int dCelsius = (dFarenheit - 32) / (9/5);
        return dCelsius;
    }
    // 9
    public int celsiusToFahrenheit(int dCelsius){
        int dFahrenheit = (9/5 * dCelsius) + 32;
        return dFahrenheit;
    }
}

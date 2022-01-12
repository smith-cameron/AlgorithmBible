import java.util.ArrayList;

public class FunConII_01 {
    public static void main(String[] args) {
        ArrayList<Object> things = new ArrayList<Object>();
        things.add(21);
        things.add("Hello World");
        things.add(new ArrayList<Integer>());
        @SuppressWarnings("unchecked")
        ArrayList<Integer> nestedList = (ArrayList<Integer>) things.get(2);
        nestedList.add(22);
        System.out.println(things);

    }
}

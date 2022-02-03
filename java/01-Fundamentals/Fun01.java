class Fun01{
    // 2
    public void printAndCount(){
        int count = 0;
		for(int i = 512; i <= 4096; i++) {
            if(i % 5 == 0){
                System.out.println(i);
                count ++;
            }
        }
        System.out.println(count);
    }

    // 3
    public void printNums() {
		for(int i = -52; i <= 1066; i++) {
			System.out.println(i);
        }
    }
    // 4
    public void printWhile(){
        int i = 0;
        while (i <= 60000) {
            if (i % 6 == 0) {
                System.out.println(i);
            }
            i ++;
        }
    }
    // 5
    public void beCheerful(int input){
        for(int i = 0; i <= input; i++){
            System.out.println("good morning!");
        }
    }
    // 6
    public void printEitherOr(){
        for(int i = 0; i <= 100 ; i++){
            if(i % 5 == 0 && i % 10 == 0){
                System.out.println("Coding Dojo");
            }
            else if(i % 5 == 0){
                System.out.println("Coding");
            }
            else{
                System.out.println(i);
            }
        }
    }
    // 7
    public void printExcept(){
        for(int i = -300; i <= 0; i+=3){
            if(i == -6 || i == -3){
                continue;
            }
            System.out.println(i);
        }
    }
    // 8
    public void printParam(String input){
        System.out.println(input);
    }
    // 9
    public void printIntegers(){
        int i = 2000;
        while(i <= 5280){
            System.out.println(i);
            i++;
        }
    }
    // 10
    public int addOdds(){
        int sum = 0;
		for(int i = -300000; i <= 300000; i++) {
            if( i % 2 != 0){
                sum += i;
                System.out.println(sum);
            }
		}
		return sum;
    }
    // 11
    public void cakeDay(int num1, int num2){
        if (num1 == 12 || num1 == 21){
            if(num2 == 12 || num2 == 21){
                System.out.println("How did you know!?");
            }
            else {
                System.out.println("Just another day....");
            }
        }
        else {
            System.out.println("Just another day....");
        }
    }
    // 12
    public void printDown(){
        int i = 2016;
        while(i >= 1){
            System.out.println(i);
            i -= 4;
        }
    }
    // 13
    public void leapYear(int input){
        if (input % 4 == 0){
            if (input % 100 == 0){
                if (input % 400 == 0){
                    System.out.println("A Special Kind of Leap Year!");
                }
                else{
                    System.out.println("Not a Leap Year.");
                }
            }
            else{
                System.out.println("Leap Year!");
            }
        }
        else{
            System.out.println("Not a Leap Year.");
        }
    }
    // 14
    public void flexibleCountdown(int min, int max, int mult){
        for(int i = max; i >= min; i -= mult) {
            System.out.println(i);
		}
    }
    // 15
    public void finalCountdown(int mult, int min, int max, int exclude){
        while(min <= max){
            if(min % mult ==0){
                if(min == exclude){
                    min += 1;
                    continue;
                }
                else{
                    System.out.println(min);
                }
            }
            min +=1;
        }
    }
    
    
}
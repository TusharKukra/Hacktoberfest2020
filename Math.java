import java.util.Scanner;
public class Math {
    public static void main(String[] args) {
        int ans,n1,n2;
        Scanner scan1 = new Scanner(System.in);
        System.out.println("Enter two numbers ");
        n1 = scan1.nextInt();
        n2 = scan1.nextInt();
        ans1 = n1 + n2;
        System.out.println("Addition = "+ans1);

        ans2 = n1 - n2;
        System.out.println("Subtraction = "+ans2);

        ans3 = n1 * n2;
        System.out.println("Multiplication = "+ans3);
        
        ans4 = n1/n2;
        System.out.println("Quotient = "+ans4+" & Remainder = "+n1%n2);
        
        scan.close();
    }
}

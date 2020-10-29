import java.util.*;

class ReverseString {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter string to reverse: ");
        reverseString(input.nextLine());
    }
    public static void reverseString(String s) {
        for (int i = s.length() - 1; i >= 0; i--){
            System.out.print(s.charAt(i));
        }
    }
}
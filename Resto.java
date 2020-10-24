import java.util.Scanner; 

public class Resto{
    public static void main(String args[]){
        Scanner ipt = new Scanner(System.in);
        Scanner ipt1 = new Scanner(System.in);

        int shipCost=0;
        
        System.out.println("*************************************************");
        System.out.println("*                   INPUT MENU                  *");
        System.out.println("*************************************************");
        System.out.print("Enter a food name \t: ");
        String foodName = ipt.nextLine();
        System.out.print("Enter the food prize \t: IDR ");
        int foodPrize = ipt1.nextInt();
        System.out.print("Do you want express delivery (0=No, 1=Yes)? ");
        int delivery = ipt1.nextInt();

        if(delivery==1 || delivery==0){
            if(delivery==1){
                if(foodPrize<100000){
                    shipCost=45000;
                }
                else{
                    shipCost=55000;
                }
            }
            else if(delivery==0){
                if(foodPrize<100000){
                    shipCost=20000;
                }
                else{
                    shipCost=30000;
                }
            }
            int priceTotal = foodPrize + shipCost;
        
            System.out.println("*************************************************");
            System.out.println("*                    RECEIPT                    *");
            System.out.println("*************************************************");
            System.out.println("* "+foodName+"\tIDR "+foodPrize+"\t\t\t*");
            System.out.println("* Shipping cost\tIDR "+shipCost+"\t\t\t*");
            System.out.println("* Total\t\tIDR "+priceTotal+"\t\t\t*");
            System.out.println("*************************************************");
        }
        else{
            System.out.println("*************************************************");
            System.out.println("*               Your input invalid              *");
            System.out.println("*************************************************");
        }
    }
}
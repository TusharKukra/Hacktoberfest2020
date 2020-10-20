/* A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number. */

#include<stdio.h>
#include<math.h>
main()
{
 int i,j,num,temp,sum=0;
 printf("Enter number\n");
 scanf("%d",&num);
  while(sum!=1 && sum!=4)
  {
   sum=0;
   while(num>0)
  {
    j=num%10;
    sum+=(j*j);
    num=num/10; 
  }
  num=sum;
  }
  
  if(sum==1)
 printf("Happy Number\n");
 else
 printf("UnHappy Number\n");
}

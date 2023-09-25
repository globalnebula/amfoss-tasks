#include<stdio.h>

int main()
{
    int i,j,n;

    printf("Enter number 'n' : ");
    scanf("%d",&n);

    printf("Prime numbers are :- ");
    for(i=2;i<=n;i++)
    {
        int c=0;
        for(j=1;j<=i;j++)
        {
            if(i%j==0)
            {
                c++;
            }
        }

       if(c==2)
        {
            printf("%d ",i);
        }
    }
}
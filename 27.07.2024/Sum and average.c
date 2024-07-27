#include<stdio.h>
int main()
{
    int sum,j1,j2,j3;
    float ave;
    printf("Enter three integers : ");
    scanf("\n%d%d%d",&j1,&j2,&j3) ;
    sum=j1+j2+j3;
    ave=sum/3.0;
    printf("Sum of %d %d and %d %d:\n",j1,j2,j3,sum);
    printf("Average of %d,%d and %d:%f\n",j1,j2,j3,ave);
    return 0;
}

 #include<stdio.h>
    int gcd(int a,int j)
    {
        if(j==0)
            return a;
        return gcd(j,a%j);
    }
    int main(){
        int a,j;
        printf("Enter two integers: ");
        scanf("%d %d",&a,&j);
        printf("GCD: %d\n",gcd(a, j));
    }
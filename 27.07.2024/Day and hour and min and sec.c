#include<stdio.h>
void main()
{
    int days7,hours7,min7,sec7,total7,dd,hh,mm;
    scanf("%d", &days7);
    if(1<=days7&&days7<=25)
    {
        dd=days7*24*3600;
    } 
    scanf("%d", &hours7);
    if(1<=hours7&&hours7<=60)
    {
        hh=hours7*3600;
    }
    scanf("%d",&min7);
    if(1<=min7&&min7<=60)
    { 
        mm=min7*60;
    }
    scanf("%d", &sec7); 
    total7=dd+hh+mm+sec7;
    printf("%d seconds\n", total7);
}

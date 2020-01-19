#includ
{
    int i,j,k,l=1,N,d,r,count=0;
    scanf("%d",&N);
    for(i=1;i<=N;i++)
    {
        k=1;
        d=i%2;
        r=l+i-1;
        for(j=0;j<i;j++)
        {

 if(d==0)
            {
                printf("%d",r);
                r--;
                if(k<i)
                {
                    printf("*");
                    k=k+1;
                }
                l++;
                continue;
            }
            printf("%d",l);
            l++;
            if(k<i)
            {
                printf("*");
                k=k+1;
            }
        }
        printf("\n");
    }
    return 0;
}

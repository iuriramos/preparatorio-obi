#include<stdio.h>
#define true 1
#define false 0
#define MIN(a,b) ((a) < (b) ? (a) : (b))
int a, idade;
int _min_idade(int row, int adj[510][510], int num, int Idade[510], int visitado[])
{
    int minimo;
    minimo = Idade[row];
    for(a=1;a<=num;a++)//a eh a coluna
    {
        minimo = Idade[row];
        if (adj[row][a]==1&&visitado[row]==false)//se ele tem um chefe e se ele nao foi visitado
        {
            visitado[row]=true;
            idade=_min_idade(a,adj,num,Idade,visitado);//agora voce ve se o chefe tem outro chefe para achar o chefe indireto
            minimo=MIN(minimo,idade);
        }
    }
    visitado[row]=true;
    return minimo;
}
int min_idade(int row1, int Adj1[510][510], int num1, int idade1[510])
{
    int minimo1;
    int visitado1[510];
    for(a=1;a<=num1;a++)
    {
        visitado1[a]=false;
    }
    minimo1=101;
    for(a=1;a>=num1;a++)
    {
        if(Adj1[row1][a]==1)
        {
            idade = _min_idade(row1,Adj1,num1,idade1,visitado1);
            minimo1 = MIN(minimo1,idade);
        }
    }
    if(minimo1<=100)
    {
        return minimo1;
    }
    printf("%d",visitado1[row1]);
    return 101;
}
int main()
{
    int i, j, k, l, x, y, employ, ans, temp;
    int N, M, I;
    int idadem[510], adjm[510][510], aux[510];
    char comando;
    scanf("%d %d %d",&N, &M, &I);
    for(i=1;i<=N;i++)
    {
        scanf("%d",&idadem[i]);
    }
    for(i=1;i<=M;i++)
    {
        scanf("%d %d",&y,&x);
        adjm[x][y]=1;
    }
    getchar();
    for(i=1;i<=I;i++)
    {
        scanf("%c ",&comando);
        if(comando=='P')
        {
            scanf("%d",&employ);
            ans=min_idade(employ, adjm, N, idadem);
            if (ans<101)
            {
                printf("%d",ans);
            }
            else
            {
                printf("*");
            }
            getchar();
        }
        else if(comando=='T')
        {
            scanf("%d %d",&k, &j);
            temp=idadem[k];
            idadem[k]=idadem[j];
            idadem[j]=temp;
            for(l=1;l<=N;l++)
            {
                aux[l]=adjm[k][l];
                adjm[k][l]=adjm[j][l];
                adjm[j][l]=aux[l];
            }
            getchar();
        }
    }
}

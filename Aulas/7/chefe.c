#include<stdio.h>
#define true 1
#define false 0
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int _min_idade(int row, int adj[510][510], int N, int idades[510], int visitado[510])
{
    // printf("start -- min idade (%d)\n", row);
    visitado[row]=true; // visita nó assim que entra na função
    int minimo = idades[row];
    for(int col=1; col<=N; col++)//a eh a coluna
    {
        if (adj[row][col]==1 && visitado[col]==false)//se ele tem um chefe e se ele nao foi visitado
        {
            // não eh mais necessario, agora nó é marcado assim que chega na função
            // visitado[col]=true;
            int idade=_min_idade(col,adj,N,idades,visitado);//agora voce ve se o chefe tem outro chefe para achar o chefe indireto
            minimo=MIN(minimo,idade);
        }
    }
    // printf("end -- min idade (%d): %d\n", row, minimo);
    return minimo;
}
void print_adj(int adj[510][510], int N) {
    printf("[\n");
    for (int i = 1; i <= N; i++) {
        printf("[ ");
        for (int j = 1; j <= N; j++) {
            printf("%d, ", adj[i][j]);
        }
        printf("]\n");
    }
    printf("]\n");
}
int min_idade(int row, int adj[510][510], int N, int idades[510])
{
    int minimo = 101;
    int visitado[510];
    for(int a=1;a<=N;a++)
    {
        visitado[a]=false;
    }
    for(int col=1;col<=N;col++)
    {
        if(adj[row][col]==1 && visitado[col]==false)
        {
            int idade = _min_idade(col, adj, N, idades, visitado);
            minimo = MIN(minimo, idade);
        }
    }
    if(minimo <= 100)
    {
        return minimo;
    }
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
    // print_adj(adjm, N);
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
            // temp=idadem[k];
            // idadem[k]=idadem[j];
            // idadem[j]=temp;
            for(l=1;l<=N;l++)
            {
                aux[l]=adjm[k][l];
                adjm[k][l]=adjm[j][l];
                adjm[j][l]=aux[l];
            }
            // colunas também, vértices devem atualizar os locais para onde apontam
            for(l=1;l<=N;l++)
            {
                aux[l]=adjm[l][k];
                adjm[l][k]=adjm[l][j];
                adjm[l][j]=aux[l];
            }
            getchar();
            // print_adj(adjm, N);
        }
    }
}

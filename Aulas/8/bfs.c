#include<stdio.h>
#define N 4
int i, j, k, l, m, a, node, count;
int matriz[4][4] = {{0,1,1,0},{0,0,0,1},{0,1,0,0},{0,0,0,0}};
void bfs(int start, int end) // mudei assinatura (CAMINHO)// sem o end--> return parent(array de pais)
{
    int parent[N], curr[N], next[N], path[N];
    for(a=0;a<N;a++)
    {
        parent[a]=-1;
        curr[a]=0;
        next[a]=0;
    }
    i=0;
    parent[start] = start;// convenciona que se ele nao tem pai, ele igual a ele
    curr[i]=start; //i eh o ponteiro para curr
    i=1;
    while (i>0)
    {
        j=0;
        for (k=0;k<i;i++)// 0, 1, 2, ..., i-1   elementos do current processar
        {
            node = curr[k]; //incialmente: start
            for(l=0;l<N;l++)
            {
                if (matriz[node][l]==1)//[0,1,1,0]
                {
                    if(parent[l]==-1)//se for -1, nao foi descoberto
                    {
                        parent[l]=node;
                        next[j]=l;
                        j+=1;
                    }
                }
            }
        }
        for(a=0;a<N;a++)
        {
            curr[a] = next[a];
        }
        i=j;//se j =0 ou seja nao achei mais nenhum nao visitado sai do LOOP
    }
    node = end;
    m=0;
    while (node != parent[node]){// assumindo que o grafo eh conexo e nao tem disconexao
        path[m++]= node;//indo de baixo pra cima pegando os pais e descobrindo o camiho entre o start e o end
        node= parent[node];
    }//ainda precisa reverter
    path[m]=start;
    for(a=m;a>=0;a--)
    {
        printf("%d, ",path[a]);// do final pro inicio (caminho reverso)
    }
}
int main()
{
    bfs(0,3);
}
//Next eh o tamanho da linha
// percorrer os vizinhos
//node eh onde ue to
//linha eh da matriz
// percorrendo linha pra ver se tem caminho entre node e l, se existe --> pai de l eh no

#include<stdio.h>
#define true 1
#define false 0
#define N 3
#define MAX 1000
typedef int bool;
int a, m, node, next;
int matriz[3][3]={{0,1,4},{0,0,2},{0,0,0}};
void dijkstra(int start, int end)
{
    int parent[N], distance[N], path[N], min_dist; // distance = distancia entre start e todos outros
    bool intree[N];
    for(a=0;a<N;a++)
    {
        intree[a]=false;
        parent[a]=-1;
        distance[a]=MAX;
    }
    node = start;
    distance[start]= 0;
    intree[start] = true;
    while(node != -1)// -1 eh o valor de parada
    {
        for(a=0;a<N;a++)
        {
            if (matriz[node][a]>0)
            {
                if((distance[node]+matriz[node][a]) < distance[a])
                {
                    distance[a]=distance[node]+matriz[node][a];
                    parent[a]=node;
                }
            }
        }
        //pegar o proximo node
        node = -1;
        min_dist = MAX;
        for(a=0;a<N;a++)
        {
            if(distance[a]<min_dist && intree[a]==false)
            {
                min_dist=distance[a];//descobrir o proximo no com a menor distancia
                node=a;
            }
        }
        if(node!=-1)
        {
            intree[node]=true;
        }
    }
    node=end;
    m=0;
    while (node != -1){// assumindo que o grafo eh conexo e nao tem disconexao
        path[m++]= node;//indo de baixo pra cima pegando os pais e descobrindo o camiho entre o start e o end
        node= parent[node];
    }//ainda precisa reverter
    for(a=m-1;a>=0;a--)
    {
        printf("%d, ",path[a]);// do final pro inicio (caminho reverso)
    }
    printf("%d",distance[end]);
}
int main()
{
    dijkstra(0,2);
}

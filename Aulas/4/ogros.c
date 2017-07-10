#include<stdio.h>
int S, E, val, mid;
int pontuacao(int A[10010], int T,  int target){
    S = 0;
    E = T - 1;
    while(S<E)
    {
        mid = (S+E+1)/2;
        val= A[mid];
        if (val == target){
            return mid;
        }
        else if (val>target){
            E=mid-1;
        }
        else{
            S=mid;
        }
    }
    if(S==E){
        return S;
    }
    return -1;
}
int main()
{
    int N, M, x, i;
    int faixa[10010], ponto[10010];
    scanf("%d %d", &N, &M);
    faixa[0]=0;
    for (i=1;i<N;i++){
        scanf("%d", &faixa[i]);
    }
    for (i=0;i<N;i++){
        scanf("%d",&ponto[i]);
    }
    for(i=0;i<M;i++){
        scanf("%d",&x);
        printf("%d ",ponto[pontuacao(faixa, N, x)]);
    }
}

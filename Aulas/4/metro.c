#include<stdio.h>
int S, E, val, mid, i;
int maximo(int a[10010], int b, int ideal, int target) // funcao que procura o maior valor possivel para o tamanho do pao
{
    S=1;
    E=ideal;
    while(S<E)
    {
        val=0;
        mid = (S+E+1)/2;
        for(i=0;i<b;i++){
            val+=a[i]/mid;
        }
        if(val>=target){ //se a divisao dos paes pelo tamanho mid for maior ou igual que o numero de paes necessarios, mudar o start para mid
            S=mid;
        }
        else if(val<target){ //se a divisao dos paes pelo tamanho mid for menor que o numero de paes necessarios, mudar o end para mid - 1
            E=mid - 1;
        }
    }
    if(S==E) return S;
    return -1;
}
int main()
{
    int N, K, num;
    int tamanho[10010];
    scanf("%d %d",&N, &K);
    for(i=0;i<K;i++){
        scanf("%d",&tamanho[i]);
        num += tamanho[i];
    }
    num = num/N;//num eh o valor ideal para o tamanho do pao
    printf("%d", maximo(tamanho,K,num,N));
}

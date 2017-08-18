#include<stdio.h>
//cruzamento entre duas linhas
//comparar os numeros pra ver quantos na frente sao maiores por que se for menor ele nao cruza pois a reta passa por baixo olhar para <----
//toda vez que tiver troca --->contador
int soma, soma1, mid, i, j, k;
int merge(int numeros[60010], int extra[60010], int start, int mid, int end)
{
    i = start;
    j = mid;
    k = start;
    soma1 = 0;
    while (i<mid && j<end){
        if (numeros[i]<=numeros[j]){
            extra[k]=numeros[i];
            i++;
        }
        else{
            extra[k]=numeros[j];
            j++;
            soma1 += (mid - i);
        }
        k++;
    }
    while(i<mid){
        extra[k]=numeros[i];
        i++;
        k++;
    }
    while(j<end){
        extra[k]=numeros[j];
        j++;
        k++;
    }
    for(k=start;k<=end;k++){
        numeros[k]=extra[k];
    }
    return soma1;
}
int mergesort(int numeros[60010], int extra[60010], int start, int end)
{
    if(end-start<2) return 0;
    soma = 0;
    mid = (start + end + 1)/2;
    soma += mergesort(numeros, extra, start, mid);
    soma += mergesort(numeros, extra, mid, end);
    soma += merge(numeros, extra, start, mid, end);
    return soma;
}
int main()
{
    int N, lista[60010], plus[60010];
    scanf("%d",&N);
    for(i=0;i<N;i++){
        scanf("%d",&lista[i]);
    }
    printf("%d", mergesort(lista, plus, 0, N-1));
}

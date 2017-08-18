#include<stdio.h>
//cruzamento entre duas linhas
//comparar os numeros pra ver quantos na frente sao maiores por que se for menor ele nao cruza pois a reta passa por baixo olhar para <----
//toda vez que tiver troca --->contador

int merge(int numeros[60010], int extra[60010], int start, int mid, int end)
{
    int i = start;
    int j = mid;
    int k = start;
    int soma1 = 0;
    // trabalhando com intervalos fechados
    // i vai de start até mid - 1 => [start, mid -1] ou [start, mid)
    // j vai de mid até end => [mid, end]
    // equivalente a:
    // while (i <= mid - 1 && j <= end) {
    while (i<mid && j<=end){ 
        if (numeros[i]<=numeros[j]){
            extra[k]=numeros[i];
            i++;
        }
        else{
            extra[k]=numeros[j];
            j++;
            // nesta linha que a contagem de cruzamentos é feita
            // mid - i => representa o que falta da primeira metade [start, mid -1] ser processada
            // numeros[j] é menor do que todos os números entre [i, mid -1]
            // # [i, mid -1] = (mid - 1) -i + 1 = mid - i
            soma1 += (mid - i); 
            
        }
        k++;
    }
    printf("%d ", soma1);
    while(i<mid){
        extra[k]=numeros[i];
        i++;
        k++;
    }
    while(j<=end){ // intervalo fechado...
        extra[k]=numeros[j];
        j++;
        k++;
    }
    for(k=start;k<=end;k++){ // aqui você utilizou corretamento o intervalo [start, end]
        numeros[k]=extra[k];
    }
    return soma1;
}
int mergesort(int numeros[60010], int extra[60010], int start, int end)
{
    // end - start + 1 => quantidade de elementos em [start, end] (intervalo fechado).
    // se a quantidade de elementos é menor que 2, numeros jah está ordenado
    if(end-start + 1 < 2) return 0; 
    int soma = 0;
    int mid = (start + end + 1)/2;
    soma += mergesort(numeros, extra, start, mid - 1); // trabalhando com o intervalo fechado [start, mid - 1]
    printf("soma = %d\n", soma);
    soma += mergesort(numeros, extra, mid, end); // intervalo fechado [mid, end]
    printf("soma = %d\n", soma);
    soma += merge(numeros, extra, start, mid, end);
    printf("soma = %d\n", soma);
    return soma;
}
int main()
{
    int N, lista[60010], plus[60010];
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        scanf("%d",&lista[i]);
    }
    // para simplificar a chamada você pode trabalhar com o intervalo fechado [0, N - 1]
    // mas no meu código me lembro que trabalhei com o intervalo aberto [0, N)
    // no meu código trabalhei com intervalo aberto ao final então a chamda seria
    // mergesort(lista, plus, 0, N - 1)
    // no seu código vou seguir a vamos trabalhar com o intervalo fechado [0, N - 1]
    // então a chamada continua a mesma mergesort(lista, plus, 0, N - 1)
    printf("%d", mergesort(lista, plus, 0, N-1));
    // uma observação em python:
    // range(start, end) => start, start + 1, ...., end -2, end -1. 
    // ou seja, range(start, end) => [start, end)
    // por isso eh mais fácil de se trabalhar com intervalos abertos ao final
    // acho que dessa forma vai ficar mais fácil para você entender o código em py tambem
}

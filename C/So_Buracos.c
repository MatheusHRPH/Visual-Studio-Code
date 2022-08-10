#include <stdio.h>
#include<stdlib.h>
#include <math.h>
#include <time.h>
#include <conio.h>
#define N 1000

void main(){
int vetor[N];
int i, estaburaco = 0;
float buraco = 0, vivo = 0;
srand(time(0));

for(i=0; i < N; i++) {
    vetor[i] = rand() % 2;
    printf("%d\n", vetor[i]);
}
for(i=0; i<N; i++) {
    if(vetor[i] == 0 && estaburaco == 0){
        buraco++;
        estaburaco = 1;

    }
    if(vetor[i] == 1){
        estaburaco = 0;
        vivo++;
    }
}
printf("\n%.0f Programas e %.0f Buracos\n", vivo, buraco );
printf("Porcentagem de buracos = %.2f\n", (buraco/vivo)*100 );

}

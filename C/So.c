#include <stdio.h>

int main() {
double ouro;
float num[50];
num[0] = 1.0;
num[1] = 1.0;
int i, x = 2, iteracoes = 100;
for(i = 0; i != iteracoes; i++){
    num[x] = num[x-1] + num[x-2];
    ouro = num[i+1]/num[i];
    printf("%.f/ %.f =  %.20Lf\n", num[i+1], num[i], ouro);
    x++;

    };  
}
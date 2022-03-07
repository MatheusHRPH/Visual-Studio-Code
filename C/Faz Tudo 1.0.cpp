#include <stdlib.h>
#include <stdio.h>
#include <math.h>

//FAZ TUDO AAAAAA222


int max( int num1, int num2){
	int resultado, divisor, maior, contagem;
	resultado=0;
	divisor=1;
	contagem=0;
	if (num1 >= num2){
	 maior=num1;
}
	 else (num1 < num2);{
	 	maior=num2;
	 }
	 while(contagem <= maior){
		if(num1%divisor==0 && num2%divisor==0 && divisor>resultado){
	     resultado = divisor;
		 divisor = divisor+1;
		 contagem= contagem +1;
		}
	else{
		  resultado=resultado;
		 divisor= divisor+1;
		 contagem= contagem +1;
	}
}
return resultado;
}

int primo ( int N) {
	int  resultado;
	resultado=0;
	if(N == 2 || N == 3 || N == 5 || N == 7 ) resultado =1;
	 else
	 	if (N==9) resultado=0;
	 else{
	 	if(N % 2  == 0) resultado=0;
		 else{
		 	if(N%3 ==0) resultado=0;
		 	 else{
		 	 	if(N%5==0) resultado=0;
		 	 	 else{
		 	 	 	if(N%7==0) resultado=0;
		 	 	 	 else{
		 	 	 	 	if(N%9==0) resultado=0;
		 	 	 	 	 else{
		 	 	 	 	 	resultado=1; 
		 	 	 	 	 	
							 }
						}
				   }
			  }
		}
}

return resultado;
}
int main () {
	int escolha, valor, c100=0, c50=0, c10=0, c5=0, c1=0, pares=0, impares=0, n, divisao, v1=0;
	int num1, num2, num, s, m;
	char gravida[40];
	float peso, altura, imc, mediageral=0, mediapar=0, S1=0, S2=0, k=0, v2;
	printf("Bem Vindo ao Faz Tudo 1.0 \n\n\n");
	printf("Feito por Matheus Hoffmann \n\n\n");
	printf("O que deseja realizar: \n\n\n");
	printf("Digite [1] para Indice de massa corporal \n\n");
	printf("Digite [2] para Divisao de cedulas \n\n");
	printf("Digite [3] para Media geral e media de pares\n\n");
	printf("Digite [4] para Calculador de Serie Harmonica [1/1 + 1/2 + 1/3 ... 1/n] \n\n");
	printf("Digite [5] para Maximo divisor comum \n\n");
	printf("Digite [6] para Verificar se e primo \n\n");
	printf("Digite [7] para Calculador de Meses de Gravidez \n\n");
	scanf("%d", &escolha);
	system("cls");
	if(escolha!=1 && escolha!=2 && escolha!=3 && escolha!=4 && escolha!=5 && escolha!=6 && escolha!=7)
	printf("Desculpe, Escolha Invalida, Programa Encerrado \n\n\n");
    else{
    	if(escolha==1){
    	printf("Calculador de Indice de massa Corporal ATIVADO \n\n\n");	
		printf("Informe o peso \n");
    	scanf("%f", &peso);
    	printf("Informe a altura \n");
    	scanf("%f", &altura);
    	imc=peso/pow(altura,2);
        printf("Indice de Massa Corporal:%.1f \n\n" ,peso/pow(altura,2));	
        if(imc<20.0) printf("  Abaixo do Peso \n\n\n");
        if(imc>20&&imc<=25) printf(" Peso Normal \n\n\n");	
        if(imc>25&&imc<=30) printf("  Sobre Peso \n\n\n");
        if(imc>30&&imc<=40) printf("  Obeso \n\n\n");	
        if(imc>40) printf(" Obeso Morbido \n\n\n");	
	}
	else 
	    if(escolha==2){
	    printf("Divisor de Cedulas ATIVADO \n\n\n");
	    printf("Digite o valor: \n\n");
	    scanf("%d", &valor);
	    while (valor > 0){
		 if(valor >= 100){
		 	valor = valor - 100;
		 	c100++;
		            } else
		        if ( valor >= 50){
		    	valor = valor - 50;
		    	c50++;
		    	      } else
		    	          if ( valor >= 10){
		    	          valor = valor - 10;
		    	          c10++;
		                         } else 
		                                 if ( valor >= 5){
		    	                         valor = valor - 5;
		    	                         c5++;
		                                              } else {
			
		      
		    	                                                valor = valor - 1;
		    	                                                c1++;
		                                                             }
		    
	  	                                                                       }
		
        printf ("Cedulas de 100: %d \n\n ", c100);
        printf ("Cedulas de 50: %d \n\n ", c50);
        printf ("Cedulas de 10: %d \n\n ", c10);
        printf ("Cedulas de 5: %d \n\n", c5);
        printf ("Cedulas de 1: %d \n\n ", c1); 
	    }
	else
	    if(escolha==3){
	    printf("Calculador de media geral e media de pares ATIVADO \n\n\n");
	    printf("Digite um numero [0 para encerrar]: \n");
	scanf("%d", &n);
	if(n>0){
	
	
	while (n>0){
		        mediageral=mediageral+n;
		         if(n%2==0){
				    pares=pares+1;
				    mediapar=mediapar+n;
			}
				   else impares=impares+1;
				   printf("Digite outro numero [0 para encerrar]: \n");
				   scanf("%d", &n);
			}
			if(pares<1)mediapar=0;
			else{
				mediapar=mediapar/pares;
			}
			divisao=pares+impares;
		    mediageral=mediageral/divisao;
		    printf("Foram digitados %d numeros pares \n", pares);
			printf("Foram digitados %d numeros impares \n", impares);
			printf("A media dos pares foi: %.3f \n", mediapar);
		    printf("A media geral foi : %.3f \n", mediageral);
		    
		}
		else printf("Programa encerrado \n");
	    }
	    else
	        if(escolha==4){
	        	printf("Calculador de Serie Harmonica [1/1 + 1/2 + 1/3 ... 1/n] ATIVADO \n\n\n");
	        	printf("Digite um numero inteiro e positivo: \n");
            scanf("%f", &v2);
            while (v1<v2) {
	 
            k = k+1;
            S1 = 1/k;
            S2 = S2 + S1;
            v1 = v1+1;
            } 
            printf(" O resultado da soma foi: %f \n\n\n", S2);
	        }
	    else
	        if(escolha==5){
	        printf("Calculador de Maximo Divisor Comum ATIVADO \n\n\n");
	        printf("Digite o primeiro numero: \n\n");
	        scanf("%d", &num1);
	        printf("Digite o segundo numero: \n\n");
	        scanf("%d", &num2);
	        printf(" Maximo divisor comum : %d \n\n", max(num1,num2));
	        }
	    else
		    if(escolha==6){
		    printf("Verificador de Numero primo ATIVADO \n\n\n");
		    printf("Digite um numero: \n");
	        scanf("%d", &num);
	        printf("O resultado foi : %d\n", primo(num));
	        printf("1 = Primo (Divide apenas por 1 e por ele mesmo[%d] )\n", num);
	        printf("0 = Nao Primo  \n");
			}
			if(escolha==7){
	        printf("Calculador de Meses de Gravidez ATIVADO \n\n\n");
	        printf("Quem esta gravida: \n\n");
            scanf("%s", gravida);
  
   
            printf("Quantas semanas: \n\n");
            scanf("%d", &s);
   
            if(s<=4)m=1;
                else
                    if(4<s&&s<=9) m=2;
                        else 
                            if(10<=s&&s<=13) m=3;
                            else
                                if(14<=s&&s<=18) m=4;
                                    else
                                        if(19<=s&&s<=22) m=5;
                                            else
                                                if(23<=s&&s<=27) m=6;
                                                    else
                                                        if(28<=s&&s<=31) m=7;
                                                            else
                                                                if(32<=s&&s<=36) m=8;
                                                                    else
                                                                        if(37<=s&&s<=42) m=9;
   printf("%s esta no %d  mes da gravidez \n\n", gravida, m);
							
			}  
	
}
	system("pause");
	
	return 0;
	
	
}

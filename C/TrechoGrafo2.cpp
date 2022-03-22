#include <iostream>

using namespace std;

const int TAM=10;

struct no {
    int destino;
    struct no *prox;
};

int vertice[TAM];
struct no *arestas[TAM];

int n_vertices=0;

void inicia_grafo() {
    int i; 

    for (i=0; i<TAM; i++)
        arestas[i]=NULL;
}

void insere(int valor){
	if(n_vertices < TAM){
		for(int i=0; i<n_vertices; i++) {
			if(vertice[i]==valor){
				cout << "Valor Repetido" << endl;
			}
		}
		vertice[n_vertices]=valor;
		n_vertices++;
	}else cout << "vetor cheio" << endl;
}

void insere_arestas(int orig, int dest) {
    int i=0;
    int j=1; 
    struct no *atual,*novo,*anterior;

    while (i<n_vertices && vertice[i]!=orig)
        i++;
    if (i==n_vertices) {
        cout << "Nao existe vertice de origem" << endl;
        return;
    }
    while (j<n_vertices && vertice[j]!=dest)
        j++;
    if (j==n_vertices) {
        cout << "Nao existe vertice de dest" << endl;
        return;
    }
    
    atual = arestas[i];
    while(atual != NULL) {
    	if(atual -> destino == dest){
    		cout << "Aresta Repetida" << endl;
    		return; 
		}
		anterior = atual;
		atual = atual->prox;
	}
	novo = new (struct no); 
	novo->destino = dest;
	novo->prox = NULL;
	if(arestas[i] == NULL) 
		arestas[i] = novo;
	else anterior->prox = novo; 
}

void remove_arestas(int orig, int dest) {
    int i=0;
    int j=0;
    struct no *atual,*novo,*anterior;

    while (i < n_vertices && vertice[i] != orig)
        i++;
    if (i==n_vertices) {
        cout << "Nao existe vertice de origem" << endl;
        return;
    }
    while (j<n_vertices && vertice[j] != dest)
        j++;
    if (j == n_vertices) {
        cout << "Nao existe vertice de dest" << endl;
        return;
    }
    
    atual = arestas[i];
    while(atual != NULL){
    	if(atual->destino == dest) {
    		if(atual == arestas[i]) 
    			arestas[i] = arestas[i]->prox;
			else anterior->prox = atual->prox;
			delete(atual);
			return;
		}
		anterior = atual;
		atual = atual->prox;
	}
	
}

void haaresta(int origem, int dest) {
	struct no *atual,*novo,*anterior;
	while(atual != NULL){
    	if(atual->destino == dest){
    		cout << "A aresta existe" << endl;
    		return;
		}
	}
	cout << "Nao encontrado" << endl;
} 


void imprime_grafo() {

    struct no *atual;

    for (int i=0; i<n_vertices; i++) {
        cout << vertice[i] << " -> " ;
        for (atual=arestas[i]; atual!=NULL; atual=atual->prox)
            cout << "<" << vertice[i] << "," << atual->destino << "> ";
        cout << endl;
    }
}

int main() {

    insere(10);
    insere(20);
    insere(30);
    insere(40);
    insere(50);
    insere_arestas(10,40);
    insere_arestas(20,30);
    insere_arestas(20,50);
    insere_arestas(30,40);
    insere_arestas(50,40);
    insere_arestas(60,10);
    insere_arestas(10,60);
    imprime_grafo();

    haaresta(10,40);
    haaresta(40,10);
    haaresta(60,40);
    haaresta(40,60);

    remove_arestas(40,10);
    remove_arestas(20,30);
    remove_arestas(20,50);
    remove_arestas(60,10);
    remove_arestas(10,60);

    imprime_grafo();

}


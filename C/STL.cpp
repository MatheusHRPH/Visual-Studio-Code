#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main () {

    stack <int> pilha;
    queue <int> fila;
    vector <int> lista;
    vector <int> :: iterator it;
    set <int> arvore;
    set <int> :: iterator its;


    pilha.push(10);
    pilha.push(11);
    pilha.push(12);
    cout << "Topo da pilha: " << pilha.top() << endl;

    fila.push(20);
    fila.push(21);
    fila.push(22);
    cout << "Frente da fila: " << fila.front() << endl;

    pilha.pop();
    fila.pop();
    
    cout << "Tamano da pilha: " << pilha.size() << endl;
    cout << "Tamano da fila: " << fila.size() << endl;

    lista.push_back(31);
    lista.push_back(32);
    lista.push_back(30);


    for(it = lista.begin(); it != lista.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
    for(int i = 0; i < lista.size(); i++) {
        cout << lista[i] << " "; 
    }
    cout << endl;
    sort(lista.begin(), lista.end());

    for(it = lista.begin(); it != lista.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
    for(int i = 0; i < lista.size(); i++) {
        cout << lista[i] << " "; 
    }
    cout << endl;

    arvore.insert(41);
    arvore.insert(42);
    arvore.insert(43);
    for(its = arvore.begin(); its != arvore.end(); its++) {
        cout << *its << " ";
    }
    

}
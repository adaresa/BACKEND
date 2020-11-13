#include <stdio.h>

int numInput(char[]);
void fillArray(int size, double[size][size]);
void newArray(int size, double[size][size], double[size][size]);
void printArray(int size, double[size][size]);

int main() {
   // SAA RUUTMAATRIKS A RIDADE JA VEERGUDE ARV
   int n = numInput("Sisesta ruutmaatriks A ridade ja veergude arv(1-10): ");
   // TÄIDA RUUTMAATRIKS A REAALARVUDEGA
   double A[n][n];
   fillArray(n, A);
   // MOODUSTATAKSE MASSIIV B JAGADES MASSIIVI A ELEMENTE SAMA REA DIAGONAALELEMENDIGA
   double B[n][n];
   newArray(n, A, B);
   // VÄLJASTA EKRAANILE MASSIIV B
   printArray(n, B);
   return 0;
}

int numInput(char text[]){
    int num;
    do{ 
        printf("%s", text);
        scanf("%d", &num);
    }while(num < 1 || num > 10);
    printf("\n");
    return num;
}

void fillArray(int size, double arr[size][size]){
    int i, j;
    for(i = 0; i < size; i++){
        for(j = 0; j < size; j++){
            printf("Insert A[%d][%d]: ", i, j);
            scanf("%lf", &arr[i][j]);
        }
    }
    printf("\n");
}

void newArray(int size, double arrA[size][size], double arrB[size][size]){
    int i, j;
    for(i = 0; i < size; i++){
        for(j = 0; j < size; j++){
            arrB[i][j] = (arrA[i][j] / arrA[i][i]);
        }
    }
}

void printArray(int size, double arr[size][size]){
    int i, j;
    for(i = 0; i < size; i++){
        for(j = 0; j < size; j++){
            printf("%.2lf  ", arr[i][j]);
        }
        printf("\n");
    }
}
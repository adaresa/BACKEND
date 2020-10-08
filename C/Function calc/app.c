#include<stdio.h>
#include<math.h>

int main(){
   double A, H, YM, Y[15], X[15];
   printf("Algfunktsioon on: y = (sqrt(x) * sin(1/x)) / (x + exp(x))\n");
   printf("Sisesta algv22rtus A\n");
   scanf("%lf", &A);
   while (A == 0)
   {
      printf("Algv22rtus ei tohi olla 0\nSisesta algv22rtus A\n");
      scanf("%lf", &A);
   }
   printf("Sisesta samm H\n");
   scanf("%lf", &H);
   while (H <= 0)
   {
      printf("Samm peab olema nullist suurem\nSisesta samm H\n");
      scanf("%lf", &H);
   }
   printf("Sisesta alampiir YM\n");
   scanf("%lf", &YM);

   int n, i;
   double tmp;
   X[0]=A;

   for(i=0;i<15;i++){
      if(X[i] < 0){
         tmp = -sqrt(-X[i]);
      }
      else{
         tmp = sqrt(X[i]);
      }
      Y[i] = (tmp * sin(1.0/X[i])) / (X[i]+exp(X[i]));
      if(Y[i] < YM){
         i--;
         break;
      }
      X[i+1] = X[i] + H;
   }
   n = i;
   printf("\nX      | Y\n");
   for(i=0;i<n;i++){
      if(X[i] == 0.0){
         printf("%.3lf  | puudub\n", X[i]);
      }
      else if(X[i] < 0){
         printf("%.3lf | %.3lf+i\n", X[i], Y[i]);
      }
      else{
         printf("%.3lf  | %.3lf\n", X[i], Y[i]);
      }
   }
   if(i < 14){
      printf("X(%.3lf)-i Y(%.3lf) v22rtus on madalam kui alampiir YM = %.3lf\n", X[i], Y[i], YM);
   }
   return 0;
}

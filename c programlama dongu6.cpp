#include <stdio.h>
int main(){
	int top = 0;
	for(int i = 1;i<=10;i++){
		printf("bir sayi giriniz");
		int sayi;
		scanf("%d",&sayi);
		top = top + sayi;
	}
	printf("sayilarin toplami : %d \n",top);
	printf("sayilarin ortalamasi : %d",top/10);
}

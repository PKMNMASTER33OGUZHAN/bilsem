#include <stdio.h>
int main(){
	for(int a = 1;a<=10;a++){
		for(int c=1;c<=10;c++){
			if((a+c)%2==0)
			printf("*");
			else
			printf(" ");
		}
		printf("\n");
	}
}

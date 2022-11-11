#include <stdio.h>
int main(){
	int girilen;
	int enbuyuk=0;
	for (int i=0;i<3;i++){
		scanf("%d",&girilen);
		if (girilen>enbuyuk)
		enbuyuk=girilen;
	}
	printf("enbuyuk:%d",enbuyuk);
}

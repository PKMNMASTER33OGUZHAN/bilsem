#include <stdio.h>
int main(){
    int top = 0;
    int say = 0;
    int sayi=0;
    while(sayi!= -1){
    	printf("bir sayi giriniz");
    	
    	scanf("%d",&sayi);
    	/* if(sayi==0)
    	          continue;*/
        if(sayi==-1)
                   break;
        top = top + sayi;
        say ++;
        printf("top ; %d say: %d\n",top,sayi,say);
        
	}
	printf("toplam: %d\n",top);
	printf("ortalama: %d",top/say);
}

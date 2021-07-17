#include<stdio.h>

int main(){
    int pswd = 3049;
    int atmpt;
    while (1)
    {
        printf("Enter Password: ");
        scanf("%d", &atmpt);

        if (atmpt==pswd)
        {
            printf("welcome !");
            break;
        }
        
    }
    
}
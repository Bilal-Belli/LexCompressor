%start startState numberOfIterations multipleChar
%{
#include <string.h>
int cmpt;
char character[1];
int x;
%}
%%
<startState>[a-zA-Z]          {strcpy(character,yytext); BEGIN numberOfIterations;}
<numberOfIterations>[0-9]+    {x = atoi(yytext);for(int i=0;i<x;i++){fprintf(yyout,"%s",character);} BEGIN startState;}
%%
int yywrap(){
    return 1;
}
int main(){
    printf("Processing...");
    extern FILE *yyin, *yyout;
    yyin = fopen("Output.txt", "r");
    yyout = fopen("Output2.txt", "w");
    BEGIN startState;
    yylex();
    return 0;
}
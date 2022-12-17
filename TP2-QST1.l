%start startState singleChar multipleChar
%{
#include <string.h>
int cmpt;
char character[1];
%}
%%
<startState>[a-zA-Z]    {printf("%s",yytext); strcpy(character,yytext); cmpt=1; BEGIN singleChar;/*ils sont des conditions initials*/}
<singleChar>[a-zA-Z]    {if(strcmp(character, yytext) == 0){cmpt++;BEGIN multipleChar;}else{fprintf(yyout,"%s%d", character,cmpt);cmpt=1;strcpy(character,yytext);}}
<multipleChar>[a-zA-Z]  {if(strcmp(character, yytext) == 0){cmpt++;}else{fprintf(yyout, "%s%d", character,cmpt);cmpt=1;strcpy(character,yytext);BEGIN singleChar;}}
<singleChar,multipleChar>[ \t]     {fprintf(yyout, "%s%d ", character,cmpt);cmpt=1;BEGIN startState; }
<singleChar,multipleChar>\n        { fprintf(yyout, "%s%d", character,cmpt);cmpt=1;BEGIN startState; }
<singleChar,multipleChar><<EOF>>    {fprintf(yyout,"%s%d", character,cmpt); yyterminate();}
%%
int yywrap(){
    return 1;
}
int main(){
    printf("Processing...");
    extern FILE *yyin, *yyout;
    yyin = fopen("test.txt", "r");
    yyout = fopen("Fichier-Compresser.txt", "w");
    BEGIN startState;
    yylex();
    printf("\nEnd of Process.(Lex)\n");
    return 0;
}
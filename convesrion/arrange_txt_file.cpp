#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
int cifra(char c)
{
    return (c>='0' && c<='9') || c=='.';
}
void sredi(char *s)
{
    char p[100];
    for(int i=0;s[i]!='\0';i++)
        if(s[i]=='-')
            if(cifra(s[i-1]))
            {
                strcpy(p,s+i);
                s[i]=' ';
                s[i+1]='\0';
                strcat(s,p);
            }
}
int main()
{
    char ime_in[]=  "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB/";
    char ime_out[]= "C:/Users/matij/Desktop/M31_direktna_blizu/txt/DBHSB1/";
    char kartd[]="disk_";
    char kartb[]="bulge_";
    char karth[]="halo_";
    char karts[]="stars_";
    char kartbnd[]="bndry_";
    char txt[]=".txt";
    int n=100;
    char deo[100];
    for(int i=0;i<=n;i++)
    {
        if(i<=9)
            strcpy(deo,"00");
        if(i<=99 && i>=10)
            strcpy(deo,"0");
        if(i>=100)
            strcpy(deo,"");
        char diskkart_in[100];
        char bulgekart_in[100];
        char halokart_in[100];
        char starskart_in[100];
        char bndrykart_in[100];

        char diskkart_out[100];
        char bulgekart_out[100];
        char halokart_out[100];
        char starskart_out[100];
        char bndrykart_out[100];

        char index[100];
        itoa(i,index,10);
        strcpy(diskkart_in,ime_in);
        strcat(diskkart_in,kartd);
        strcat(diskkart_in,deo);
        strcat(diskkart_in,index);
        strcat(diskkart_in,txt);

        strcpy(diskkart_out,ime_out);
        strcat(diskkart_out,kartd);
        strcat(diskkart_out,deo);
        strcat(diskkart_out,index);
        strcat(diskkart_out,txt);

        strcpy(bulgekart_in,ime_in);
        strcat(bulgekart_in,kartb);
        strcat(bulgekart_in,deo);
        strcat(bulgekart_in,index);
        strcat(bulgekart_in,txt);

        strcpy(bulgekart_out,ime_out);
        strcat(bulgekart_out,kartb);
        strcat(bulgekart_out,deo);
        strcat(bulgekart_out,index);
        strcat(bulgekart_out,txt);

        strcpy(halokart_in,ime_in);
        strcat(halokart_in,karth);
        strcat(halokart_in,deo);
        strcat(halokart_in,index);
        strcat(halokart_in,txt);

        strcpy(halokart_out,ime_out);
        strcat(halokart_out,karth);
        strcat(halokart_out,deo);
        strcat(halokart_out,index);
        strcat(halokart_out,txt);

        strcpy(bndrykart_in,ime_in);
        strcat(bndrykart_in,kartbnd);
        strcat(bndrykart_in,deo);
        strcat(bndrykart_in,index);
        strcat(bndrykart_in,txt);

        strcpy(bndrykart_out,ime_out);
        strcat(bndrykart_out,kartbnd);
        strcat(bndrykart_out,deo);
        strcat(bndrykart_out,index);
        strcat(bndrykart_out,txt);

        strcpy(starskart_in,ime_in);
        strcat(starskart_in,karts);
        strcat(starskart_in,deo);
        strcat(starskart_in,index);
        strcat(starskart_in,txt);

        strcpy(starskart_out,ime_out);
        strcat(starskart_out,karts);
        strcat(starskart_out,deo);
        strcat(starskart_out,index);
        strcat(starskart_out,txt);

        char s[100];
        ifstream ulazd(diskkart_in);
        ofstream izlazd(diskkart_out);
        while(!ulazd.eof())
        {
            ulazd.getline(s,100);
            sredi(s);
            izlazd<<s<<endl;
        }
        ulazd.close();
        izlazd.close();
        cout<<"Gotov: "<<diskkart_out<<endl;

        ifstream ulazb(bulgekart_in);
        ofstream izlazb(bulgekart_out);
        while(!ulazb.eof())
        {
            ulazb.getline(s,100);
            sredi(s);
            izlazb<<s<<endl;
        }
        ulazb.close();
        izlazb.close();
        cout<<"Gotov: "<<bulgekart_out<<endl;

        ifstream ulazh(halokart_in);
        ofstream izlazh(halokart_out);
        while(!ulazh.eof())
        {
            ulazh.getline(s,100);
            sredi(s);
            izlazh<<s<<endl;
        }
        ulazh.close();
        izlazh.close();
        cout<<"Gotov: "<<halokart_out<<endl;


        ifstream ulazs(starskart_in);
        ofstream izlazs(starskart_out);
        while(!ulazs.eof())
        {
            ulazs.getline(s,100);
            sredi(s);
            izlazs<<s<<endl;
        }
        ulazs.close();
        izlazs.close();
        cout<<"Gotov: "<<starskart_out<<endl;

        ifstream ulazbnd(bndrykart_in);
        ofstream izlazbnd(bndrykart_out);
        while(!ulazbnd.eof())
        {
            ulazbnd.getline(s,100);
            sredi(s);
            izlazbnd<<s<<endl;
        }
        ulazbnd.close();
        izlazbnd.close();
        cout<<"Gotov: "<<bndrykart_out<<endl;

        cout<<"Gotov ceo blok: "<<index<<endl;
    }

}

#include<bits/stdc++.h>
#define SIZE 5
using namespace std;

int push(int [],int,int);
int pop(int [],int);
void topelement(int [],int);
void sizeofstack(int top);
void display(int [],int);
int isfull(int);
int isempty(int);

int main()
{
    int stack[SIZE],ch,top=-1,data;
    while(ch!=6)
    {
        cout<<"PUSH"<<endl;
        cout<<"POP"<<endl;
        cout<<"TOP ELEMENT"<<endl;
        cout<<"SIZE"<<endl;
        cout<<"DISPLAY"<<endl;
        cout<<"EXIT"<<endl;
        cout<<"Enter Choice: ";
        cin>>ch;
        switch(ch)
        {
            case 1:
                cout<<"Enter data: ";
                cin>>data;
                top=push(stack,top,data);
            break;
            case 2:
                top=pop(stack,top);
            break;
            case 3:
                topelement(stack,top);
            break;
            case 4:
                sizeofstack(top);
            break;
            case 5:
                display(stack,top);
            break;
        }
    }
    return 0;
}

int push(int stack[],int top,int data)
{
    if(isfull(top))
        cout<<"Stack Overflow"<<endl;
    else
    {
        top++;
        stack[top]=data;
    }
    return top;
}

int pop(int stack[],int top)
{
    int data;
    if(isempty(top))
        cout<<"Stack Underflow"<<endl;
    else
    {
        data=stack[top];
        top--;
        cout<<"Deleted data is: "<<data<<endl;
    }
    return top;
}

void topelement(int stack[],int top)
{
    cout<<stack[top]<<endl;
}

void sizeofstack(int top)
{
    cout<<top+1<<endl;
}

void display(int stack[],int top)
{
    if(isempty(top))
        cout<<"Stack is empty"<<endl;
    else
    {
        for(int i=top;i>=0;i--)
            cout<<stack[i]<<endl;
    }
}

int isfull(int top)
{
    if(top==SIZE-1)
        return 1;
    else
        return 0;
}

int isempty(int top)
{
    if(top==-1)
        return 1;
    else
        return 0;
}

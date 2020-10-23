#include <stdio.h>
#include <malloc.h>

struct node
{
    int x;
    struct node *nxt;
}*f=NULL,*r=NULL,*p;

void InsertBeg();
void InsertEnd();
void Deletenode();
void Display();

int main()
{
    int c,fl=1;
    while(fl)
    {
        printf("1.Insert at the beginning\n2.Insert at the end\n3.Delete a node\n4.Display the list\n5.Exit\nEnter choice:");
        scanf("%d",&c);

        switch(c)
        {
            case 1:
                {
                    InsertBeg();
                    break;
                }
            case 2:
                {
                    InsertEnd();
                    break;
                }
            case 3:
                {
                    Deletenode();
                    break;
                }
            case 4:
                {
                    Display();
                    break;
                }
            case 5:
                {
                    fl=0;
                    break;
                }
            default:
                {
                    printf("Invalid choice.\n");
                }
        }
    }
    return 0;
}

void InsertBeg()
{
    int a;
    printf("Enter data:");
    scanf("%d",&a);
    p = (struct node*)malloc(sizeof(struct node));
    //p= new node;
    p->x=a;
    p->nxt=NULL;
    if(f==NULL)
    f=r=p;
    else
    {
        p->nxt=f;
        f=p;
    }

    printf("Inserted successfully.\n");
}

void InsertEnd()
{
    int a;
    printf("Enter data:");
    scanf("%d",&a);
    //p=new node;
    p=(struct node*)malloc(sizeof(struct node));
    p->x=a;
    p->nxt=NULL;
    if(f==NULL)
    f=r=p;
    else
    {
        r->nxt=p;
        r=p;
    }
    printf("Inserted successfully.\n");
}

void Deletenode()
{
    int a,fl=0;
    //node prep=new node;
    struct node *prep= (struct node*)malloc(sizeof(struct node));
    printf("%d",f->x);
    if(f==NULL)
    printf("List empty.\n");
    else
    {
        printf("Enter the data of the node to be deleted:");
        scanf("%d",&a);
        prep=p=f;
        while(p)
        {
            if(p->x==a)
            {
                fl=1;
                if(p==f)
                {
                    f=p->nxt;
                }
                else if(p==r)
                {
                    prep->nxt=NULL;
                    r=prep;
                }
                else
                {
                    prep->nxt=p->nxt;
                }
                //delete p;
                free(p);
                break;
            }
            else
            {
                prep=p;
                p=p->nxt;
            }
        }

        if(fl)
        printf("Deleted successfully.\n");
        else
        printf("Node not found.\n");
    }
}

void Display()
{
    printf("The list is: ");
    p=f;
    while(p)
    {
        printf("%d ",p->x);
        p=p->nxt;
    }
    printf("\n");
}



#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "time.h"
#include "DateTime.h"
#include "Objects.h"
#include "Headers.h"
#include "Structs.h"
#include "conio.h"
#include "windows.h"
#pragma warning(disable : 4996)

void PrintObjects(HeaderA**);
int InsertNewObject(HeaderA**, char*, int);
Object3* RemoveExistingObject(HeaderA**, char*);
Node* CreateBinaryTree(HeaderA** ppStruct5);
void TreeTraversal(Node* pTree);
Node* DeleteTreeNode(Node* pTree, unsigned long int Code);

void DrawTree(Node*, int);
void Tests1(HeaderA**, int);
void Tests2(HeaderA**, int);

// Global variables
HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
WORD saved_attributes;
char red[] = "red";
char blue[] = "blue";
char green[] = "green";
char none[] = "";

// Object3, Struct5 | Kasper Vaus 206465IACB
int main()
{
	/* To style console text */
	CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
	GetConsoleScreenBufferInfo(hConsole, &consoleInfo);
	saved_attributes = consoleInfo.wAttributes;
	/*************************/

	int N = 35; // 1. N = 35
	HeaderA** ppStruct5 = GetStruct5(3, N); // generate source structure with Object3, length N

	Tests1(ppStruct5, N); // First 3 functions
	Tests2(ppStruct5, N);  // Last 3 functions
	
	printf("\n\nPress any key to close this window . . .\n");
	getch();
	return 0;
}

void PrintObjects(HeaderA** ppStruct5)
{
	int n = 0;
	// ppStruct5 for every letter in alphabet
	for (int i = 0; i < 26; ++i)
	{
		// traverse every HeaderA in every ppStruct5
		for (HeaderA* p = ppStruct5[i]; p; p = p->pNext)
		{
			// traverse every Object3 in every HeaderA
			for (Object3* q = (Object3*)p->pObject; q; q = q->pNext)
			{
				printf("%d) %s %lu %02d:%02d:%02d\n", ++n, q->pID, q->Code, q->sTime1.Hour, q->sTime1.Minute, q->sTime1.Second);
			}
		}
	}
}

int checkID(char const* id)
{
	// if first letter of 1. word not capital letter
	if (*id < 'A' || *id > 'Z')
	{
		return 0;
	}
	// if any non-first letter in 1. word is not a small letter
	for (++id; *id != ' ' && *id != 0; ++id)
	{
		if (*id < 'a' || *id > 'z')
		{
			return 0;
		}
	}
	// if no space after 1. word
	if (*id != ' ')
	{
		return 0;
	}
	++id;
	// if first letter of 2. word is not capital letter
	if (*id < 'A' || *id > 'Z')
	{
		return 0;
	}
	// if any non-first letter in 2. word is not a small letter
	for (++id; *id != 0; ++id)
	{
		if (*id < 'a' || *id > 'z')
		{
			return 0;
		}
	}
	// ID check success!
	return 1;
}

Object3* makeNode(char const* pNewID, int NewCode)
{
	// make a new Object3 type object & give memory
	Object3* p = (Object3*)malloc(sizeof(Object3));
	if (!p)
		return NULL;
	p->pID = (char*)malloc(strlen(pNewID) + 1);
	if (!p->pID)
		return NULL;
	strcpy(p->pID, pNewID);
	p->Code = NewCode;
	time_t RawTime;
	time(&RawTime);
	GetTime1(RawTime, &p->sTime1);
	p->pNext = NULL;
	return p;
}

int InsertNewObject(HeaderA** ppStruct5, char* pNewID, int NewCode)
{
	// check if ID is valid
	if (!checkID(pNewID))
	{
		return 0;
	}
	int a = *pNewID - 'A'; // 1. word 1. letter (A=0, B=1, .., Z=25)
	char b = ' ';		   // 2. word 1. letter (A=65, B=66, .., Z=90)
	// find 1. letter of 2. word
	for (int i = 0; pNewID[0] != 0; ++i)
	{
		if (pNewID[i] == ' ')
		{
			b = pNewID[i + 1];
			break;
		}
	}
	// if no ppStruct5 for letter
	if (!ppStruct5[a])
	{
		ppStruct5[a] = (HeaderA*)malloc(sizeof(HeaderA));
		if (!ppStruct5[a])
			return 0;
		ppStruct5[a]->pObject = NULL;
		ppStruct5[a]->cBegin = b;
		ppStruct5[a]->pNext = NULL;
	}
	HeaderA* binder = ppStruct5[a];
	// if letter of new entry comes before letter of first binder
	// put new entry as first, connect current after it
	if (binder->cBegin > b)
	{
		ppStruct5[a] = (HeaderA*)malloc(sizeof(HeaderA));
		if (!ppStruct5[a])
			return 0;
		ppStruct5[a]->pObject = NULL;
		ppStruct5[a]->cBegin = b;
		ppStruct5[a]->pNext = binder;
		binder = ppStruct5[a];
	}
	// if letter of new entry comes after letter of first binder
	// find where new entry fits
	// E.g. Current binders are ['A', 'C'], new entry is ['B']. Insert new entry as ['A', 'B', 'C']
	// if binder already exists, insert into linked list of objects
	else if (binder->cBegin != b)
	{
		while (binder->pNext && binder->pNext->cBegin < b)
		{
			binder = binder->pNext;
		}
		if (!binder->pNext || binder->pNext->cBegin != b)
		{
			HeaderA* t = binder->pNext;
			binder->pNext = (HeaderA*)malloc(sizeof(HeaderA));
			if (!binder->pNext)
				return 0;
			binder->pNext->pObject = NULL;
			binder->pNext->cBegin = b;
			binder->pNext->pNext = t;
		}
		binder = binder->pNext;
	}
	// if no objects belong to that binder, add the first one
	if (!binder->pObject)
	{
		binder->pObject = makeNode(pNewID, NewCode);
		printf("Successfully added %s\n", pNewID);
		return 1;
	}
	// insert into existing linked list of objects (objects already belong to binder)
	Object3* p = (Object3*)binder->pObject;
	while (p->pNext)
	{
		if (strcmp(pNewID, p->pID) == 0)
		{
			return 0;
		}
		p = p->pNext;
	}
	if (strcmp(pNewID, p->pID) == 0)
	{
		return 0;
	}
	p->pNext = makeNode(pNewID, NewCode);
	printf("Successfully added %s\n", pNewID);
	return 1;
}

Object3* RemoveExistingObject(HeaderA** ppStruct5, char* pExistingID)
{
	// check if ID is valid
	if (!checkID(pExistingID))
	{
		return NULL;
	}
	int a = *pExistingID - 'A'; // 1. word 1. letter (a=0, b=1, .., z=25)
	char b = ' ';				// 2. word 1. letter (a=65, b=66, .., z=90)
	for (int i = 0; pExistingID[0] != 0; ++i)
	{
		if (pExistingID[i] == ' ')
		{
			b = pExistingID[i + 1];
			break;
		}
	}
	// nothing to remove if no ppStruct5 for letter
	if (!ppStruct5[a])
	{
		return NULL;
	}
	HeaderA* binder = ppStruct5[a];
	// move to correct HeaderA
	while (binder && binder->cBegin < b)
	{
		binder = binder->pNext;
	}
	// nothing to remove if no binder for that letter
	if (!binder || binder->cBegin != b)
	{
		return NULL;
	}
	// look for matching ID to delete
	for (Object3* p = (Object3*)binder->pObject, *q = NULL; p; q = p, p = p->pNext)
	{
		if (strcmp(pExistingID, p->pID) == 0)
		{
			// if no objects in binder
			if (!q)
			{
				binder->pObject = p->pNext;
				// del binder
			}
			else
			{
				q->pNext = p->pNext;
			}
			printf("Successfully removed %s\n", p->pID);
			return p;
		}
	}
	return NULL;
}

Node* newBTNode(Object3* pObject)
{
	// make node for binary tree
	Node* node = (Node*)malloc(sizeof(Node));
	if (!node)
		return NULL;
	node->pObject = pObject;
	node->pLeft = node->pRight = NULL;
}

unsigned long int key(Node* p)
{
	// input BT node, output Code belonging to object in node
	return ((Object3*)p->pObject)->Code;
}

Node* CreateBinaryTree(HeaderA** ppStruct5)
{
	Node* pTree = NULL;
	// ppStruct5 for every letter in alphabet
	for (int i = 0; i < 26; ++i)
	{
		// traverse every HeaderA in every ppStruct5
		for (HeaderA* p = ppStruct5[i]; p; p = p->pNext)
		{
			// traverse every Object3 in every HeaderA
			for (Object3* q = (Object3*)p->pObject; q; q = q->pNext)
			{
				// if tree is empty, create first node
				if (!pTree)
				{
					pTree = newBTNode(q);
				}
				else
				{
					Node* pp = pTree, * qq = NULL;
					// until reaches bottom of tree
					while (pp)
					{
						qq = pp;
						// move left if Code is lower
						if (q->Code < key(pp))
						{
							pp = pp->pLeft;
						}
						// move right if Code is higher
						else
						{
							pp = pp->pRight;
						}
					}
					// if code is lower, make new child to left
					if (q->Code < key(qq))
					{
						qq->pLeft = newBTNode(q);
					}
					// if code is higher, make new child to right
					else
					{
						qq->pRight = newBTNode(q);
					}
				}
			}
		}
	}
	return pTree;
}

void TreeTraversal(Node* pTree)
{
	if (pTree)
	{
		// traverse tree using left-root-right
		TreeTraversal(pTree->pLeft);
		Object3* q = (Object3*)pTree->pObject;
		printf("%s %lu %02d:%02d:%02d\n", q->pID, q->Code, q->sTime1.Hour, q->sTime1.Minute, q->sTime1.Second);
		TreeTraversal(pTree->pRight);
	}
}

Node* DeleteTreeNode(Node* pTree, unsigned long int Code)
{
	Node* p = pTree, * q = NULL;
	// look for Code in tree
	while (p && key(p) != Code)
	{
		q = p;
		if (Code < key(p))
		{
			p = p->pLeft;
		}
		else
		{
			p = p->pRight;
		}
	}
	// return if no match found
	if (!p)
	{
		printf("Failed to delete %d\n", Code);
		return pTree;
	}
	// found match has no left or right child
	if (!p->pLeft || !p->pRight)
	{
		Node* rep = p->pLeft ? p->pLeft : p->pRight;
		if (!q)
			return rep;
		if (p == q->pLeft)
		{
			q->pLeft = rep;
		}
		else
		{
			q->pRight = rep;
		}
	}
	// found match has both children
	else
	{
		Node* r = NULL, * t = p->pRight;
		while (t->pLeft != NULL)
		{
			r = t;
			t = t->pLeft;
		}
		if (r)
		{
			r->pLeft = t->pRight;
		}
		else
		{
			p->pRight = t->pRight;
		}
		p->pObject = t->pObject;
	}
	printf("Successfully deleted %d\n", Code);
	return pTree;
}

void SetColor(char* Color)
{
	if (strcmp(Color, "blue") == 0)
		SetConsoleTextAttribute(hConsole, FOREGROUND_BLUE);
	else if (strcmp(Color, "red") == 0)
		SetConsoleTextAttribute(hConsole, FOREGROUND_RED);
	else if (strcmp(Color, "green") == 0)
		SetConsoleTextAttribute(hConsole, FOREGROUND_GREEN);
	else
		SetConsoleTextAttribute(hConsole, saved_attributes);
}

void DrawTree(Node* pTree, int space)
{
	if (space == 0) {
		SetColor(blue);
		printf("\n8. Drawing the binary tree\n");
		SetColor(green);
	}
	if (pTree == NULL) {
		for (int i = 10; i < space+10; i++)
		{
			printf(" ");
		}
		printf("-");
	}
	else {
		space += 10;
		DrawTree(pTree->pRight, space);
		printf("\n");
		for (int i = 10; i < space; i++)
		{
			printf(" ");
		}
		printf("%lu\n", ((Object3*)pTree->pObject)->Code);
		DrawTree(pTree->pLeft, space);
	}
}

void Tests1(HeaderA** ppStruct5, int N)
{	
	// 1. PART TESTS
	SetColor(red);
	printf(" \n1. PART TESTS\n ");
	SetColor(blue);
	printf("\n2. (N=35) Printing source structure\n");			// 2. Print source structure
	SetColor(none);
	PrintObjects(ppStruct5);
	SetColor(blue);
	printf("\n\n3.1. Adding objects\n");						// 3.1. Add objects with ID's
	SetColor(none);
	char p[][6] = { "Dx Gz", "Dx Ga", "Db Aa", "Dk Za", "Dr Wa", "Aa Aa", "Ab Ba", "Za Aa", "Za Ab", "Za Ba", "Wx Xa", "Wx Aa", "zb Kk", "Zc ca", "Dr Wa", "ZB kk", "Fa", "Fa_Fa" };
	for (int i = 0; i < 18; ++i)
	{
		if (!InsertNewObject(ppStruct5, p[i], rand()))
		{
			printf("Error when adding %s\n", p[i]);
		}
	}
	SetColor(blue);
	printf("\n\n3.2. Printing objects\n");						// 3.2. Print added objects
	SetColor(none);
	PrintObjects(ppStruct5);
	SetColor(blue);
	printf("\n\n4.1. Removing objects\n");						// 4.1. Remove objects with given ID's
	SetColor(none);
	for (int i = 0; i < 18; ++i)
	{
		if (!RemoveExistingObject(ppStruct5, p[i]))
		{
			printf("Error when removing %s\n", p[i]);
		}
	}
	SetColor(blue);
	printf("\n\n4.2. Printing objects\n");						// 4.2. Print after removing objects
	SetColor(none);
	PrintObjects(ppStruct5);
}

void Tests2(HeaderA** ppStruct5, int N)
{
	// 2. PART TESTS
	SetColor(red);
	printf("\n2. PART TESTS\n");
	SetColor(blue);
	printf("\n2. (N=35) Printing source structure\n");			// 2. Print source structure
	SetColor(none);
	PrintObjects(ppStruct5);
	SetColor(blue);
	printf("\n\n3. Creating and printing binary tree\n");		// 3. Create and print the binary tree
	SetColor(none);
	Node* tree = CreateBinaryTree(ppStruct5);
	TreeTraversal(tree);
	SetColor(blue);
	printf("\n\n4. Deleting root and printing binary tree\n"); // 4. Delete tree root and print the tree
	SetColor(none);
	tree = DeleteTreeNode(tree, ((Object3*)tree->pObject)->Code);
	TreeTraversal(tree);
	SetColor(blue);
	printf("\n\n5. N = 10");									// 5. N = 10
	N = 10;
	ppStruct5 = GetStruct5(3, N);
	printf("\n6. Printing source structure\n");				// 6. Print source structure
	SetColor(none);
	PrintObjects(ppStruct5);
	SetColor(blue);
	printf("\n\n7. Creating and printing binary tree\n");		// 7. Create and printing the binary tree
	tree = CreateBinaryTree(ppStruct5);
	SetColor(none);
	TreeTraversal(tree);
	DrawTree(tree, 0);															// 8. Draw the binary tree
	SetColor(blue);
	printf("\n\n9.1. Deleting nodes\n");						// 9.1 Delete nodes
	SetColor(none);
	tree = DeleteTreeNode(tree, 101110100);
	tree = DeleteTreeNode(tree, 4455511);
	tree = DeleteTreeNode(tree, 258186307);
	tree = DeleteTreeNode(tree, 55555);
	SetColor(blue);
	printf("\n\n9.2. Printing binary tree\n");					// 9.2. Print the tree
	SetColor(none);
	TreeTraversal(tree);
}
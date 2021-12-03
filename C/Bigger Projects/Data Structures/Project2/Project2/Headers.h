//
//            Header declarations
//            -------------------

typedef struct heada
{
	void *pObject; // Pointer to the linked list of objects. 
				   // Objects may be of types Object1, ....Object10.
				   // Declarations of objects are in file Objects.h
	char cBegin;   // The linked list contains objects in which
				   // the first letter of the second word of ID
				   // (Struct5) 
				   // is cBegin.
	struct heada *pNext;
}	HeaderA;

typedef struct node
{
	void *pObject;		 // Pointer to object belonging to this node
						 // Objects may be of types Object1, ....Object10.
						 // Declarations of objects are in file Objects.h
	struct node *pLeft,  // Pointer to the left child node
				*pRight; // Pointer to the right child node
}	Node;

typedef struct stack
{
	void *pObject;
	struct stack *pNext;
}	Stack;
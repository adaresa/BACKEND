//
//            Object declarations
//            -------------------

typedef struct ob3
{  // formatting string for printf is "%d) %s %lu %02d:%02d:%02d\n", the result is for example "1) Abcde 100 15:52:07"
   // or "10) Abcde Fghij 100 15:52:07"
	char *pID;
	unsigned long int Code;
	Time1 sTime1;  // Declaration of Time1 is in file DateTime.h
	struct ob3 *pNext;
} Object3;

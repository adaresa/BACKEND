//
//            Date and time: structure declarations and function prototypes
//            -------------------------------------------------------------

typedef struct
{
	int Hour;
	int Minute;
	int Second;
} Time1;

int GetTimeString(time_t RawTime, int nResult, char *pResult);
/*
RawTime - time from the computer clock. Example for getting RawTime:
#include "time.h"
time(&RawTime);
nResult - number of bytes in the result buffer
pResult - pointer to the result buffer
Format for result: "hh:mm:ss", for example half past two is "14:30:00"
Return value 0 - nResult is too small or pResult, no result
1 - done
*/

int GetTime1(time_t RawTime, Time1 *pTime1);
/*
RawTime - see above
pTime1 - pointer to the result
Return value 0 - pTime1 is not correct, no result
1 - done
*/

typedef struct
{
	int Day;
	int Month; // from 1 to 12
	int Year;
} Date1;

typedef struct
{
	int Day;
	char Month[4]; // "Jan", "Feb", ...
	int Year;
} Date2;

typedef struct
{
	int Day;
	char *pMonth; // pointer to full name in Estonian
	int Year;
} Date3;
int GetDateString(time_t RawTime, int nResult, char *pResult);
/*
RawTime - time from the computer clock. Example for getting RawTime:
#include "time.h"
time(&RawTime);
nResult - number of bytes in the result buffer
pResult - pointer to the result buffer
Format for result: "dd-mm-yyyy", for example the 10-th of October 2010 is "10-15-2010"
Return value 0 - nResult is too small or pResult is not correct, no result
1 - done
*/

int GetDate1(time_t RawTime, Date1 *pDate1);
/*
RawTime - see above
pDate1 - pointer to the result
Return value 0 - pDate1 is not correct, no result
1 - done
*/

int GetDate2(time_t RawTime, Date2 *pDate2);
/*
RawTime - see above
pDate2 - pointer to the result
Return value 0 - pDate2 is not correct, no result
1 - done
*/

int GetDate3(time_t RawTime, int nMonthBuf, char *pMonthBuf, Date3 *pDate3);
/*
RawTime - see above
nMonthBuf - number of bytes in the buffer for month name
pMonthBuf - pointer to the buffer into which the month name will be stored
pDate3 - pointer to the result
Return value 0 - nMonthBuf is too small or pMonthBuf or pDate2 is not correct, no result
1 - done
*/

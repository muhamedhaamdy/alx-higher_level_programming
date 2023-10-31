#include "lists.h"
/**
 * check_cycle - function that check for a cycle in linked list
 * @list : linked list
 * Return : a boolean (1 or 0)
*/
int check_cycle(listint_t *list)
{
	listint_t *fastPtr = list, *slowPtr = list;

	while (fastPtr != NULL && fastPtr->next != NULL  && slowPtr != NULL)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
			return (1);
	}
	return (0);
}

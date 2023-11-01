#include "lists.h"
int is_sorted(listint_t *list)
{
	listint_t *curr = list;

	while (curr && curr->next)
	{
		if (curr->n > curr->next->n)
			return (0);
		curr = curr->next;
	}
	return (1);
}
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *tmp;

	curr = *head;
	add_nodeint_end(&tmp, number);
	if (!is_sorted(*head))
		return (NULL);
	while (curr->next)
	{
		if (curr->next->n > number)
		{
			tmp->next = curr->next;
			curr->next = tmp;
			return (tmp);
		}
		curr = curr->next;
	}
	return (NULL);
}

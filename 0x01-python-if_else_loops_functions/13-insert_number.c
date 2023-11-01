#include "lists.h"

/**
 * insert_node - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to insert
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *tmp;

	curr = *head;
	tmp = malloc(sizeof(listint_t));
	if (!tmp)
	{
		return (NULL);
	}
	tmp->n = number;
	tmp->next = NULL;
	if (!curr || number < curr->n)
	{
		tmp->next = curr;
		return (*head = tmp);
	}
	while (curr)
	{
		if (!curr->next || curr->next->n > number)
		{
			tmp->next = curr->next;
			curr->next = tmp;
			return (tmp);
		}
		curr = curr->next;
	}
	return (NULL);
}

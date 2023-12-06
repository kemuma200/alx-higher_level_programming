#include "lists.h"

/**
 *free_listint_t - frees a list
 *@head: linkedlist
 *
 */
void free_listint_t(listint *head)
{
	listint *curr;
	while (head != NULL)
	{
		curr = head;
		head = head->next;
		free(curr);
	}
}

/**
 *print_listint - prints listint nodes
 *@h: linkedlist
 *Returns: number of nodes
 */

size_t print_listint(const listint *h)
{
	unsigned int n = 0;
	const listint_t *curr;


	curr = h;
	while (current != NULL)
	{
		printf("%i\n", curr->n);
		current = curr->next;
		n++;
	}
	return (n);

}
/**
 *add_nodeint_end - adds node to the end of the list
 *@head: linkedlist
 *@n: int to be included in new node
 *Returns: address of new node, else null
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new, *curr;


	curr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (curr->next != NULL)
			curr = curr->next;
		curr->next = new;
	}
	return (new);

}

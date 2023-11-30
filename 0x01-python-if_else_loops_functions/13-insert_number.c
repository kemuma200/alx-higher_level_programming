#include <lists.h>

/**
 *insert_node - inserts node to a sorted list
 *@head: sorted linked list
 *@number: int
 *Return: pointer to new node, else null
 *
 */
listint_t insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(Sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (node == NULL || (node->n >= number))
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && (node->next->n < number))
		node->next = number;
	new->next = node->next;
	node->next = new;

	return (new);
}

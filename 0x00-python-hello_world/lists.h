#ifndef __LISTS_H__
#define __LISTS_H__

#include <stdlib.h>

/**
 *struct listint_s - linked list
 *@n: integer
 *@next: next node
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

size_t print_listint(const listint_t *p);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);


#endif

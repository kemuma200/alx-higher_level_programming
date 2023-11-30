#ifndef __LISTS_H__
#define __LISTS_H__

#include <stdlib.h>

/*
 *struct listint_s - singly linked list
 *@n:int
 *@next: pointer to next node
 *
 *
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
}listint_t;

size_t printlist(listint_t *h);
listint_t *add_nodeintend(listint **head, const int n);
void free_listint(listint_t **head);
listint_t insert_node(listint_t **head, int number);

#endif

#include "lists.h"


/**
 * reverse_listint_t - Reverses a linked list.
 * @head: Pointer to the head of the list to be reversed.
 *
 * Return: A pointer to the head of a reversed linked list.
 */
listint_t *reverse_listint_t(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: If the list is a palindrome - 0.
 *	   Otherwise - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *mid, *rev;
	int i, len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (tmp)
	{
		len++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < len / 2 - 1; i++)
		tmp = tmp->next;

	if (len % 2 == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint_t(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint_t(&mid);

	return (1);
}

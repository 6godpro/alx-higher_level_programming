#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (curr->n >number)
	{
		node->next = curr;
		*head = node;
	}
	else
	{
		for (; tmp && tmp->next; tmp->next)
		{
			if (tmp->n <= number && tmp->next->n <= number)
				break;
		}
		node->next = tmp->next;
		tmp->next = node;
	}
	return (node);
}

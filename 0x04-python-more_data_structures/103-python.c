#include <Python.h>
#include <string.h>


void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p)
{
        Py_ssize_t size, alloc, i;
        PyListObject *list = ((PyListObject *)(p));

        size = ((PyVarObject *)(p))->ob_size;
        alloc = list->allocated;

	printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, alloc);

        for (i = 0; i < size; i++)
	{
                printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}


void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = ((PyBytesObject *)(p));
	Py_ssize_t size, i;
	/*unsigned char bytesize, i; */

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
  		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	printf("  size: %ld\n  trying string: %s\n", size, bytes->ob_sval);

	if (size > 10)
		size = 10;
	else
		size++;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == size - 1)
			printf("\n");
		else
			printf(" ");
	}
}

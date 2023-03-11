#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = ((PyListObject *)(p));

	size = PyList_Size(p);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, alloc);

	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}

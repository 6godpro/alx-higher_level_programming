#include <Python.h>


void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about the python list.
 * @p: A PyObject object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = ((PyListObject *)(p));

	fflush(stdout);

	size = ((PyVarObject *)(p))->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (strcmp(list->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(list->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: A PyObject object.
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt = ((PyFloatObject *)(p));
	char *buff;

	fflush(stdout);

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(flt->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}

/**
 * print_python_bytes - Prints basic info about the Python bytes.
 * @p: A PyObject object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = ((PyBytesObject *)(p));
	Py_ssize_t size, i;

	fflush(stdout);

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

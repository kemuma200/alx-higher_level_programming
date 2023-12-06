#include <Python.h>

/**
 *print_python_list_info - prints basic info about python lists"
 *@p: Pyobject list
 *
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	Pyobject *b;


	size = Py_Size(p);
	alloc = ((PyList *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++;
	{
		printf("Element %d: ", i);
		b = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(b)->tp_name);
	}

}

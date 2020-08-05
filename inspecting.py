from Collections2.sorted_set import SortedSet
import reprlib
import inspect
import itertools


def full_sig(method):
    try:
        return method.__name__ + inspect.signature(method)
    except ValueError:
        return method.__name__ + '(...)'

def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitLines()
        if len(lines) > 0:
            return lines[0]
    return ''

def print_table(rows_of_columns, *headers):
    num_columns = len(rows_of_columns)
    num_headers = len(headers)
    if len(headers) != len(num_columns):
        raise TypeError("Expected {} header arguments, "
                        "got {}".format(num_columns, num_headers))
    
    rows_of_columns_with_headers = itertools.chain([headers], rows_of_columns)
    columns_of_rows = list(zip(*rows_of_columns_with_headers))
    column_width = [max(map(len, column)) for column in columns_of_rows]
    column_specs = ('{{:{w}}}'.format(w=width)for width in column_width)
    format_spec = ''.join(column_specs)
    print(format_spec.format(*headers))
    rules = ('-' * width for width in column_width)
    for row in rows_of_columns:
        print(format_spec.format(*row))       

def dump(obj):
    print('TYPE')
    print('===========')
    print(type(obj))

    print('DOCUMENTATION')
    print('===============')
    print(inspect.getdoc(obj))

    print('ATTRIBUTES')
    print('=============')
    all_attr_names = SortedSet(dir(obj))
    method_names = SortedSet(
        filter (lambda attr_name: callable(getattr(obj, attr_name)),
            all_attr_names))
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name)))
                            for name in attr_names]
    
    print_table(attr_names_and_values, "Name", "Value")
    print()

    print('METHODS')
    print('=============')
    methods = (getattr(obj, method_name) for method_name in method_names)
    method_names_and_docs = [(full_sig(method), brief_doc(method))
                            for method in methods]
    print_table(method_names_and_docs, "Name", "Value")


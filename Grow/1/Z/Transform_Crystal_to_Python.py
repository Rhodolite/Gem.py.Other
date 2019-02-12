#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Z.Core                  import  arrange
from    Z.Crystal_ParseTree     import  Crystal_ParseTree
from    Z.Crystal_ParseTree     import  Crystal_Statement_Copyright
from    Z.Crystal_ParseTree     import  Crystal_Statement_Output_1
from    Z.Python_ParseTree      import  Python_ParseTree
from    Z.Python_ParseTree      import  Python_Statement_Comment_Many
from    Z.Python_ParseTree      import  Python_Statement_Print_1


#
#   Crystal_ParseTree.convert_crystal_to_python
#
def Crystal_ParseTree__convert_crystal_to_python(self, input_path):
    python_parse_tree = Python_ParseTree()

    for v in self.crystal_statements:
        statement = v.convert_crystal_to_python(input_path)

        if statement:
            python_parse_tree.append_python_statement(statement)

    return python_parse_tree


Crystal_ParseTree.convert_crystal_to_python = Crystal_ParseTree__convert_crystal_to_python


#
#   Crystal_Statement_Copyright.convert_crystal_to_python
#
def Crystal_Statement_Copyright__convert_crystal_to_python(self, path):
    copyright = self.extract_copyright(path)

    return Python_Statement_Comment_Many(
               tuple([
                   '#',
                   arrange('#   {}', copyright),
                   '#',
               ]),
           )


Crystal_Statement_Copyright.convert_crystal_to_python = Crystal_Statement_Copyright__convert_crystal_to_python


#
#   Crystal_Statement_Output_1.convert_crystal_to_python
#
def Crystal_Statement_Output_1__convert_crystal_to_python(self, path):
    return Python_Statement_Print_1(self.argument)


Crystal_Statement_Output_1.convert_crystal_to_python = Crystal_Statement_Output_1__convert_crystal_to_python

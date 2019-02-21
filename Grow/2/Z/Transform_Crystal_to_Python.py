#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#-<OLD>
#-from  Z.Core                          import  arrange
#-</OLD>

#+<NEW>
from    Capital.Core                    import  arrange
#+</NEW>


from    Z.Crystal_ParseTree     import  Crystal_ParseTree
from    Z.Crystal_ParseTree     import  Crystal_Statement_Copyright
from    Z.Crystal_ParseTree     import  Crystal_Statement_Output_1
from    Z.Python_ParseTree      import  Python_ParseTree
from    Z.Python_ParseTree      import  Python_Statement_Comment_Many
from    Z.Python_ParseTree      import  Python_Statement_Print_1


#
#   Pseudo Methods
#
#       Instead of declaring `.convert_crystal_to_python` methods in
#       their classes in "Z/Crystal_ParseTree" we declare them here
#       as "pseudo" methods (i.e.: as functions).
#
#       REASON:
#           We will eventually have 15+ converters (for all the different
#           langauges).
#
#           It's way more organized, and readable, to put each set of converter
#           code in it's own file instead of in the classes.
#
#       FUTURE:
#           In the future the Crystal Language will allow the following:
#
#               method Crystal_ParseTree.convert_crystal_to_python(input_path)
#
#           to make it clearer we are defining a method for a class.
#
#           At that point, we will declare methods for classes outside of
#           their class (once we have good support infrastructure and tools for
#           querying, finding, and modifying these methods).
#


#
#   Crystal_Statement_Copyright.convert_crystal_to_python
#
#       Consider this a "pseudo" method of `Crystal_Statement_Copyright`.
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


#
#   Crystal_Statement_Output_1.convert_crystal_to_python
#
def Crystal_Statement_Output_1__convert_crystal_to_python(self, path):
    return Python_Statement_Print_1(self.argument)



#
#   map__Crystal_Statement_Type__to__psuedo_method : Map { Crystal_Statement_* : Function }
#
#       PRESENT:
#           This maps a `Crystal_Statement_*` to a "psuedo method" (actually to
#           a function).
#
#       EXPLANATION:
#           What we really want to do, long term, is declare the
#           `.convert_crysal_to_python` methods in this file (instead of the
#           file the classes are declared in).
#
#           Since it is not standard in python, to declare methods outside of
#           classes (although it can be done), for now, we don't declare these
#           as methods, but as functions.
#
#           Thus we simply create a mapping table here and use it in
#           `Crystal_ParseTree__convert_crystal_to_python` (see note there).
#
map__Crystal_Statement_Type__to__psuedo_method = {
    Crystal_Statement_Copyright : Crystal_Statement_Copyright__convert_crystal_to_python,
    Crystal_Statement_Output_1  : Crystal_Statement_Output_1__convert_crystal_to_python,
}


#
#   convert_crystal_to_python
#
#       Consider this a "pseudo" method of `Crystal_ParseTree`.
#
#       (See note in `Crystal_Statement_Copyright__convert_crystal_to_python`
#       for an explanation of "psuedo" method).
#
def Crystal_ParseTree__convert_crystal_to_python(self, input_path):
    python_parse_tree = Python_ParseTree()

    for v in self.crystal_statements:
        #
        #   Find out "psuedo" method using the mapping table (converting the
        #   type of `v` to the "psuedo" method).
        #
        #   FUTURE:
        #       Once the crystal language supports declaring methods outside of
        #       their classes we can convert the next three lines of code to
        #       the much more readable:
        #
        #           statement = v.convert_crstal_to_python(input_path)
        #
        v__convert_crystal_to_python__pseudo_method = map__Crystal_Statement_Type__to__psuedo_method[type(v)]

        statement = v__convert_crystal_to_python__pseudo_method(v, input_path)

        if statement:
            python_parse_tree.append_python_statement(statement)

    return python_parse_tree

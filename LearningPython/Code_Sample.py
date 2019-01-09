#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


#
#   Python 2:
#
#   1.  code_sample: <Code #1 code_sample @Code_Sample.py:198>
#
#        arguments/locals:  total_arguments<3>; total_locals<9>
#          argument[0..2]:  argument_0, argument_1, argument_2
#             local[3..8]:  local_0, local_1, local_2, NestedClass, nested_1, local_4
#
#          cell_variables:  4
#                  [0..3]:  cell_0, cell_1, cell_2, cell_3
#
#          free_variables:  0           #   free variables only appear in nested functions when using cell variables
#
#     mostly_global_names:  2
#                  [0..2]:  len, object
#
#               constants:  12
#                     [0]:  None                                            #   Return value
#                     [1]:  0                                               #   local_0
#                     [2]:  'hello'                                         #   cell_0
#                     [3]:  'hi'                                            #   cell_1
#                     [4]:  'two'                                           #   cell_2
#                     [5]:  'three'                                         #   cell_3
#                     [6]:  1                                               #   local_1
#                     [7]:  2                                               #   local_2
#                     [8]:  'NestedClass'                                   #   Class name for `NestedClass`
#                     [9]:  <Code #6 NestedClass @Code_Sample.py:207>       #   Wrapper for `NestedClass`
#                    [10]:  <Code #7 nested_1 @Code_Sample.py:214>          #   `nested_1`
#                    [11]:  4                                               #   local_4
#
#   2.  wrapper to create NestedClass: <Code #6 NestedClass @Code_Sample.py:207>
#
#        arguments/locals:  total_arguments<0>; total_locals<0> #   Always 0 for a wrapper to create a class
#          cell_variables:  0                                   #   Always 0 for a wrapper to create a class
#          free_variables:  3
#                     [0]:  cell_0
#                     [1]:  cell_1
#                     [2]:  cell_2                      #   NOTE:  Only used to "pass through" to `nested_0`
#     mostly_global_names:  5
#                     [0]:  __name__                    #   Read global `__name__`, assign to local `__module__`
#                     [1]:  __module__                  #   Local `__module__` is copy of global `__name__`
#                     [2]:  length                      #   Global (part of calculating `h`)
#                     [3]:  h                           #   Local `h`
#                     [4]:  nested_0                    #   Local `nested_0`
#               constants:  1
#                     [0]:  'hmm'.                                          #   `h`
#                     [1]:  <Code #11 nested_0 @Code_Sample.py:210>         #   `nested_0`
#
#       Disassembled Code for the wrapper to create class `NestedClass`
#
#           NOTE:
#               This wrapper does not refer to the name `NestedClass`, the class is actually created
#               (and the name used there, in the *caller* to this wrapper).
#
#               All this wrapper does is create the "class locals", which is used as the 3rd argument to `type`
#               (The first argument to `type` is the name of the class, and the second argument to `type`
#               is the base classes, both of these are supplied by the *caller* to this wrapper).
#
#            207          0 LOAD_NAME                0 (__name__)
#                         3 STORE_NAME               1 (__module__)     #   __module__ = __name__
#
#            208          6 LOAD_DEREF               0 (cell_0)
#                         9 LOAD_DEREF               1 (cell_1)
#                        12 BINARY_ADD
#                        13 LOAD_NAME                2 (length)
#                        16 LOAD_CONST               0 ('hmm')
#                        19 CALL_FUNCTION            1
#                        22 BINARY_ADD
#                        23 STORE_NAME               3 (h)              #   h = cell_0 + cell_1 + length('hmm')
#
#            210         26 LOAD_CLOSURE             2 (cell_2)         #   "pass through" cell_2 to `nested_0`
#                        29 BUILD_TUPLE              1
#                        32 LOAD_CONST               1 (<Code #11 @Code_Sample.py:60>)
#                        35 MAKE_CLOSURE             0                  #   Create a closure around `nested_0`
#                                                                       #       with `cell_2` as free variable #0
#                        38 STORE_NAME               4 (nested_0)       #   Store in local `nested_0`
#
#                        41 LOAD_LOCALS             #   A class wrapper always loads the locals ...
#                        42 RETURN_VALUE            #   ... as the return value.
#
#   3.  nested method `nested_0`: <Code #11 nested_0 @Code_Sample.py:210>
#
#       NOTE:
#           This method is only nested *inside* `code_sample`.
#
#           It is *NOT* nested inside either the wrapper to create `NestedClass`, or `NestedClass` itself.
#
#           Like all methods, it ignores it's class, for nesting purposes.
#
#       NOTE #2:
#
#           Thus, for example, `h` refers to a global `h`.  It *DOES* not refer to `h` in `NestedClass`.
#
#        arguments/locals:  total_arguments<2>; total_locals<3>
#          argument[0..1]:  nested_argument_0, argument_1
#                local[2]:  local_0
#
#          cell_variables:  0
#
#          free_variables:  1
#                     [0]:  cell_2
#
#     mostly_global_names:  1
#                     [0]:  h
#
#               constants:  2
#                     [0]:  None                            #   Not Used
#                     [1]:  '0'                             #   local_0
#
#       Disassembled Code for the wrapper to create class `NestedClass`
#
#           211           0 LOAD_CONST               1 ('0')
#                         3 STORE_FAST               2 (local_0)        #   local_0 = '0'
#
#           212           6 LOAD_GLOBAL              0 (h)
#                         9 LOAD_FAST                2 (local_0)
#                        12 BINARY_ADD
#                        13 LOAD_DEREF               0 (cell_2)
#                        16 BINARY_ADD
#                        17 RETURN_VALUE                                #   return h + local_0 + cell_2
#
#   4.  nested method `nested_1`: <Code #7 nested_1 @Code_Sample.py:214>
#
#       NOTE:
#           Even though `nested_1` does *NOT* use `cell_2` (in the python code), it does *NEED*
#           to access `cell_2` as a free variable, in order to pass it down into it's nested
#           function `nested_nested`.
#
#        arguments/locals:  total_arguments<0>; total_locals<3>
#             local[0..2]:  nested_local_0, nested_nested, nested_local_2
#
#          cell_variables:  1
#                     [0]:  nested_cell_0
#
#          free_variables:  3
#                  [0..2]:  cell_0, cell_2, cell_3
#
#     mostly_global_names:  0
#
#               constants:  2
#                     [0]:  None                                            #   return value
#                     [1]:  'nested_cell_0'                                 #   nested_cell_0
#                     [2]:  <Code #18 nested_nested @Code_Sample.py:194>    #   nested_nested
#                     [3]:  '2'                                             #   nested_local_2
#
#       Disassembled Code for `nested_1`:
#
#           215           0 LOAD_DEREF               1 (cell_0)
#                         3 LOAD_DEREF               3 (cell_3)
#                         6 BINARY_ADD
#                         7 STORE_FAST               0 (nested_local_0)     #   nested_local_0 = cell_0 + cell_2
#
#           216          10 LOAD_CONST               1 ('nested_cell_0')
#                        13 STORE_DEREF              0 (nested_cell_0)      #   nested_cell_0 = 'nested_cell_0'
#
#           218          16 LOAD_CLOSURE             1 (cell_0)             #   Closure #0 for `nested_nested`
#                        19 LOAD_CLOSURE             2 (cell_2)             #   Closure #1 for `nested_nested`
#                        22 LOAD_CLOSURE             0 (nested_cell_0)      #   Closure #2 for `nested_nested`
#                        25 BUILD_TUPLE              3
#                        28 LOAD_CONST               2 (<Code #18 nested_nested @Code_Sample.py:218>)
#                        31 MAKE_CLOSURE             0                      #   Create a closure around `nested_nested`
#                                                                           #       with `cell_0` as free variable #0
#                                                                           #       with `cell_2` as free variable #1
#                                                                           #       with `nested_cell_0` as free variable #2
#                        34 STORE_FAST               1 (nested_nested)      #   Store in local `nested_nested`
#
#           221          37 LOAD_CONST               3 ('2')
#                        40 STORE_FAST               2 (nested_local_2)     #   nested_local_2 = '2'
#
#                        43 LOAD_CONST               0 (None)
#                        46 RETURN_VALUE                                    #   return None
#
#   5.  nested method `nested_nested`: <Code #18 nested_nested @Code_Sample.py:218>
#
#        arguments/locals:  total_arguments<0>; total_locals<0>
#          cell_variables:  0
#          free_variables:  3
#                  [0..2]:  cell_0, cell_2, nested_cell_0
#     mostly_global_names:  0
#               constants:  1
#                     [0]:  None                                            #   return value
#
#       Disassembled Code for `nested_nested`:
#
#           219           0 LOAD_DEREF               1 (cell_2)
#                         3 LOAD_DEREF               2 (nested_cell_0)
#                         6 BINARY_ADD
#                         7 LOAD_DEREF               0 (cell_0)
#                        10 BINARY_ADD
#                        11 RETURN_VALUE                                    #   return cell_2 + nested_cell_0 + cell_0
#
def code_sample(argument_0, argument_1, argument_2):
    local_0 = 0
    cell_0 = len('hello')
    cell_1 = len('hi')
    cell_2 = len('two')
    cell_3 = len('three')
    local_1 = 1
    local_2 = 2

    class NestedClass(object):      #   NestedClass = local_3
        h = cell_0 + cell_1 + length('hmm')

        def nested_0(nested_argument_0, nested_argument_1):
            local_0 = '0'
            return h + local_0 + cell_2

    def nested_1():
        nested_local_0 = cell_0 + cell_3
        nested_cell_0  = 'nested_cell_0'

        def nested_nested():
            return cell_2 + nested_cell_0 + cell_0

        nested_local_2 = '2'

    local_4 = 4

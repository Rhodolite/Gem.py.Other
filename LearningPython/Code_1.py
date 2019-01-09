#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Code_2')
def module():
    show_hidden = true


    @privileged
    def import__disassemble_code():
        Python_Disassemble = __import__('dis')

        disassemble_code = Python_Disassemble.disassemble

        return disassemble_code


    disassemble_code = import__disassemble_code()


    @privileged
    def import_code_sample():
        code_sample = __import__('Code_Sample').code_sample

        return code_sample


    code_sample = import_code_sample()

    Function = code_sample.__class__

    if is_python_2:
        python_function_code = Function.func_code.__get__
    else:
        python_function_code = Function.__code__.__get__


    @privileged
    def function_code(f):
        return python_function_code(f)


    code_sample__code = function_code(code_sample)

    Code = code_sample__code.__class__

    code_cell_variables      = Code.co_cellvars   .__get__
    code_constants           = Code.co_consts     .__get__
    code_filename            = Code.co_filename   .__get__
    code_first_line_number   = Code.co_firstlineno.__get__
    code_flags               = Code.co_flags      .__get__
    code_free_variables      = Code.co_freevars   .__get__
    code_line_number_table   = Code.co_lnotab     .__get__
    code_mostly_global_names = Code.co_names      .__get__
    code_name                = Code.co_name       .__get__
    code_stack_size          = Code.co_stacksize  .__get__
    code_total_arguments     = Code.co_argcount   .__get__
    code_total_locals        = Code.co_nlocals    .__get__
    code_variable_names      = Code.co_varnames   .__get__
    code_virtual_code        = Code.co_code       .__get__

    if is_python_3:
        code_total_keyword_arguments = Code.co_kwonlyargcount.__get__


    @share
    def show_code(name, code):
        header = 19


        def show(k, v):
            line('%*s:  %s', header, k, v)


        def show_portray(k, v):
            line('%*s:  %s', header, k, portray_2(v))


        def show_total(k, v):
            line('%*s:  total<%d>', header, k, length(v))


        def show_tuple(k, v, portray_element = true):
            show_portray(k, v)

            show_element = (show_portray   if portray_element else   show)

            for [i, v] in enumerate(v):
                show_element(arrange('[%d]', i), v)


        with indent(arrange('%s: %s', name, portray_code(code))):
            cell_variables  = code_cell_variables (code)
            total_arguments = code_total_arguments(code)
            total_locals    = code_total_locals   (code)
            variable_names  = code_variable_names (code)


            #
            #   name, filename, first line number
            #
            show_portray('name',              code_name             (code))
            show_portray('filename',          code_filename         (code))
            show_portray('first_line_number', code_first_line_number(code))


            #
            #   flags, stack size, line number table, virtual code
            #
            show_portray('flags',             code_flags            (code))
            show_portray('stack_size',        code_stack_size       (code))
            show_total  ('line_number_table', code_line_number_table(code))
            show_total  ('virtual_code',      code_virtual_code     (code))


            #
            #   total_arguments, total_locals, variable_names
            #
            assert total_locals == length(variable_names)

            show('arguments/locals', arrange('total_arguments<%d>; total_locals<%d>', total_arguments, total_locals))

            for i in iterate_range(total_locals):
                if i < total_arguments:
                    show(arrange('argument[%d]', i), variable_names[i])
                else:
                    show(arrange('local[%d]', i), variable_names[i])

            #
            #   total_keyword_arguments (python 3 only)
            #
            if is_python_3:
                show_portray('total_keyword_arguments', code_total_keyword_arguments(code))


            #
            #   cell_variables, names
            #
            show_tuple('cell_variables',      code_cell_variables     (code), portray_element = false)
            show_tuple('free_variables',      code_free_variables     (code), portray_element = false)
            show_tuple('mostly_global_names', code_mostly_global_names(code), portray_element = false)

            #
            #   constants
            #
            show_tuple('constants', code_constants(code))


    @share
    def show_code_1():
        blank()


        def show_nested(name, code):
            for [i, v] in enumerate(code_constants(code)):
                if type(v) is Code:
                    nested_name = arrange('%s.constants[%d]', name, i)

                    blank()
                    show_code(nested_name, v)
                    blank()
                    disassemble_code(v)

                    show_nested(nested_name, v)



        with indent('show_code_1:', prefix = 2):
            show_code('code_sample__code', code_sample__code)

            show_nested('code_sample__code', code_sample__code)

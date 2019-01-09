#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
@module('LearningPython.Ctypes_1')
def module():
    @privileged
    def import_Python_Ctypes():
        import  ctypes as Python_Ctypes

        return Python_Ctypes


    Python_Ctypes = import_Python_Ctypes()


    #
    #   C Types: Basic types
    #
    C_Boolean           = Python_Ctypes.c_bool
    C_Character         = Python_Ctypes.c_char
    C_Character_Pointer = Python_Ctypes.c_char_p
    C_Integer           = Python_Ctypes.c_int
    C_Long              = Python_Ctypes.c_long
    C_Size_Type         = Python_Ctypes.c_size_t
    C_Void_Pointer      = Python_Ctypes.c_void_p


    #
    #   C Types: Complex types
    #
    #       C_Base_Structure                - Base class of C Type structures
    #       create__C_Pointer               - Function that creates a C pointer.
    #       create__C_Python_API_Function   - Function that creates a C pointer to a Python API function written in C
    #
    C_Base_Structure              = Python_Ctypes.Structure
    create__C_Pointer             = Python_Ctypes.POINTER
    create__C_Python_API_Function = Python_Ctypes.PYFUNCTYPE


    #
    #   C functions
    #
    c_alignment   = Python_Ctypes.alignment
    c_cast        = Python_Ctypes.cast
    c_memory_move = Python_Ctypes.memmove
    c_memory_set  = Python_Ctypes.memset
    c_size_of     = Python_Ctypes.sizeof
    c_string_at   = Python_Ctypes.string_at


    header = 30

    def show_row(name, v):
        line('%*s: %s', header, name, portray_2(v))


    def show_C_Type(name, C_Type):
        line('%*s: %s', header, name, portray_2(C_Type))


    @share
    def show_ctypes_1():
        blank()

        with indent('show_ctypes_1:', prefix = 2):
            show_C_Type('C_Boolean',           C_Boolean)
            show_C_Type('C_Character',         C_Character)
            show_C_Type('C_Character_Pointer', C_Character_Pointer)
            show_C_Type('C_Integer',           C_Integer)
            show_C_Type('C_Long',              C_Long)
            show_C_Type('C_Size_Type',         C_Size_Type)
            show_C_Type('C_Void_Pointer',      C_Void_Pointer)

            blank()

            show_row('C_Base_Structure', C_Base_Structure)

            blank()

            show_row('create__C_Pointer', create__C_Pointer)
            show_row('create__C_Python_API_Function', create__C_Python_API_Function)

            blank()


            show_row('c_alignment',   c_alignment)
            show_row('c_cast',        c_cast)
            show_row('c_memory_move', c_memory_move)
            show_row('c_memory_set',  c_memory_set)
            show_row('c_size_of',     c_size_of)
            show_row('c_string_at',   c_string_at)

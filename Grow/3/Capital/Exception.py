#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#


from    Capital.Core                    import  creator


#
#   Import the version of "PREPARE_*Error" names we want to use.
#
from    Capital.Global                  import  capital_globals


exception_version = capital_globals.exception_version


if exception_version == 1:
    from    Capital.Private.Exception_V1        import  PREPARE_AttributeError
    from    Capital.Private.Exception_V1        import  PREPARE_ValueError
elif exception_version == 2:
    from    Capital.Private.Exception_V2        import  PREPARE_AttributeError
    from    Capital.Private.Exception_V2        import  PREPARE_ValueError
else:
    from    Capital.Core                import  FATAL

    FATAL('Capital/Exception.py: unknown exception version: {}', exception_version)

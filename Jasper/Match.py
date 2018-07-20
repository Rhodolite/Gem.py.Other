#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Jasper.Match')
def gem():
    require_gem('Gem.System')
    require_gem('Tremolite.Compile')


    from Gem import python_version
    from Tremolite import compile_regular_expression


    if python_version == '2.7.12 (default, Dec  4 2017, 14:50:18) \n[GCC 5.4.0 20160609]':
        C = ((
            #
            #<copyright>
            #   The following is generated from calling python's standard library:
            #
            #       1.  'sre_parse.py', function parse; and
            #       2.  'sre_compile.py', function '_code'
            #
            #   then saving the result; and is thus possibly:
            #
            #       Copyright (c) 1998-2001 by Secret Labs AB.  All rights reserved.
            #
            #       This version of the SRE library can be redistributed under CNRI's
            #       Python 1.6 license.  For any other use, please contact Secret Labs
            #       AB (info@pythonware.com).
            #
            #   (Currently the same copyright is used for both python 2.7 & 3.5 versions)
            #
            #   P.S.:  To make things simple, all *changes* to the original code below are dual licensed under
            #          both (1) the MIT License that the rest of Gem is licensed; and (2) under the exact same
            #          "CNRI's Python 1.6" license as the original code.
            #
            #   NOTE:  Dual copyright only applies to the changes, not to the original code which is obviously
            #          only licensed under the original license.
            #
            0,

            #
            #   r' {,7777777}(?P<operator>\.|import) {,7777777}'
            #
            ((
                17, 4, 0, 1, 15555560, 29, 6, 0, 7777777, 19, 32, 1, 21, 0, 7, 5, 19, 46, 18, 17, 15, 19, 105, 19, 109,
                19, 112, 19, 111, 19, 114, 19, 116, 18, 2, 0, 21, 1, 29, 6, 0, 7777777, 19, 32, 1, 1,
            )),
            ((none, 'operator')),

            #
            #   r' {,7777777}(?:(?P<keyword>import) {,7777777})?(?P<comment_newline>(?://(?P<comment>(?: {,7777777}[^\x00-\x1f ]{1,7777777}){,7777777}) {,7777777})?(?P<newline>\n\Z))?'
            #
            ((
                29, 6, 0, 7777777, 19, 32, 1, 28, 26, 0, 1, 21, 0, 19, 105, 19, 109, 19, 112, 19, 111, 19, 114, 19, 116,
                21, 1, 29, 6, 0, 7777777, 19, 32, 1, 22, 28, 59, 0, 1, 21, 2, 28, 42, 0, 1, 19, 47, 19, 47, 21, 4, 28,
                22, 0, 7777777, 29, 6, 0, 7777777, 19, 32, 1, 29, 11, 1, 7777777, 15, 6, 26, 27, 0, 32, 0, 1, 22, 21, 5,
                29, 6, 0, 7777777, 19, 32, 1, 22, 21, 6, 19, 10, 6, 7, 21, 7, 21, 3, 22, 1,
            )),
            ((none, 'keyword', 'comment_newline', 'comment', 'newline')),

            #
            #   '[A-Z_a-z][0-9A-Z_a-z]{,7777777}'
            #
            ((
                17, 14, 4, 1, 7777778, 10, 0, 0, 2281701374, 134217726, 0, 0, 0, 0, 0, 15, 11, 10, 0, 0, 2281701374,
                134217726, 0, 0, 0, 0, 0, 29, 16, 0, 7777777, 15, 11, 10, 0, 67043328, 2281701374, 134217726, 0, 0, 0,
                0, 0, 1, 1,
            )),
            #</copyright>
        )).__getitem__


        def M(regular_expression, code, groups = 0, flags = 0):
            return compile_regular_expression(regular_expression, C(code), C(groups), C(flags)).match


    else:
        require_gem('Tremolite.Parse')


        from Tremolite import parse_ascii_regular_expression


        def M(regular_expression, code, groups = 0, flags = 0):
            return compile_regular_expression(
                regular_expression,
                *parse_ascii_regular_expression(regular_expression)#,
            ).match


    #
    #   alphanumeric_or_underscore = ANY_OF('0-9', 'A-Z', '_', 'a-z')
    #
    #   as = 'as'
    #
    #   assign_operator = '='
    #
    #   colon = ':'
    #
    #   comma = ','
    #
    #   comment_newline = OPTIONAL('#' + ZERO_OR_MORE(DOT)) + LINEFEED + END_OF_PATTERN
    #
    #   compare_equal = '=='
    #
    #   dot = '.'
    #
    #   else = 'else'
    #
    #   equal_sign = '='
    #
    #   except = 'except'
    #
    #   finally = 'finally'
    #
    #   for = 'for'
    #
    #   greater_than_sign = '>'
    #
    #   if = 'if'
    #
    #   import = 'import'
    #
    #   in = 'in'
    #
    #   is = 'is'
    #
    #   left_brace = '{'
    #
    #   left_parenthesis = '('
    #
    #   left_square_bracket = '['
    #
    #   less_than_sign = '<'
    #
    #   letter_or_underscore = ANY_OF('A-Z', '_', 'a-z')
    #
    #   logical_and_sign = '&'
    #
    #   logical_or_sign = '|'
    #
    #   minus_sign = '-'
    #
    #   name = letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore)
    #
    #   not = 'not'
    #
    #   not_equal = '!='
    #
    #   number = '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9'))
    #
    #   or = 'or'
    #
    #   ow = ZERO_OR_MORE(' ')
    #
    #   ow_semicolon = ow + semicolon
    #
    #   percent_sign = '%'
    #
    #   period = '.'
    #
    #   plus_sign = '+'
    #
    #   print = 'print'
    #
    #   right_brace = '}'
    #
    #   right_parenthesis = ')'
    #
    #   right_square_bracket = ']'
    #
    #   semicolon = ';'
    #
    #   slash_sign = '/'
    #
    #   star = '*'
    #
    #   tilde = '~'
    #
    #   try = 'try'
    #
    #   w = ONE_OR_MORE(' ')
    #


    #
    #   import_pattern_match
    #
    #       ow + G('operator', period | 'import') + ow
    #
    import_pattern_match = M(
        r' {,7777777}(?P<operator>\.|import) {,7777777}',
        1,
        2,
    )

    #
    #   line_match
    #
    #       ow + OPTIONAL(G('keyword', import) + ow) + Q('comment_newline', OPTIONAL(slash_sign + slash_sign + G('comment', ZERO_OR_MORE(ow + ONE_OR_MORE(NOT_ANY_OF('\x00-\x1f', ' ')))) + ow) + G('newline', LINEFEED + END_OF_PATTERN))
    #
    line_match = M(
        r' {,7777777}(?:(?P<keyword>import) {,7777777})?(?P<comment_newline>(?://(?P<comment>(?: {,7777777}[^\x00-\x1f ]{1,7777777}){,7777777}) {,7777777})?(?P<newline>\n\Z))?',
        3,
        4,
    )

    #
    #   name_match
    #
    #       name
    #
    name_match = M(
        '[A-Z_a-z][0-9A-Z_a-z]{,7777777}',
        5,
    )


    export(
        'import_pattern_match',     import_pattern_match,
        'line_match',               line_match,
        'name_match',               name_match,
    )

PURPOSE

    This project is created to make code easy to read & learn.

    The idea is to start at 400 lines of code, and then through lesson grow the code.

    The hope is to have lots of people learn the code & work on improving it.


DEMO

    For a demo, do the following (type the lines with `$` -- but without the `$`):

        $ cat Vision.z
        $ python Vision.z
        % Z.py: Created Vision.py
        $ python Vision.py
        Programming is an art to communicate clearly and concisely to fellow programmers.
        $ cat Vision.py

CRYSTAL - Commnunity Resoures Yielding Simple Tutorial And Lessons.

    This project will create the Crystal parser.

    We will be defining the Crystal Language, over time.

    The Crystal Language can be translated to multiple other language (python, C, C++, Java, etc).


NO PARSER, INITIALLY.

    Instead of starting with a parser, we will use the Python parser, thus
    our initial code is super small (400 lines).

    The initial language (due to not having a parser) is a little awkward:

        1.  Being a little awkward, initially, is a good tradoff.

        2.  It makes the code super small & easy to learn.

        3.  Once we have developed a parser, the awkwardness will go away.


GENERATING MULTIPLE LANGAUGES.

    To make the project interesting, we will create a code generator that
    can take the same input and transform it to multiple langauges.

    ADVANTAGE:

        This makes it super simple to get new people to contribute!!

        Just ask them to read the current code & add a new language!


Z - THE AWKWARDNESS OF USING THE PYTHON PARSER, INITIALLY

    We will use `Z` in the python parser, to represent code that it to
    be transformed to another language.

    Code without a `Z` will be run during translation, but not be output
    to the other language.

    Actually, as this project grows, we will be able to do some really
    interesting code generation, by intermixing normal python code with
    code generation (using `Z`).


Vision.z - FIRST PROGRAM

    The first program is "Vision.z".  It has 3 lines of executable code:

        #
        #   Copyright (c) 2019 Joy Diamond.  All rights reserved.
        #
        import  Z


        Z.copyright
        Z.output('Programming is an art to communicate clearly and concisely to fellow programmers.')

    This means generate code that does two things:

        1.  Copy the copyright from "Vision.z" to the generated code.

        2.  Output a line of text, using the appropriate functions for the chosen language.

                A.  In python this would be `print`.

                B.  In C this would be `printf`

                C.  In C++ this would be `cout <<`

                D.  In Java this would be `System.out.Println`

                E.  In Bash this would be `echo`

        3.  We will create code generators, for all the languages listed above (and others), in
            future lessons.

        4.  For now we just generate python code.


SUMMARY OF HOW THE CODE GENERATOR WORKS:

    Basically a three step process:

        1.  Extract code generation from "Vision.Z"

        2.  Transform

        3.  Load to "Vision.py" (i.e.: create "Vision.py").

    Details:

        4.  The input file is "Vision.z"

        5.  It imports "Z.py" for its Z statements.

        6.  "Z/Extract.py" has functions that are called for each Z statement, and creates a Crystal parse tree
        
            6A. "Z/Crystal_ParseTree.py" is the Crystal Parse Tree.

        7.  "Z/Transform_Crystal_to_Python" is called to transform the Crystal Statments to Python Statements

            7A. "Z/Python_ParseTree.py" is the Python Parse Tree.

        8.  "Z/CodeGenerator_OnExit.py" creates "Vision.py" (when "Vision.x" exits).

DETAILS OF HOW THE CODE GENERATOR WORKS:

    Z.py - CODE GENERATOR.

        The code generator is in "Z.py". 

        Actually this is just a wrapper to input "Z/*.py".

        Read that file next :)

    Z/Core.py - Core Support code.

        Nothing much here -- just two support functions.

    Z/Crystal_ParseTree.py

        A parse tree of Crystal statements.

        This is what the Z statements in "Vision.z" create.

        IMPORTANT NOTE:
            Transform methods are *NOT* declared in this file -- but instead in "Z/Transform_Crystal_to_*.py"

            This is so that each language, can have it's own seperate file.

    Z/Extract.py

        This implements the Z command for "Vision.z".

        Basically each `Z` command generates a Crystal Statement to add to the Crystal Parse tree.

    Z/Python_ParseTree.py

        A parse tree of Python statements.

    Z/Transform_Crystal_to_Python
    
        Transform Crystal statements to Python statements.

        NOTE:
            This is unusual in that the methods are declared in THIS FILE instead of in "Z/Crystal_ParseTree.py"

            (See comment above under "Z/Crystal_ParseTree.py").

    Z/CodeGenerator_OnExit.py

        Output "Vision.py" when "Vision.z" exits.

        This is slightly unsual way of doing things, but it allows us to say:

            python Vision.x

        as a demo :) -- so it's worth the cost.

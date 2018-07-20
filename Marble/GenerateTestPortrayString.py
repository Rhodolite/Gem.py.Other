#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Marble.GenerateTestPortrayString')
def gem():
    require_gem('Marble.Core')
    require_gem('Topaz.PortrayString')


    from Topaz import portray_string_many


    def portray_java_string(s):
        f     = create_SimpleStringOutput()
        w     = f.write

        w('"')

        for c in s:
            a = lookup_ascii(c)

            if a is none:
                w(portray(c)[1:-1])
                continue

            if a.is_apostrophe:
                w("'")
                continue

            if a.is_quotation_mark:
                w('\\"')
                continue

            w(a.portray)

        w('"')

        return f.getvalue()

    @share
    def generate_test_portray_string():
        line('    static public final PortrayStringData_2[]   portray_string_many = new PortrayStringData_2[] {')

        prefix = ' ' * 8

        total_m1 = length(portray_string_many) - 1

        for [i, row] in enumerate(portray_string_many):
            used = length(row)

            if used == 2:
                [s, raw_expected] = row
            else:
                [s, raw_expected, python_expected] = row

            line("%sPortrayStringData.create_%d(", prefix, used);
            line("%s  %s,",   prefix, portray_java_string(s));

            if used == 2:
                line("%s  %s//,", prefix, portray_java_string(raw_expected));
            else:
                line("%s  %s,",   prefix, portray_java_string(raw_expected));
                line("%s  %s//,", prefix, portray_java_string(python_expected));

            if i == total_m1:
                line("%s)//,", prefix);
                break

            line("%s),", prefix);

        line('    };');

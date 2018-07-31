#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CodeGenerator.NestedConjure')
def module():
    require_module('CodeGenerator.Core')


    show_assert = 7


    class CommonKeyData(Object):
        __slots__ = ((
            'f',                        #   DelayedOuput
            'share',                    #   Boolean
            'show_assert',              #   Boolean
            'use_herd_estimate',        #   Boolean

            'total',                    #   Integer
            'chain',                    #   Tuple of String+
            'keys',                     #   String

            'coverage_name',            #   0 | String+
            'coverage_index',           #   Mutable Integer
        ))


        def __init__(t, f, share, show_assert, use_herd_estimate, total, chain, keys, coverage_name):
            t.f                 = f
            t.share             = share
            t.show_assert       = show_assert
            t.use_herd_estimate = use_herd_estimate

            t.total = total
            t.chain = chain
            t.keys  = keys

            t.coverage_name  = coverage_name
            t.coverage_index = 0


        def __repr__(t):
            return arrange('<CommonKeyData %s %s %s %d %s %s; %s %s>',
                           t.share,
                           t.show_assert,
                           t.use_herd_estimate,
                           t.total,
                           t.chain,
                           t.keys,
                           t.coverage_name, t.coverage_index)


        def cover(t):
            coverage_name = t.coverage_name

            if coverage_name is 0:
                return

            t.f.line('%s[%d] += 1', coverage_name, t.coverage_index)

            t.coverage_index += 1


    class KeyData(Object):
        __slots__ = ((
            'common',                   #   CommonKeyData
            'shift',                    #   Integer

            'b2',                       #   Zero | String+
            'b1',                       #   Zero | String+
            'p',                        #   String+
            'q',                        #   String+
            'r',                        #   Zero | String+
            's',                        #   Zero | String+

            'k0',                       #   Zero | String+
            'k1',                       #   String+
            'k2',                       #   String+
            'k3',                       #   Zero | String+
            'k4',                       #   Zero | String+
        ))


        def __repr__(t):
            return arrange('<KeyData %s %d; %s %s %s %s %s %s; %s %s %s %s %s>',
                           t.common, t.shift,
                           t.b2, t.b1, t.p, t.q, t.r, t.s,
                           t.k0, t.k1, t.k2, t.k3, t.k4)


        def __init__(t, common, shift, b2, b1, p, q, r, s, _, k0, k1, k2, k3, k4):
            assert _ is 0

            t.common = common
            t.shift  = shift

            t.b2 = b2
            t.b1 = b1
            t.p  = p
            t.q  = q
            t.r  = r
            t.s  = s
            t.k0 = k0
            t.k1 = k1
            t.k2 = k2
            t.k3 = k3
            t.k4 = k4


        def create_assert(t, v):
            common = t.common

            if common.show_assert:
                common.f.line('assert %s',
                              ' and '.join(arrange('(%s.%s is %s)', v, k, k)   for k in common.chain))


        def create_assert_r(t):
            common = t.common

            if common.show_assert:
                common.f.line('assert %s',
                              ' and '.join(arrange('(r.%s is %s)', k, k)   for k in common.chain))


        def create_r(t, r = 'r', extra = 0):
            common = t.common

            if extra is 0:
                common.f.line('%s = Meta(%s)', r, common.keys)
            else:
                common.f.line('%s = %s = Meta(%s)', extra, r, common.keys)

            t.create_assert(r)


        def remove_b_k2(t):
            if 0:
                k_sample = t.k_sample

                if k_sample is 0:
                    k_sample = t.k2
                elif type(k_sample) is not Tuple:
                    k_sample = ((k_sample, t.k2))
                else:
                    k_sample += ((t.k2,))

            return KeyData(
                      t.common, t.shift + 1,
                      t.b2, t.b1, t.p,  t.r,  t.s,  0,
                      0,    t.k0, t.k1, t.k3, t.k4, 0,
                   )


        def remove_p2_k0(t):
            return KeyData(
                      t.common, t.shift + 1,
                      t.b1, t.p,  t.q,  t.r,  t.s,  0,
                      0,    t.k1, t.k2, t.k3, t.k4, 0,
                   )


    def create_KeyData(common, k1, k2, k3 = 0, k4 = 0):
        return KeyData(
                   common, 0,
                   0, 0, 'p', 'q', (0   if k3 is 0 else   'r'), (0   if k4 is 0 else   's'),
                   0, 0, k1,  k2,  k3,                          k4,
               )


    def create_if_glimpse(t, skip = 1):
        common        = t.common
        coverage_name = common.coverage_name
        cover         = common.cover
        f             = common.f
        b1            = t.b1
        p             = t.p
        q             = t.q
        k1            = t.k1
        k2            = t.k2
        k3            = t.k3

        if k3 is 0:
            if coverage_name:
                with f.line('if %s.%s is %s:', p, k2, k2):
                    cover()
                    f.line('return %s', p)
            else:
                f.line('if %s.%s is %s: return %s', p, k2, k2, p)

            f.blank()
            return

        if b1 is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', b1)

        f.blank()

        with f.indent(arrange('if %s.%s is %s:', p, k2, k2)):
            cover()
            f.blank_suppress()
            create_if_glimpse(t.remove_b_k2(), skip = skip + 1)
            t.create_r(q)
            f.line('%s(%s, create_horde_2(%d, %s.%s, %s, %s, %s))', displace, k1, skip, p, k3, k3, p, q)
            f.line('return %s', q)

        f.blank()


    def create_test_herd_member(t, herd_k, herd_v, displace = 0, herd_k_next = 0, create_result = 0):
        common        = t.common
        coverage_name = common.coverage_name
        cover         = common.cover
        f             = common.f
        show_assert   = common.show_assert
        p             = t.p
        q             = t.q
        k2            = t.k2

        f.blank()

        if displace:
            pk = arrange('%s%s', p, herd_k)
            f.line('%s = %s.%s', pk, p, herd_k)
        else:
            pk = arrange('%s.%s', p, herd_k)

        if (coverage_name) or (show_assert):
            with f.indent(arrange('if %s is %s:', pk, k2)):
                cover()
                f.line('%s = %s.%s', q, p, herd_v)
                t.create_assert(q)
                f.line('return %s', q)
        else:
            f.line('if %s is %s: return %s.%s', pk, k2, p, herd_v)

        if displace:
            if create_result:
                f.blank()
                t.create_r(q)
                f.blank()
                with f.indent(arrange('if %s is absent:', pk)):
                    cover()
                    f.line('%s.%s = %s', p, herd_k, k2)
                    f.line('%s.%s = %s', p, herd_v, q)
                    f.line('return %s', q)
            else:
                with f.indent(arrange('if %s is absent:', pk)):
                    cover()
                    f.line('%s.%s = %s', p, herd_k, k2)

                    if herd_k_next is not 0:
                        f.line('%s.%s = absent', p, herd_k_next)

                    t.create_r(q, extra = arrange('%s.%s', p, herd_v))
                    f.line('return %s', q)
        else:
            assert create_result is 0

        f.blank()

        return pk


    def create_test_herd_glimpse(
            t, herd_k, herd_v,

            test_absent = 0, displace = 0, herd_k_next = 0, if_keyword = 'if', create_result = 0,
    ):
        common        = t.common
        coverage_name = common.coverage_name
        cover         = common.cover
        f             = common.f
        show_assert   = common.show_assert
        b1            = t.b1
        p             = t.p
        k1            = t.k1
        k3            = t.k3

        if test_absent:
            indent     = f.indent('else:')
            pk         = arrange('%s%s', b1, herd_k)
            if_keyword = 'if'
        else:
            indent = empty_context_manager
            pk     = arrange('%s.%s', b1, herd_k)

        with indent:
            if test_absent:
                cover()
                f.line('%s = %s.%s', pk, b1, herd_k)

            with f.indent(arrange('%s %s is %s:', if_keyword, pk, k1)):
                cover()
                f.line('%s = %s.%s', p, b1, herd_v)

                if k3 is 0:
                    create_if_glimpse(t)
                    f.blank_suppress()

                if displace is 0:
                    f.line('%sr = %s.displace_%s', b1, b1, herd_v)
                else:
                    f.line('%sr = %s', b1, displace)

            if test_absent:
                if create_result:
                    with f.indent('else:'):
                        cover()
                        assert herd_k_next is 0

                        t.create_r(p)

                        f.blank()

                        with f.indent(arrange('if %s is absent:', pk)):
                            cover()
                            f.line('%s.%s = %s', b1, herd_k, k1)
                            f.line('%s.%s = %s', b1, herd_v, p)
                            f.line('return %s', p)

                        f.blank()
                else:
                    with f.indent(arrange('elif %s is absent:', pk)):
                        cover()
                        f.line('%s.%s = %s', b1, herd_k, k1)

                        if herd_k_next is not 0:
                            f.line('%s.%s = absent', b1, herd_k_next)

                        t.create_r(p, extra = arrange('%s.%s', b1, herd_v))
                        f.line('return %s', p)

        return pk


    def create_assert_k_sample(t, v, k_sample):
        common = t.common

        f = common.f

        if type(k_sample) is Tuple:
            f.line('assert %s',
                   ' and '.join(arrange('(%s.sample().%s is %s)', v, k, k)   for k in k_sample))
            return

        f.line('assert %s.sample().%s is %s', v, k_sample, k_sample)


    def create_last(t, estimate = 0, k_sample = 0):
        common        = t.common
        coverage_name = common.coverage_name
        cover         = common.cover
        f             = common.f
        show_assert   = common.show_assert
        b1            = t.b1
        p             = t.p
        q             = t.q
        k1            = t.k1
        k2            = t.k2

        #if common.use_herd_estimate:    k_sample = 'FAKE'

        if t.b1 is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', b1)

        if estimate is not 0:
            if common.total is 2:
                assert k_sample is 0

                possible_herd  = 7
                possible_horde = 0

                f.line('#create_last: herd only')
            else:
                possible_herd  = (k_sample is 0)
                possible_horde = 7

                if possible_herd:
                    f.line('#create_last: herd or horde')
                else:
                    f.line('#create_last: horde only')

            if (coverage_name) or (show_assert):
                with f.indent(arrange('if %s is 8:', estimate)):
                    cover()

                    f.line('%s = map__lookup(%s, %s)', q, p, k2)
                    with f.indent(arrange('if %s is not none:', q)):
                        cover()
                        t.create_assert(q)
                        f.line('return %s', q)
                    cover()

                    f.blank()

                    t.create_r(q)
                    f.line('map__store(%s, %s, %s)', p, k2, q)
                    f.line('return %s', q)
                    f.blank()
            else:
                f.line('if %s is 8: return (map__lookup(%s, %s)) or (map__provide(%s, %s, Meta(%s)))',
                       estimate, p, k2, p, k2, common.keys)

            if not possible_herd:
                f.line('assert %s is 3', estimate)
                f.blank()

            aa = create_test_herd_member(t, 'a', 'v')

            if not show_assert:
                f.blank_suppress()

            ab = create_test_herd_member(t, 'b', 'w')

            if possible_herd:
                if not show_assert:
                    f.blank_suppress()

                with f.indent(arrange('if %s is 2:', estimate)):
                    cover()

                    herd = arrange('create_herd_3(%s, %s, %s, %s.v, %s.w, %s)', aa, ab, k2, p, p, q)

                    t.create_r(q)

                    if b1 is 0:
                        f.line('%s(%s, %s)', displace, k1, herd)
                    else:
                        with f.indent(arrange('if %sh is 8:', b1)):
                            cover()
                            f.line('map__store(%s, %s, %s)', b1, k1, herd)
                        with f.indent('else:'):
                            cover()
                            f.line('%sr(%s, %s)', b1, b1, herd)

                    f.line('return %s', q)

                ac = create_test_herd_member(t, 'c', 'x', (3   if possible_horde else   0))

                if not show_assert:
                    f.blank_suppress()

                with f.indent(arrange('if %s is 3:', estimate)):
                    cover()

                    herd = arrange('create_herd_4(%s, %s, %s, %s, %s.v, %s.w, %s.x, %s)',
                                   aa, ab, ac, k2, p, p, p, q)

                    t.create_r(q)

                    if b1 is 0:
                        f.line('%s(%s, %s)', displace, k1, herd)
                    else:
                        with f.indent(arrange('if %sh is 8:', b1)):
                            cover()
                            f.line('map__store(%s, %s, %s)', b1, k1, herd)
                        with f.indent('else:'):
                            cover()
                            f.line('%sr(%s, %s)', b1, b1, herd)

                    f.line('return %s', q)

                f.blank()

                f.line('assert %s is 7', estimate)

                ad  = create_test_herd_member(t, 'd',  'y',  4)
                ae  = create_test_herd_member(t, 'e',  'z',  5, herd_k_next = 'e6')
                ae6 = create_test_herd_member(t, 'e6', 'z6', 6, herd_k_next = 'e7')
                ae7 = create_test_herd_member(t, 'e7', 'z7', 7, create_result = 7)

                f.blank()


                def create_herd_many__from__herd_7():
                    with f.indent('create_herd_many(', '),'):
                        f.line('%s, %s, %s, %s, %s, %s, %s, %s,', aa,  ab, ac, ad, ae, ae6, ae7, k2)
                        f.line('%s.v, %s.w, %s.x, %s.y, %s.z, %s.z6, %s.z7, %s,', p, p, p, p, p, p, p, q)


                if b1 is 0:
                    with f.indent(
                            arrange('%s(', displace), arrange('%*s)', length(displace),  ' '), length(displace) + 4
                    ):
                        f.line('%s,', k1)
                        create_herd_many__from__herd_7()
                else:
                    with f.indent(arrange('if %sh is 8:', b1)):
                        cover()
                        with f.indent('map__store(', ')'):
                            f.line('%s,', b1)
                            f.line('%s,', k1)
                            create_herd_many__from__herd_7()
                    with f.indent('else:'):
                        cover()
                        with f.indent(arrange('%sr(', b1), ')'):
                            f.line('%s,', b1)
                            create_herd_many__from__herd_7()

                f.blank()

                f.line('return %s', q)
                return

            skip = (length(k_sample)   if type(k_sample) is Tuple else   1)

            ac = create_test_herd_member(t, 'c', 'x', 3, create_result = 7)

            f.blank()

            f.line('h = create_horde_many(%d, %s, %s, %s, %s, %s.v, %s.w, %s.x, %s)',
                   skip, aa, ab, ac, k2, p, p, p, q)
            create_assert_k_sample(t, 'h', k_sample)
            f.line('%s(%s, h)', displace, k1)
            f.line('return %s', q)
            return

        f.line('%s = %s.glimpse(%s)', q, p, k2)
        if (coverage_name) or (show_assert):
            with f.indent(arrange('if %s is not none:', q)):
                cover()
                t.create_assert(q)
                f.line('return %s', q)
            cover()
        else:
            f.line('if %s is not none: return %s', q, q)

        f.blank()
        t.create_r(q)

        a_ = arrange('%s_', p)

        f.line('%s = %s.insert(%s, %s)', a_, p, k2, q)

        if k_sample is 0:
            if coverage_name:
                with f.indent(arrange('if %s is not %s:', p, a_)):
                    cover()
                    f.line('%s(%s, %s)', displace, k1, a_)
            else:
                f.line('if %s is not %s: %s(%s, %s)', p, a_, displace, k1, a_)
            cover()

            f.blank()
        else:
            with f.indent(arrange('if %s is not %s:', p, a_)):
                cover()
                create_assert_k_sample(t, a_, k_sample)
                f.line('%s(%s, %s)', displace, k1, a_)

        f.line('return %s', q)


    def create_next(t, p_estimate = 0, k_sample = 0):
        common        = t.common
        coverage_name = common.coverage_name
        cover         = common.cover
        show_assert   = common.show_assert
        f             = common.f
        shift         = t.shift
        b2            = t.b2
        b1            = t.b1
        p             = t.p
        q             = t.q
        k0            = t.k0
        k1            = t.k1
        k2            = t.k2
        k3            = t.k3
        k4            = t.k4

        #f.line('#create_next(%s, %s, %s)', t, p_estimate, k_sample)

        if b1 is 0:
            assert p_estimate is 0
            assert k0         is 0

            f.line('%s = lookup(%s)', p, k1)

            if (coverage_name) or (show_assert):
                with f.indent(arrange('if %s is none:', p)):
                    cover()
                    t.create_r(q)
                    f.line('return provide(%s, %s)', k1, q)
            else:
                f.line('if %s is none: return provide(%s, Meta(%s))', p, k1, common.keys)

            f.blank_suppress()

            if k3 is not 0:
                create_if_glimpse(t)
        elif p_estimate is 0:
            f.line('%s = %s.glimpse(%s, absent)', p, b1, k1)
            create_if_glimpse(t)
        else:
            possible_herd  = (shift is 1) and (k_sample is 0)
            possible_horde = (k_sample is not 0) or (k3 is not 0)

            assert (possible_herd) or (possible_horde)

            if possible_herd:
                if possible_horde:
                    f.line('#create_next: shift: %d; herd or horde', shift)
                else:
                    f.line('#create_next: shift: %d; herd only', shift)
            else:
                assert possible_horde

                f.line('#create_next: shift: %d; horde only', shift)

            with f.indent(arrange('if %s is 8:', p_estimate)):
                cover()
                f.line('%s = map__lookup(%s, %s)', p, b1, k1)

                if (coverage_name) or (show_assert):
                    with f.indent(arrange('if %s is none:', p)):
                        cover()
                        t.create_r(q)
                        f.line('return map__provide(%s, %s, %s)', b1, k1, q)
                else:
                    f.line('if %s is none: return map__provide(%s, %s, Meta(%s))', p, b1, k1, common.keys)

                if k3 is 0:
                    create_if_glimpse(t)
                    f.blank_suppress()

            if possible_herd:
                indent     = empty_context_manager
                if_keyword = 'elif'
            else:
                indent     = f.indent('else:')
                if_keyword = 'if'

            with indent:
                f.blank_suppress()

                if not possible_herd:
                    f.line('assert %s is 3', p_estimate)
                    f.blank()

                pa = create_test_herd_glimpse(t, 'a', 'v', if_keyword = if_keyword)
                pb = create_test_herd_glimpse(t, 'b', 'w', if_keyword = 'elif')

                if possible_herd:
                    f.blank_suppress()
                    with f.indent(arrange('elif %s is 2:', p_estimate)):
                        cover()

                        if b2 is 0:
                            displace = 'store'
                        else:
                            displace = arrange('%s.displace', b2)

                        t.create_r(p)
                        f.line('%s(%s, create_herd_3(%s.a, %s.b, %s, %s.v, %s.w, %s))', displace, k0, b1, b1, k1, b1, b1, p)
                        f.line('return %s', p)

                    ac = create_test_herd_glimpse(
                             t, 'c', 'x',

                             (3   if possible_horde else   0),
                             (0   if possible_horde else   arrange('%s.displace_x', b1)),
                             if_keyword = 'elif',
                         )

                    if possible_horde:
                        indent     = f.indent('else:')
                        if_keyword = 'if'
                    else:
                        indent     = empty_context_manager
                        if_keyword = 'elif'

                    with f.indent(arrange('%s %s is 3:', if_keyword, p_estimate)):
                        cover()

                        if b2 is 0:
                            displace = 'store'
                        else:
                            displace = arrange('%s.displace', b2)

                        t.create_r(p)
                        f.line('%s(%s, create_herd_4(%s.a, %s.b, %s.c, %s, %s.v, %s.w, %s.x, %s))',
                                displace, k0, b1, b1, b1, k1, b1, b1, b1, p)
                        f.line('return %s', p)


                    with indent:
                        with f.indent('else:'):
                            cover()

                            f.line('assert %s is 7', p_estimate)

                            ad = create_test_herd_glimpse(t, 'd', 'y', displace = 'displace_4y')

                            ae = create_test_herd_glimpse(
                                     t, 'e',  'z',  5,

                                     displace = 'displace_4z', herd_k_next = 'e6',
                                 )

                            with f.indent():
                                ae6 = create_test_herd_glimpse(
                                          t, 'e6', 'z6', 6,

                                          displace = 'displace_4z6', herd_k_next = 'e7',
                                      )

                                with f.indent():
                                    ae7 = create_test_herd_glimpse(
                                              t, 'e7', 'z7', 7,

                                              displace = 'displace_4z7', create_result = 7,
                                          )

                                    with f.indent(prefix = 8):
                                        if b2 is 0:
                                            displace = 'store'
                                        else:
                                            displace = arrange('%s.displace', b2)

                                        with f.indent(arrange('%s(', displace), arrange('%*s)', length(displace),  ' '), length(displace) + 4):
                                            f.line('%s,', k0)
                                            with f.indent('create_herd_many(', ')'):
                                                f.line('%s.a, %s.b, %s.c, %s, %s, %s, %s, %s,',
                                                        b1, b1, b1, ad, ae, ae6, ae7, k1)
                                                f.line('%s.v, %s.w, %s.x, %s.y, %s.z, %s.z6, %s.z7, %s,',
                                                        b1, b1, b1, b1, b1, b1, b1, p)

                                        f.blank()

                                        f.line('return %s', p)

                else:
                    with f.indent('else:'):
                        cover()

                        f.line('%s  = %s.glimpse(%s, absent)', p, b1, k1)
                        f.line('%sr = 0', p)

                    f.line('INCOMPLETE')

            f.blank()

            if k3 is not 0:
                create_if_glimpse(t)

        f.blank()

        if common.use_herd_estimate:
            estimate = arrange('%sh', p)

            f.line('%s = %s.herd_estimate', estimate, p)
            if_not_herd = arrange('if %s is 0:', estimate)
        else:
            estimate    = 0
            if_not_herd = arrange('if not %s.is_herd:', p)

        f.blank()

        with f.indent(if_not_herd):
            cover()

            if coverage_name:
                with f.indent(arrange('if %s.%s is %s:', p, k2, k2)):
                    cover()
                    f.line('return %s', p)
            else:
                f.line('if %s.%s is %s: return %s', p, k2, k2, p)

            cover()

            t.create_r(q)

            if b1 is 0:
                assert k0 is 0

                f.line('herd = create_herd_2(%s.%s, %s, %s, %s)', p, k2, k2, p, q)
                f.line('store(%s, herd)', k1)
                f.line('return %s', q)
            elif p_estimate is 0:
                with f.indent(arrange('if %s is absent:', p)):
                    cover()

                    if b2 is 0:
                        displace = 'store'
                    else:
                        displace = arrange('%s.displace', b2)

                    b1_ = arrange('%s_', b1)
                    f.line('%s = %s.insert(%s, %s)', b1_, b1, k1, q)

                    if k_sample is 0:
                        if coverage_name:
                            with f.indent('if %s is not %s', b1, b1_):
                                cover()
                                f.line('%s(%s, %s)', displace, k0, b1_)
                        else:
                            f.line('if %s is not %s: %s(%s, %s)', b1, b1_, displace, k0, b1_)
                    else:
                        with f.indent(arrange('if %s is not %s:', b1, b1_)):
                            cover()
                            create_assert_k_sample(t, b1_, k_sample)
                            f.line('%s(%s, %s)', displace, k0, b1_)

                    f.line('return %s', q)

                f.blank()
                f.line('herd = create_herd_2(%s.%s, %s, %s, %s)', p, k2, k2, p, q)
                f.line('%s.displace(%s, herd)', b1, k1)
                f.line('return %s', q)
            else:
                f.line('herd = create_herd_2(%s.%s, %s, %s, %s)', p, k2, k2, p, q)

                f.blank()

                if coverage_name:
                    with f.indent('if %s is 8', p_estimate):
                        cover()
                        f.line('map__store(%s, %s, herd)', b1, k1)
                    with f.indent('else:'):
                        cover()
                        f.line('%sr(%s, herd)', b1, b1)
                else:
                    f.line('if %s is 8: map__store(%s, %s, herd)', p_estimate, b1, k1)
                    f.line('else:       %sr(%s, herd)', b1, b1)

                f.blank()

                f.line('return %s', q)
        cover()

        f.blank()

        if k3 is 0:
            create_last(t, estimate)
            return

        with f.indent(arrange('if %s.skip is 0:', p)):
            cover()
            create_next(t.remove_p2_k0(), estimate)

        f.blank()

        cover()

        f.blank()

        t2 = t.remove_b_k2()

        if k4 is 0:
            f.line('assert %s.skip is 1', p)
            create_sample(t, 0)
            create_last(t2, estimate, k_sample = k2)
            return

        create_sample(t, 1)

        with f.indent(arrange('if %s.skip is 1:', p)):
            cover()
            create_next(t2.remove_p2_k0(), k_sample = k2)

        f.blank()
        f.line('assert %s.skip is 2', p)

        create_sample(t2, 2, skip = 2)
        create_last(t2.remove_b_k2(), estimate, k_sample = ((k2,k3)) )


    def create_sample(t, multiple, skip = 1):
        common = t.common

        f  = common.f
        b1 = t.b1
        p  = t.p
        k1 = t.k1
        k2 = t.k2

        if b1 is 0:
            displace = 'store'
        else:
            displace = arrange('%s.displace', b1)

        f.blank()

        if multiple is 0:
            f.line('%s_%s = %s.sample().%s', p, k2, p, k2)
        elif multiple is 1:
            f.line('%s_sample = %s.sample()', p, p)
            f.line('%s_%s     = %s_sample.%s', p, k2, p, k2)
        else:
            assert multiple is 2
            f.line('%s_%s = %s_sample.%s', p, k2, p, k2)

        with f.indent(arrange('if %s_%s is not %s:', p, k2, k2)):
            t.create_r()
            if skip is 1:
                f.line('%s(%s, create_herd_2(%s_%s, %s, %s.remove_skip(), r))', displace, k1, p, k2, k2, p)
            else:
                f.line('%s(%s, create_horde_2(%d, %s_%s, %s, %s.remove_skip(%d), r))',
                       displace, k1, skip - 1, p, k2, k2, p, skip)

            f.line('return r')

        f.blank()


    def create_conjure(
            f, prefix, suffix, k1, k2, k3 = 0, k4 = 0,

            coverage          = 0,
            share             = 0,
            show_assert       = 0,
            use_herd_estimate = 0,
    ):
        if k3 is 0:
            total = 2
            chain = ((k1, k2))
            keys  = 'k1, k2'
        elif k4 is 0:
            total = 3
            chain = ((k1, k2, k3))
            keys  = 'k1, k2, k3'
        else:
            total = 4
            chain = ((k1, k2, k3, k4))
            keys  = 'k1, k2, k3, k4'

        coverage_name = (0   if coverage is 0 else   arrange('coverage_%s', suffix))

        common = CommonKeyData(
                         f, share, show_assert, use_herd_estimate, total, chain, keys, coverage_name,
                     )

        t    = create_KeyData(common, k1, k2, k3, k4)
        name = arrange('%s_%s', prefix, suffix)

        f.blank2()

        f.line( ('@share'   if share is 7 else   '@export') )
        with f.indent(arrange('def produce_%s(', name), '):', 8):
            f.line('name, Meta, cache,')
            f.blank()
            f.line('lookup  = absent,')
            f.line('provide = absent,')
            f.line('store   = absent,')
        with f.indent():
            f.line('lookup  = cache.get')
            f.line('provide = cache.setdefault')
            f.line('store   = cache.__setitem__',)
            f.blank2()
            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(%s):', name, t.common.keys)):
                common.cover()
                create_next(t)

            f.blank2()

            f.line('return %s', name)

        f.blank2()

        if coverage:
            f.line('%s = [0] * %d', coverage_name, common.coverage_index)

            f.blank2()

            with f.indent('export(', ')'):
                f.line('%r, %s', coverage_name, coverage_name)

            f.blank2()


    def create_nested_conjure__X(
            year, author, prefix, module_name, which,

            blanks            = 0,
            coverage          = 0,
            share             = 0,
            show              = 0,
            show_assert       = show_assert,
            use_herd_estimate = 0,
    ):
        if type(which) is not Tuple:
            which = ((which,))

        path = path_join(module_path[0], '../UnitTest', arrange('%s.gpy', module_name.replace('.', '/')))

        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@module(%r)', module_name)

            create_horde_flags = [0]


            def process(
                    test, suffix, k1, k2, k3 = 0, k4 = 0,

                    use_herd_estimate = use_herd_estimate,
            ):
                if test in which:
                    if loop == 1:
                        if k3 is not 0:
                            create_horde_flags[0] = 7

                    if loop == 2:
                        create_conjure(
                            f, prefix, suffix, k1, k2, k3, k4,

                            coverage          = coverage,
                            share             = share,
                            show_assert       = show_assert,
                            use_herd_estimate = use_herd_estimate,
                        )
                elif blanks:
                    if loop == 1:
                        produce_zero.append(arrange('produce_%s_%s', prefix, suffix))


            with f.indent('def module():'):
                f.blank_suppress()

                create_herd_many = 0
                import_list      = ['create_herd_3', 'create_herd_4', 'create_herd_many']
                produce_zero     = []

                for loop in [1, 2]:
                    if loop == 2:
                        if create_horde_flags[0]:
                            import_list.append('create_horde_2')
                            import_list.append('create_horde_many')
                            import_list.append('displace_4y')
                            import_list.append('displace_4z')
                            import_list.append('displace_4z6')
                            import_list.append('displace_4z7')

                        f.line('from Capital import %s', ', '.join(import_list))

                        f.blank2()

                        f.line('map__lookup  = Map.get')
                        f.line('map__provide = Map.setdefault')
                        f.line('map__store   = Map.__setitem__')

                        f.blank2()

                        if produce_zero:
                            produce_zero.sort()

                            for name in produce_zero:
                                f.line('%-36s = 0', name)

                            f.blank2()

                            with f.indent('share(', ')'):
                                for name in produce_zero:
                                    f.line('%-40s%s,', arrange('%r,', name), name)

                    process(21,   'dual__21',        'k2', 'k1')
                    process(2 ,   'dual',            'k1', 'k2')
                    process(312,  'triple__312',     'k3', 'k1', 'k2')
                    process(3,    'triple',          'k1', 'k2', 'k3',        )#use_herd_estimate = 0)
                    process(4,    'quadruple',       'k1', 'k2', 'k3', 'k4')
                    process(4123, 'quadruple__4123', 'k4', 'k1', 'k2', 'k3')


            data = f.finish()

        if show is 3:
            partial(''.join(data.splitlines(true)[42:102]))
        elif show is 4:
            partial(''.join(data.splitlines(true)[100:170]))
        elif show is 5:
            partial(''.join(data.splitlines(true)[140:210]))
        elif show is 7:
            partial(data)


    @export
    def create_nested_conjure(year, author):
        create_nested_conjure__X(
            year, author, 'NEW_conjure', 'UnitTest.GeneratedNew',

            which  = 2,
            #which  = ((2, 21, 3)),

            coverage = 7,
            share    = 7,
            show     = 0,
            blanks   = 7,
        )

        if 7 is 7:
            if 2:
                create_nested_conjure__X(
                    year, author, 'simplified_conjure', 'UnitTest.GeneratedConjureDual',

                    #which             = 2,
                    which             = ((21, 2)),
                    #coverage          = 7,
                    share             = 7,
                    use_herd_estimate = 7,
                )

            if 0:
                create_nested_conjure__X(
                    year, author, 'simplified_conjure', 'UnitTest.GeneratedConjureTriple',

                    which = ((312, 3)),
                    #which             = 3,
                    share             = 7,
                    use_herd_estimate = 7,
                )

            if 0:
                create_nested_conjure__X(
                    year, author, 'simplified_conjure', 'UnitTest.GeneratedConjureQuadruple',

                    which = ((4123, 4)),
                    #which = 4,
                    share = 7,
                )

            if 0:
                create_nested_conjure__X(
                    year, author, 'conjure', 'Capital.GeneratedConjureQuadruple',

                    which = 4123,
                )

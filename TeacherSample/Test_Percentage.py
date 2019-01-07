#
#   Copyright (c) 2019 Joy Diamond.  All rights reserved.
#
from    Percentage          import  percentage__with_considering_0_of_0_as_100
from    TestingFramework    import  cleanup_after_test


@cleanup_after_test
def test_percentage():
    assert percentage__with_considering_0_of_0_as_100(0, 0) == 100

    assert percentage__with_considering_0_of_0_as_100(0, 3) == 0
    assert percentage__with_considering_0_of_0_as_100(1, 3) == 33       #   Rounding down
    assert percentage__with_considering_0_of_0_as_100(2, 3) == 67       #   Rounding up
    assert percentage__with_considering_0_of_0_as_100(3, 3) == 100

    assert percentage__with_considering_0_of_0_as_100(0, 7) == 0
    assert percentage__with_considering_0_of_0_as_100(1, 7) == 14       #   Rounding down
    assert percentage__with_considering_0_of_0_as_100(2, 7) == 29       #   Rounding up
    assert percentage__with_considering_0_of_0_as_100(3, 7) == 43       #   Rounding up
    assert percentage__with_considering_0_of_0_as_100(4, 7) == 57       #   Rounding down
    assert percentage__with_considering_0_of_0_as_100(5, 7) == 71       #   Rounding down
    assert percentage__with_considering_0_of_0_as_100(6, 7) == 86       #   Rounding up
    assert percentage__with_considering_0_of_0_as_100(7, 7) == 100

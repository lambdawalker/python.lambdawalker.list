def test_smoke():
    from lambdawalker.list.flatten import flatten
    assert flatten([[1, 2], [3]]) == [1, 2, 3]
    print("list OK")

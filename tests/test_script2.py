import pytest
import mypackage.script1 as script1
import mypackage.script2 as script2

def test_method():
    bar = script1.Bar()
    bar.print()
    assert True
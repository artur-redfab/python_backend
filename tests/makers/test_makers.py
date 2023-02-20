import pytest
from components.makers.crud import get_maker_by_id
def test_get_maker_by_id():
assert get_maker_by_id(1) == {""}

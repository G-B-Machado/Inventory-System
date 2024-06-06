import pytest
from inventory import add_product, modify_product, delete_product, read_inventory

def test_add_product():
    add_product('P3', 'Product3', 8, 2, 10, 150, 'Supplier3', 'Manufacturer3', True)
    df = read_inventory(True)
    assert 'P3' in df['id'].astype(str).values

def test_modify_product():
    modify_product('P1','NewProduct1', 20, 150, True)
    df = read_inventory(True)
    assert 'NewProduct1' in df['name'].astype(str).values
    assert '20' in df['quantity'].astype(str).values
    assert '150' in df['price'].astype(str).values

def test_delete_product():
    delete_product('P2', True)
    df = read_inventory(True)
    assert not 'P2' in df['id'].astype(str).values

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
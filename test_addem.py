from addem import add
# use python -m pytest
def test_subtraction():
    assert 5 - 3 == 2
  
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8031")
    assert set1 == set2

def test_add():
    result = add(3, 5)
    assert result == 8
    # def test_api_returns_200(url):
#     response = requests.get(url)
#     assert response.status_code == 200, f"API {url} did not return 200 OK"
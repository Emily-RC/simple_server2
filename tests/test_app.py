def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

# def test_get_countries(web_client):
#     response = web_client.get("/countries")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "I have been to Sweden!"

def test_assertion_fail():
    assert 2 + 2 == 4
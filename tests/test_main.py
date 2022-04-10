def test_index(client):
    """Ensure index returns a 200 OK"""

    # get index
    res = client.get("/")

    # assert
    assert res.status_code == 200

def test_root_redirect_location_header(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in {301, 302, 303, 307, 308}
    assert response.headers.get("location") == expected_location


def test_root_redirect_resolves_to_static_page(client):
    # Arrange
    redirect_path = "/"

    # Act
    response = client.get(redirect_path, follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")

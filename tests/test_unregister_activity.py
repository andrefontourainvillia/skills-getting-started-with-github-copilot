from src.app import activities


def test_unregister_participant_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_participant_activity_not_found(client):
    # Arrange
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Nonexistent%20Activity/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_participant_not_signed_up(client):
    # Arrange
    email = "not-signed-up@mergington.edu"

    # Act
    response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not signed up"}


def test_unregister_participant_second_attempt_returns_not_found(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    first_response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": email}
    )
    second_response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": email}
    )

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 404
    assert second_response.json() == {"detail": "Student not signed up"}

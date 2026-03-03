import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)


def test_unregister_participant_success():
    response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_participant_activity_not_found():
    response = client.delete(
        "/activities/Nonexistent%20Activity/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_participant_not_signed_up():
    response = client.delete(
        "/activities/Chess%20Club/signup", params={"email": "not-signed-up@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not signed up"}

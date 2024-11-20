"""Summary
In this snippet, we are creating a test script that will test all the API endpoints in the application.
The script uses the requests library to send HTTP requests to the API endpoints and checks the response
status code and content.
"""


import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("LOCAL_BASE_URL")


def test_google_sheets_input():
    """
    Test the /google-sheets/input endpoint.
    """
    payload = {"keyword": "jeans", "website": "asos"}
    response = requests.post(f"{BASE_URL}/google-sheets/input", json=payload)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /google-sheets/input PASSED")


def test_google_sheets_input_no_website():
    """
    Test the /google-sheets/input endpoint without a website parameter.
    """
    payload = {"keyword": "jeans"}
    response = requests.post(f"{BASE_URL}/google-sheets/input", json=payload)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /google-sheets/input PASSED")


def test_google_sheets_input_no_keyword():
    """
    Test the /google-sheets/input endpoint without a keyword parameter.
    """
    payload = {"website": "asos"}
    response = requests.post(f"{BASE_URL}/google-sheets/input", json=payload)

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /google-sheets/input PASSED")


def test_alibaba_search():
    """
    Test the /alibaba/search endpoint.
    """
    payload = {"keyword": "MacBook Pro"}
    response = requests.post(f"{BASE_URL}/alibaba/search", json=payload)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /alibaba/search PASSED")


def test_asos_search():
    """
    Test the /asos/search endpoint.
    """
    payload = {"keyword": "jeans"}
    response = requests.post(f"{BASE_URL}/asos/search", json=payload)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /asos/search PASSED")


def test_youtube_search():
    """
    Test the /youtube/search endpoint.
    """
    params = {"keyword": "dogs"}
    response = requests.post(f"{BASE_URL}/youtube/search", params=params)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "message" in response.json(), "Response should contain 'message'"
    print("Test /youtube/search PASSED")


def execute_test(test_function, endpoint):
    """
    Helper function to execute a test function and record its result.
    """
    try:
        test_function()
        return {"endpoint": endpoint, "status": "PASSED"}
    except AssertionError as e:
        return {"endpoint": endpoint, "status": f"FAILED: {e}"}


def run_all_tests():
    """
    Run all API tests and return a summary of results.
    """
    tests = [
        {"function": test_google_sheets_input, "endpoint": "/google-sheets/input"},
        {"function": test_google_sheets_input_no_website, "endpoint": "/google-sheets/input"},
        {"function": test_google_sheets_input_no_keyword, "endpoint": "/google-sheets/input"},
        {"function": test_alibaba_search, "endpoint": "/alibaba/search"},
        {"function": test_asos_search, "endpoint": "/asos/search"},
        {"function": test_youtube_search, "endpoint": "/youtube/search"},
    ]

    test_results = [execute_test(test["function"], test["endpoint"]) for test in tests]

    print("\nTest Results Summary:")
    for result in test_results:
        print(f"{result['endpoint']}: {result['status']}")


if __name__ == "__main__":
    print("Running API tests...")
    run_all_tests()
    print("\nAPI tests complete.")

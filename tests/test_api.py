
from fastapi.testclient import TestClient
from src.app.main import app, model

client = TestClient(app)


# Test 1: Health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Test 2: Prediction endpoint
def test_predict():
    customer = {
        "tenure_months": 5,
        "monthly_charges": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200
    assert "churn_probability" in response.json()


# Test 3: Missing required field
def test_missing_field():
    response = client.post(
        "/predict",
        json={"tenure_months": 5}
    )

    assert response.status_code == 422


# Test 4: Invalid input
def test_invalid_input():
    customer = {
        "tenure_months": "wrong",
        "monthly_charges": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


# Test 5: Probability range
def test_probability_range():
    customer = {
        "tenure_months": 5,
        "monthly_charges": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response = client.post("/predict", json=customer)
    probability = response.json()["churn_probability"]

    assert 0 <= probability <= 1


# Test 6: Model loads successfully
def test_model_loads():
    assert model is not None


# Test 7: Deterministic prediction
def test_deterministic_prediction():
    customer = {
        "tenure_months": 5,
        "monthly_charges": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response1 = client.post("/predict", json=customer)
    response2 = client.post("/predict", json=customer)

    assert response1.json() == response2.json()

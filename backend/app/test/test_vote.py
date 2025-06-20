import requests

def test_inference():
    url = "http://localhost:8000/inference/"
    data = {"prompt": "Türkiye'nin başkenti neresidir?"}
    params = {"backend": "gpt4all"}
    r = requests.post(url, params=params, json=data)
    assert r.status_code == 200
    print("Inference sonucu:", r.json())

def test_vote():
    url = "http://localhost:8000/inference/vote"
    data = {"prompt": "Türkiye'nin başkenti neresidir?"}
    r = requests.post(url, json=data)
    assert r.status_code == 200
    result = r.json()
    print("Voting sonucu:", result)
    assert "consensus_answer" in result
    assert "confidence" in result

if __name__ == "__main__":
    test_inference()
    test_vote()
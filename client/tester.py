import requests

URL_Get = "http://127.0.0.1:8000/leads/"
if __name__ == "__main__":
    values = {"first_name": "James", "last_name": "Lee", "email": "cookies@gmail.com", "resume": "I Love Hotdogs"}
    response = requests.post(URL_Get, json=values)
    data = response.json()
    print(data)

    values = {"first_name": "Nick", "last_name": "Huang", "email": "nhuang@gmail.com", "resume": "I Love Hippos"}
    response = requests.post(URL_Get, json=values)
    data = response.json()
    print(data)

    values = {"first_name": "Johnson", "last_name": "Benson", "email": "johnBen@gmail.com", "resume": "I Love Proctoring"}
    response = requests.post(URL_Get, json=values)
    data = response.json()
    print(data)

    # response = requests.get(URL_Get2)
    # data = response.json()
    # print(data)

    # response = requests.get(URL_Get3)
    # data = response.json()
    # print(data)

    # values = {"first_name": "Nick", "last_name": "Huang", "email": "haha@gmail.com"}
    # response = requests.put(URL_Get, json=values)
    # data = response.json()
    # print(data)


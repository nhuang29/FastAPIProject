import requests

URL_Get = "http://127.0.0.1:8000/leads/"
if __name__ == "__main__":
    values = {"first_name": "Huang", "last_name": "Nick", "email": "coffee@gmail.com", "resume": "I Love Oranges"}
    response = requests.post(URL_Get, json=values)
    data = response.json()
    print(data)

    values = {"first_name": "Juju", "last_name": "Schuster", "email": "jschuster@gmail.com", "resume": "I Love Hippos"}
    response = requests.post(URL_Get, json=values)
    data = response.json()
    print(data)

    values = {"first_name": "Carmen", "last_name": "Hagan", "email": "cHagan@gmail.com", "resume": "I Love Proctoring"}
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


import requests

url = "https://oeis.org/search"
parametres = {"q": "1,2,3,6,11,23,47,106,235",
              "fmt": "json"}

r = requests.get(url, params=parametres)
dico = r.json()
print(dico)
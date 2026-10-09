import requests

coin_list = []

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text.split("<td>")
for elem in response_text:
    if elem.startswith("USD"):
        for elem2 in elem.split("</td>"):
            if elem2.startswith("USD"):
                coin_list.append(elem2)

usd = float(coin_list[0].replace("USD", "").replace(",", "."))
print(usd)
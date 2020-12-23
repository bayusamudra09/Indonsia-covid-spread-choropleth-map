import datetime
import requests
import json


data = []
api = "https://api.kawalcorona.com/indonesia/provinsi/"
response = requests.get(api).json()
tanggal = str(datetime.date.today())
for row in response:
    kode_prov = row["attributes"]["Kode_Provi"]
    provinsi = row["attributes"]["Provinsi"]
    positif = row["attributes"]["Kasus_Posi"]
    sembuh = row["attributes"]["Kasus_Semb"]
    meninggal = row["attributes"]["Kasus_Meni"]
    kasus = {"tanggal": tanggal, "FID": kode_prov, "provinsi": provinsi, "positif": positif, "sembuh": sembuh, "meninggal": meninggal}
    data.append(kasus)

with open(f'covid_files/covid_{tanggal}.json', 'w') as file:
    json.dump(data, file)
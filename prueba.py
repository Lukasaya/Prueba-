import requests

response = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json')
heroes = response.json()

for hero in heroes['members']:
    if hero['name'] == 'Eternal Flame':
        print(f"El superpoder de Eternal Flame es: {hero['powers'][0]}")
        break


import requests

url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    total_powers = sum(len(hero['powers']) for hero in data['members'])
    ganador = None
    probabilidad_mayor = 0
    for heroe in data['members']:
        probabilidad = len(heroe['powers']) / total_powers
        print(f"{heroe['name']} probabilidad de ganar: {probabilidad}")
        if probabilidad > probabilidad_mayor:
            probabilidad_mayor = probabilidad
            ganador = heroe
    print(f"\n¡El ganador del torneo de héroes campeones DRY es: {ganador['name']}!")
else:
    print(f"La solicitud falló con el error {response.status_code}")




import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = response.json()

true_count = 0
for todo in todos:
    if todo['completed'] == True:
        true_count += 1

print(f"La cantidad de documentos que devuelven valor true es: {true_count}")




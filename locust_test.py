from locust import HttpUser, task, between, constant

class WebsiteUser(HttpUser):
    wait_time = constant(1)  # Tiempo constante entre tareas

    @task(1)
    def load_home_page(self):
        # Acceder a la página de inicio
        response = self.client.get("/")
        self._print_response("Acceder a la página de inicio", response)

    @task(2)
    def login(self):
        # Acceder a Form Authentication y realizar intento de inicio de sesión
        login_data = {
            'username': 'tomsmith',
            'password': 'SuperSecretPassword!'
        }
        response = self.client.post("/login", data=login_data)
        self._print_response("Intento de inicio de sesión", response)

    @task(1)
    def download_file(self):
        # Descargar archivo en File download 
        response = self.client.get("/download/testPDF.pdf")
        self._print_response("Descarga de archivo testPDF.pdf", response)

    def _print_response(self, task_name, response):
        print(f"Tarea: {task_name}")
        print(f"URL: {response.request.url}")
        print(f"Tiempo de respuesta: {response.elapsed.total_seconds() * 1000} ms")
        print(f"Método HTTP: {response.request.method}")
        print(f"Status: {response.status_code} {response.reason}")

        total_time = response.elapsed.total_seconds()
        print(f"Tiempo total de ejecución: {total_time * 100} ms")
    
    def on_start(self):
        # Código que se ejecuta al inicio de cada usuario simulado 
        pass

# Configuración de la prueba
class LoadTestConfig:
    host = "https://the-internet.herokuapp.com"

if __name__ == "__main__":
    # locust -f locust_test.py --users 200 --spawn-rate 10
    pass
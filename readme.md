# PassGuard-REST-API

## Ejecución
1- Clonar este proyecto: `git clone https://github.com/AlanHoltz/passguard-rest-api.git`.

2- Dirigirse a la ruta principal y crear el entorno virtual: `py -3 -m venv .venv`.

3- Ejecutar entorno virtual: `.venv\Scripts\activate`.

4- Instalación de dependencias. Primero se instala Flask con: `pip install Flask`. Luego, todas las dependencias de `requirements.txt`, con el siguiente comando: `pip install -r requirements.txt`.

5- Levantar la base de datos de prueba localmente. Archivo: `passguard.sql`, en la ruta principal.

6- Ejecutar: `flask --app run run`.


### Users

| Method     | URI                               | Action                                                  |
|------------|-----------------------------------|---------------------------------------------------------|
| `POST`     | `/users/register`                        | `Creates a new user` |
| `POST` | `/users/login`                        | `Creates a new user session`                                                |

### Boxes

| Method     | URI                               | Action                                                  |
|------------|-----------------------------------|---------------------------------------------------------|
| `POST`     | `/users/boxes`                           | `Creates a new box for the given user`       |
| `GET` | `/users/boxes`                           | `Get the user boxes`         |
| `DELETE`      | `users/boxes/{box_name}`                      | `Delete a box by its name`       |



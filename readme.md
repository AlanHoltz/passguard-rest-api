# PassGuard-REST-API

## Users

| Method     | URI                               | Action                                                  |
|------------|-----------------------------------|---------------------------------------------------------|
| `POST`     | `/users/register`                        | `Creates a new user` |
| `POST` | `/users/login`                        | `Creates a new user session`                                                |

## Boxes

| Method     | URI                               | Action                                                  |
|------------|-----------------------------------|---------------------------------------------------------|
| `POST`     | `/users/boxes`                           | `Creates a new box for the given user`       |
| `GET` | `/users/boxes`                           | `Get the user boxes`         |
| `DELETE`      | `users/boxes/{box_name}`                      | `Delete a box by its name`       |



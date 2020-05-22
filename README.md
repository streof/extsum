# Extsum

`extsum` finds the ID of a [Picsum photo](https://picsum.photos/). For example,
to obtain a random 200x300 photo, one can make a `GET` request to
https://picsum.photos/200/300. The server will then redirect your request to the
location of a random photo. If that photo happened to be, say 42, you'll get
redirected to https://i.picsum.photos/id/42/200/300.jpg. The `Location` response
header of your `GET` request will contain this information. 

However, there is also another (less straightforward) way to obtain the ID of
your photo: from its metadata. And this is exactly what `extsum` does.

```
$ git clone https://github.com/streof/extsum
$ cd extsum

# Regular install
$ pip install .

# Developer install
$ pip install -e '.[dev]'

# Get started
$ python extsum
Found ID 42

# Run tests (only developer install)
pytest -v
```

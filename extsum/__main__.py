import extsum as ext

URL = "https://i.picsum.photos/id/42/1/1.jpg"
# Uncomment for random Picsum photo
# URL = "https://picsum.photos/1/1"

if __name__ == '__main__':
    # Init
    photo = ext.Load(URL)
    photo_parsed = ext.Parse(photo)

    # Print found ID (if any)
    id_found = photo_parsed.find_id()
    if id_found is None:
        print("Couldn't find any ID")
    else:
        print(f"Found ID {id_found}")

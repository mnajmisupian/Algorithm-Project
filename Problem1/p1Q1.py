# Q1
import requests  # Make network requests

# Display images
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

apikey = ""
base = (
    f"https://maps.googleapis.com/maps/api/staticmap?key={apikey}&size=640x640&scale=2&"
)


def showImageFromUrl(url, name="map_points"):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(img)
    plt.savefig(f"{name}.png")
    # plt.show()
    plt.clf()

def start():
    cityLE = (3.0319924887507144, 101.37344116244806)
    posLaju = (3.112924170027219, 101.63982650389863)
    gdex = (3.265154613796736, 101.68024844550233)
    jnt = (2.9441205329488325,101.7901521759029)
    dhl = (3.2127230893650065, 101.57467295692778)
    coordinates = [cityLE, posLaju, gdex, jnt, dhl]
    labels = ["C", "P", "G", "J", "D"]
    colors = ["red", "green", "blue", "purple", "orange"]

    # Forming request, documentaion is at https://developers.google.com/maps/documentation/maps-static/start
    requestUrl = base

    for i in range(len(coordinates)):
        requestUrl += f"&markers=color:{colors[i]}%7Clabel:{labels[i]}%7C{coordinates[i][0]},{coordinates[i][1]}"

    # Display the image from requestUrl
    showImageFromUrl(requestUrl)

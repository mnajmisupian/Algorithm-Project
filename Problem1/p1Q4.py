# Q4

import array
import googlemaps
import requests  # Make network requests

# Display images
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

apikey = ""
gmapclient = googlemaps.Client(key=apikey)


base = (
    f"https://maps.googleapis.com/maps/api/staticmap?key={apikey}&size=640x640&scale=2&"
)


def showImageFromUrl(url, name="map"):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(img)
    plt.savefig(f"{name}.png")
    plt.show()


cityLE = (3.0319924887507144, 101.37344116244806)
posLaju = (3.112924170027219, 101.63982650389863)
gdex = (3.265154613796736, 101.68024844550233)
jnt = (3.265154613796736, 101.68024844550233)
dhl = (3.2127230893650065, 101.57467295692778)

# customer1
Rawang = (3.3615395462207878, 101.56318183511695)
BukitJelutong = (3.1000170516638885, 101.53071480907951)
# customer2
SubangJaya = (3.049398375759954, 101.58546611160301)
PuncakAlam = (3.227994355250716, 101.42730357605375)
# customer3
Ampang = (3.141855957281073, 101.76158583424586)
Cyberjaya = (2.9188704151716256, 101.65251821655471)


def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


courier = [cityLE, posLaju, gdex, jnt, dhl]
courierName = ["City-link Express", "Poslaju", "GDex", "J&T", "DHL"]
origin = [Rawang, SubangJaya, Ampang]
originName = ["Rawang", "SubangJaya", "Ampang"]
destination = [BukitJelutong, PuncakAlam, Cyberjaya]
destinationName = ["BukitJelutong", "PuncakAlam", "Cyberjaya"]
distance = []
polylines = {}


j = 0
while j < 3:
    print(f"customer {j+1}")
    i = 0
    while i != 5:
        hub = courier[i]
        name = courierName[i]
        originPoint = origin[j]
        destinationPoint = destination[j]
        d_goog = gmapclient.directions(originPoint, hub, mode="driving")
        d_goog2 = gmapclient.directions(hub, destinationPoint, mode="driving")
        new_d = d_goog[0]["legs"][0]["distance"]["value"]
        new_d2 = d_goog2[0]["legs"][0]["distance"]["value"]

        poly1 = d_goog[0]["overview_polyline"]["points"]
        poly2 = d_goog2[0]["overview_polyline"]["points"]

        print(
            f"Driving distance from {originName[j]} -> {name} ->{destinationName[j]} :"
        )
        distance.append(new_d + new_d2)

        # Adding the two polyline into a python dict
        polylines[new_d + new_d2] = [poly1, poly2]

        print((distance[i] / 1000), "km")
        i = i + 1

    print(distance)
    sortedDistance = distance.copy()
    n = len(sortedDistance)

    quickSort(sortedDistance, 0, n - 1)
    print(sortedDistance)
    index = distance.index(sortedDistance[0])
    print(distance.index(sortedDistance[0]))
    shortestDistance = distance[index]
    print(
        f"The shortest distance is using {courierName[index]} with distance of {shortestDistance/ 1000} km"
    )
    print()

    # Forming polyline, documentation is at https://developers.google.com/maps/documentation/maps-static/start#Paths
    requestUrl = base

    # Appending BEFORE route to request
    d_goog3 = gmapclient.directions(originPoint, destinationPoint, mode="driving")
    poly3 = d_goog[0]["overview_polyline"]["points"]
    requestUrl += f"&path=weight:3%7Ccolor:0x0000ff80%7Cenc:{poly3}"

    # Appending AFTER route to request
    shortest_poly = polylines[
        shortestDistance
    ]  # Retrieve back the two polylines that make up the shortest route
    requestUrl += f"&path=weight:3%7Ccolor:0xff000080%7Cenc:{shortest_poly[0]}"
    requestUrl += f"&path=weight:3%7Ccolor:0xff000080%7Cenc:{shortest_poly[1]}"

    # Show map of before and after
    print(f"Showing map of before (blue) and after (red)")
    showImageFromUrl(requestUrl, name=f"map_customer{j+1}")

    print()
    distance = []
    polylines = {}
    j = j + 1

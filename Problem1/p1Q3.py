import googlemaps
import array

arrdistDic = {}


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


def main():
    global arrdistDic
    apikey = ""
    gmapclient = googlemaps.Client(key=apikey)

    cityLE = (3.0319924887507144, 101.37344116244806)
    posLaju = (3.112924170027219, 101.63982650389863)
    gdex = (3.265154613796736, 101.68024844550233)
    jnt = (2.9441205329488325, 101.7901521759029)
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

    courier = [cityLE, posLaju, gdex, jnt, dhl]
    courierName = ["cityLE", "posLaju", "gdex", "jnt", "dhl"]
    origin = [Rawang, SubangJaya, Ampang]
    originName = ["Rawang", "SubangJaya", "Ampang"]
    destination = [BukitJelutong, PuncakAlam, Cyberjaya]
    destinationName = ["BukitJelutong", "PuncakAlam", "Cyberjaya"]
    distance = []

    j = 0
    while j != 3:
        print(f"customer {j+1}")
        arrdistDic[j + 1] = {}
        i = 0
        while i != 5:
            hub = courier[i]
            name = courierName[i]
            originPoint = origin[j]
            destinationPoint = destination[j]
            d_goog = gmapclient.distance_matrix(originPoint, hub, mode="driving")
            d_goog2 = gmapclient.distance_matrix(hub, destinationPoint, mode="driving")
            new_d = d_goog["rows"][0]["elements"][0]["distance"]["value"]
            new_d2 = d_goog2["rows"][0]["elements"][0]["distance"]["value"]
            print(
                f"Driving distance from {originName[j]} -> {name} -> {destinationName[j]} :"
            )
            distance.append(new_d + new_d2)
            arrdistDic[j + 1][courierName[i]] = new_d + new_d2
            print((distance[i] / 1000), "km")
            i = i + 1

        print(distance)
        print(arrdistDic)
        sortedDistance = distance.copy()
        # sortedDistance.sort()
        n = len(sortedDistance)

        quickSort(sortedDistance, 0, n - 1)
        print(sortedDistance)
        index = distance.index(sortedDistance[0])
        print(distance.index(sortedDistance[0]))
        shortestDistance = distance[index]
        globaldistance = sortedDistance
        print(
            f"The shortest distance is using {courierName[index]} with distance of {shortestDistance/ 1000} km"
        )
        print()
        distance = []
        j = j + 1


def gotop3():
    return arrdistDic


# i=0
# while(i!=5):
#     hub = courier[i]
#     name=courierName[i]
#     originPoint = origin[j]
#     destinationPoint = destination[j]
#     d_goog = gmapclient.distance_matrix(originPoint, hub, mode='driving')
#     d_goog2 = gmapclient.distance_matrix(hub, destinationPoint, mode='driving')
#     new_d = d_goog['rows'][0]['elements'][0]['distance']['value']
#     new_d2=d_goog2['rows'][0]['elements'][0]['distance']['value']
#     print(f'Driving distance from Rawang -> {name} ->Bukit Jelutong :')
#     distance.append(new_d+new_d2)
#     print((distance[i] / 1000), 'km')
#     i=i+1
#
# print(distance)
# sortedDistance=distance.copy()
# sortedDistance.sort()
# print(sortedDistance)
# index=distance.index(sortedDistance[0])
# print(distance.index(sortedDistance[0]))
# print(f'The shortest distance is using {courierName[index]} with distance of {distance[index]/1000} km' )

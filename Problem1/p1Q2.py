import gmplot
import googlemaps

apikey = ""
gmapclient = googlemaps.Client(key=apikey)
i = 3
while i != 0:
    if i == 3:
        originPoint = "Rawang"
        destinationPoint = "Bukit Jelutong"
        d_goog = gmapclient.distance_matrix(
            originPoint, destinationPoint, mode="driving"
        )
        new_d = d_goog["rows"][0]["elements"][0]["distance"]["value"]
        print(f"Driving distance from {originPoint} to {destinationPoint} :")
        print((new_d / 1000), "km")
        i = i - 1
    elif i == 2:
        originPoint = "Subang Jaya"
        destinationPoint = "Puncak Alam"
        d_goog = gmapclient.distance_matrix(
            originPoint, destinationPoint, mode="driving"
        )
        new_d = d_goog["rows"][0]["elements"][0]["distance"]["value"]
        print(f"Driving distance from {originPoint} to {destinationPoint} :")
        print((new_d / 1000), "km")
        i = i - 1
    else:
        originPoint = "Ampang"
        destinationPoint = "Cyber Jaya"
        d_goog = gmapclient.distance_matrix(
            originPoint, destinationPoint, mode="driving"
        )
        new_d = d_goog["rows"][0]["elements"][0]["distance"]["value"]
        print(f"Driving distance from {originPoint} to {destinationPoint} :")
        print((new_d / 1000), "km")
        i = i - 1

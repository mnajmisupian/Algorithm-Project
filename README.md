# Algorithm Project
 One of the essences of computer science and information technology is to solve problems faced by
humankind. As the outcome of this project, you are required to develop a computer program that is able to
resolve the following problems:-
Problem 1: Customer who needs to make a delivery needs to know which courier company can does it
fast (assuming that the shorter the distance, the quicker is the delivery). The application will analyse five
(5) local courier companies which have their delivery hubs located in various locations in West Malaysia.
The details of the courier companies and their delivery hubs are given in Table 1.
Courier Company Delivery Hub Coordinate
City-link Express Port Klang 3.0319924887507144,
101.37344116244806
Pos Laju Petaling Jaya 3.112924170027219,
101.63982650389863
GDEX Batu Caves 3.265154613796736,
101.68024844550233
J&T Kajang 2.9441205329488325,
101.7901521759029
DHL Sungai Buloh 3.2127230893650065,
101.57467295692778
*Hub locations are fictional – created for the purposes of this project.
Table 1: Details of courier companies and their hub locations.
1. Get and mark locations of all hub locations given in Table 1.
a. Guide 1: you can use Python Geocoding Toolbox
Lookup: https://pypi.python.org/pypi/geopy#downloads
b. Guide 2: you can use gmplot
Lookup: https://github.com/vgm64/gmplot
2. Let say, three (3) customers would like to make a door-to-door parcel delivery using any one of the
courier companies, details as given in Table 2. Get the distances between origin and destination.
Customer Origin Destination
Customer 1 Rawang
(3.3615395462207878,
101.56318183511695)
Bukit Jelutong
(3.1000170516638885,
101.53071480907951)
Customer 2 Subang Jaya
(3.049398375759954,
101.58546611160301)
Puncak Alam
(3.227994355250716,
101.42730357605375)
Customer 3 Ampang Cyberjaya
(3.141855957281073,
101.76158583424586)
(2.9188704151716256,
101.65251821655471)
Table 2: Example customer delivery requests.
a. Guide 1: you can use Python Geocoding Toolbox
b. Guide 2: you should use Google Distance Matrix API
i. Login to the google developer’s website and follow through the examples. It is
important that you know how to use the API key given to you within the code that
you are going to use. Refer to this link:
https://developers.google.com/maps/documentation/distance-matrix/start
3. Assuming that all deliveries must go through their delivery hub. For example, a delivery from Kuala
Lumpur (origin) will go through Pos Laju Hub in Petaling Jaya to Putrajaya (destination). Suggest the
least distance that the parcel has to travel for each customer using every courier company.
4. Plot line between the destinations before and after the algorithm (defined in 4) is chosen.
a. Guide1: you can use google.maps.Polyline. You can refer to this link:
https://www.sitepoint.com/create-a-polyline-using-the-geolocation-and-the-google-mapsapi/

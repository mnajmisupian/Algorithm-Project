# Algorithm Project

One of the essences of computer science and information technology is to solve problems faced by

humankind. As the outcome of this project, you are required to develop a computer program that is able to

resolve the following problems:-

**Problem 1**: Customer who needs to make a delivery needs to know which courier company can does it

fast (assuming that the shorter the distance, the quicker is the delivery). The application will analyse five

(5) local courier companies which have their delivery hubs located in various locations in West Malaysia.

The details of the courier companies and their delivery hubs are given in Table 1.
| Courier Company | Delivery Hub | Coordinate |
|-----------------|--------------|------------|
| City-link Express | Port Klang | 3.0319924887507144, 101.37344116244806 |
| Pos Laju | Petaling Jaya | 3.112924170027219, 101.63982650389863 |
| GDEX | Batu Caves | 3.265154613796736, 101.68024844550233 |
| J&T | Kajang | 2.9441205329488325, 101.7901521759029 |
| DHL | Sungai Buloh | 3.2127230893650065, 101.57467295692778 |
			*Hub locations are fictional – created for the purposes of this project.
				Table 1: Details of courier companies and their hub locations.
				
1. Get and mark locations of all hub locations given in Table 1.
   - Guide 1: you can use Python Geocoding Toolbox Lookup:https://pypi.python.org/pypi/geopy#downloads

   - Guide 2: you can use gmplot
   Lookup: https://github.com/vgm64/gmplot

2. Let say, three (3) customers would like to make a door-to-door parcel delivery using any one of the courier companies, details as given in Table 2. Get the distances between origin and destination.

| Customer | Origin | Destination |
|----------|--------|-------------|
| Customer 1 | Rawang (3.3615395462207878,101.56318183511695) | Bukit Jelutong (3.1000170516638885,101.53071480907951) |
| Customer 2 | Subang Jaya (3.049398375759954,101.58546611160301) | Puncak Alam (3.227994355250716,101.42730357605375) |
| Customer 3 | Ampang (3.141855957281073,101.76158583424586) | Cyberjaya (2.9188704151716256,101.65251821655471) |
				Table 2: Example customer delivery requests.

- Guide 1: you can use Python Geocoding Toolbox
- Guide 2: you should use Google Distance Matrix API

  - Login to the google developer’s website and follow through the examples. It is important that you know how to use the API key given to you within the code that you are going to use. Refer to this link:
https://developers.google.com/maps/documentation/distance-matrix/start

3. Assuming that all deliveries must go through their delivery hub. For example, a delivery from Kuala Lumpur (origin) will go through Pos Laju Hub in Petaling Jaya to Putrajaya (destination). Suggest the
least distance that the parcel has to travel for each customer using every courier company.

4. Plot line between the destinations before and after the algorithm (defined in 4) is chosen.
	- Guide1: you can use google.maps.Polyline. You can refer to this link:
https://www.sitepoint.com/create-a-polyline-using-the-geolocation-and-the-google-mapsapi/


**Problem 2**: Shortest distance travelled does not mean that the courier company is the most
recommended option for customer to use. A sentiment analysis of the related news articles about the
courier company must be conducted.

5. Extract information from three (3) articles from online news websites that have published stories
related to each courier company.
	- Sometimes a webpage must be converted to the text version before it can be done.
		- Guide 1: You may refer to this website to extract word from a website https://www.textise.net/
	- Guide 2: You may refer to this website on how to count word frequency in a website https://programminghistorian.org/lessons/counting-frequencies
	- You can also filter stops words from the text you found.
		- Guide 3: Stops words such as conjunctions and prepositions. You may refer to this link: https://www.ranks.nl/stopwords
		- Program using a string matching algorithm to find and delete the stop words.

6. Plot line/scatter/histogram graphs related to the word count using Plotly (Word count, stop words)
	- Guide 3: You may refer to this link on how to install Plotly and how to use the API keys
http://www.instructables.com/id/Plotly-with-Python/
https://plot.ly/python/getting-started/

7. Compare words in the web pages with the positive, negative and neutral English words using a
String-Matching algorithm
	- Guide 4: You may use the following word as positive and negative English words
http://positivewordsresearch.com/list-of-positive-words/
http://positivewordsresearch.com/list-of-negative-words/
	- Put these words in a text file for you to access them in your algorithm.
	- Words that are not on the list can be considered as ‘neutral’.

8. Plot histogram graphs of positive and negative words found in the web pages.
	- Guide 5: Use Plotly

9. Give an algorithmic conclusion regarding the sentiment of those articles
	- Guide 6: If there are more positive words, conclude that the article is giving positive
sentiment, if there are more negative words, conclude that the article is giving negative
sentiment.
	- You may try to conclude in different perspectives such as whether the list of positive and
negative words above is accurate to be used in the context of the article you extracted the
text.
	- Based on the conclusion, you may say which courier company have the best sentiment.

**Problem 3**: Customers need to be able to choose the best courier company based on the distance as well
as the result of sentiment analysis of related online articles.

10. Calculate the total probability distribution of possible routes. Then, write the summary of the courier
companies, ranking from the most recommended to the least recommended based on distance and
sentiment.

**Problem 4**: Assuming that video or audio from the news or customer feedback will be used to provide
sentiment insights in the future, Dynamic Time Warping (DTW) is one of the algorithms that can
potentially be used. Explain the concept of DTW and demonstrate the implementation of DTW in
analysing a video or an audio. For example, given the following video (https://www.youtube.com/watch?v=ZwVFj8CfFeE), identify some words, for example “J&T”, “memohon” and “maaf”.
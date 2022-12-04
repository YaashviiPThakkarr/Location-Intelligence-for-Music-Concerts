# Location-Intelligence-for-Music-Concerts
Here's the ReadMe File for this Project:


[README.pdf](README.pdf)


The demonstration of Music Debut Helper is available on the link below.
1. https://youtu.be/PEPqqN5Fl3s (Demonstration video)
2. https://drive.google.com/file/d/19jlOCRIds-C-NuuiHrx8ydTGfRHf9O_G/view (Demonstration
with Scraping of one of the datasets -Ticketmaster and prototype model from 5:24 mins in the
video)

The Musician’s Helper website requires a combination of strong musical popularity data, consumer willingness to pay data, and music trend data in order to help assist musicians in deciding where to launch albums and where to focus their touring efforts. The running theory is that if we can pinpoint the most popular genres of music, geoparted by state or city, and cross apply that with the average willingness to pay in that state or city, we can provide an accurate recommendation to musicians on where to launch an album or set a city to tour through. To make Musicians Helper more sophisticated, we will also digest crime data in order to try and opt out of some cities or areas for tour dates, in order to maintain the safety of artists as we recommend optimal cities for them to pursue with their music.
- We thought to leverage Last.fm’s “Music Discovery” API in order to gather musical popularity lists to assist us in determining trending music. Through the Music Discovery Api, we hope to use metrics like play counts from artists and genres in order to interpret which music genres and styles are popular in a given city.
- The second source of data we chose to analyze was Numbeo, which provides great societal data. We intend to leverage Numbeo in order to grasp the willingness to pay for music as well as identify inopportune cities to tour in. We hope to use cost of living data to extract consumer willingness to pay, and look at crime data by state in order to set a desirability score in our recommender engine. This desirability score could allow musicians to steer clear from cities that might be unsafe, and target cities that might be lucrative.
- Our third source of data is Ticketmaster--we hope to analyze cities that are featuring incoming touring acts in order to evaluate the competition factor for a musician using Musician’s Helper. If a city has a high willingness to pay, low crime, and a high affinity amongst the music scene for the type of music that the artist in question creates, it is likely a great target city. However, if in the upcoming weeks there is a large volume of incoming touring acts, the Musician’s Helper site would recommend against touring in that city. Lots of Ticketmaster activity in the long run could be a great indicator of a healthy and thriving music scene, but too much activity in the short run would indicate a high volume of direct competitors to the musician. Musician’s Helper will digest this data to provide a strong recommendation of what cities an artist should tour in, and what cities they should target for album releases.

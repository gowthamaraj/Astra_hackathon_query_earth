Planet's volume and speed of imagery are unprecedented. Currently, Planet is operating around 200 satellites that travel a pole-to-pole path through the atmosphere, capturing around 1.4 million images per day as they go and feeding it back to 30 ground stations the company set up across the world. Many institutes and organizations are pitting little CubeSats on the space for their own purpose and for providing services. Hence it is very difficult to manually check every.
 

## PROPOSED IDEA:
We know how the google works. It is a kind of search engine which search the results using a keyword and will display the stuffs related to the keyword. Google indexes the websites related to our query keyword. We are implementing almost similar concept for the satellite images. As we get lot of image everyday, we cannot go through each set and find our datas. It would be highly time consuming and will not be helpful during emergency situations. Hence, we have come up with this idea "Querying the planet".
  
 

## WHY IT MATTERS:
During a crisis, it is important to map the entire affected area comprehensively, which is very difficult and time-consuming to do manually. This method could get important disaster mapping information into the hands of rescue and relief workers in significantly less time. In the future, this could be extended to quantify disaster impact on natural features like farmlands and forests, and to assess damage from other disasters, such as earthquakes. We just query the system like "forest fire near me”, “earth quake in Canada". Then, we will get the required information.
 

## IMPLEMENTATION AND DESIGN PLAN:
We will create a deep learning model which could identify the main objects in the image given by the satellite and put these images reference and tags based on the objects present in the database. The database will even have the counts or attributes of the tags ex: " house - 1045, trees - 678". Hence, it will also help us to trend analysis with the database ex: " rate of decrease of trees with no of houses on a particular area". The user will access these features using a webpage and will be able to query on the images he feed or already existing data. The trend analysis will be a very useful thing in terms of analysing the changes around us and for identifying relations between things over time. 
Technologies used: web-development - Flask, deep learning with python, dbms.
 


References:

	https://emerj.com/ai-sector-overviews/ai-applications-for-satellite-imagery-and-data/
	http://interactive.satellitetoday.com/via/may-2018/ai-heads-to-space-with-a-constellation-of-use-cases/
	https://www.spaceknow.com/satellite-ai/



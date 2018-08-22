# URLLookupService - Malware or  No Malware

This is a microservice written using Python, Flask and MySql to achieve a simple functionality- to check weather a URL is Malware or Not. 
The decision is based on a database that contains a list of URLs and their informations.


## Instructions to build and run:- 
### Requirements:-
- Python 3+

### Instructions:-
1. Clone the project- `git clone https://github.com/princemanohar/URLLookupService.git`
2. Go into the project folder- `cd  URLLookupService`
3. Install Dependent python modules - `pip install - requirements.txt`
4. Run the app- `python run.py`


# Extra Considerations:
1. **The number of requests may exceed the capacity of this system:** In that case, this flask app can be installed on multiple servers and they can be placed behind a **Load Balancer**. The load balancer will distribute the requests evenly to these flask apps, thereby balancing the traffic. That is how this application can be scaled to increasing traffic. Say, each system with the flask app running on it can handle 50 requests/second. And the traffic we are supporting is 500 requests/second, in that case, we can go ahead with 11 servers with this service running on them, hence we now support `11*50=550` requests per second (adding some redundancy).

2. **Strategies to update the service with new URLs:** This app has an update api, using which the entries in the database can be changed. To support 5000 requests per day, with requests evenly distributed throughout the day, i.e. 3 updates/second, it will be a pretty nominal load on our app and the database, which can handle this update traffic easily. However, in case these updates are not evenly distributed, meaning that, the updates come only over a certain hour of that day, then, it can be a problem, as we may not want our database to have a high load due to sudden increase in updates which may affect the read-times.
In that case, we will have to push the update requests into a queue and then write a consumer which subscribes to that queue and writes the entries to the database at a constant speed. This approach will keep an even update traffic at our DB, and will update all url entries eventually (with some delay). 


# Weather-App 

Testing web application to handle Django (Docker) basic concepts

[OpenWeatherMap](https://openweathermap.org) API used to access the live weather details.

[Bulma](https://bulma.io/) Framework for the css layout cuz it's easy and attractive. <br />

## Docker config

You can deploy a new version by building the App Image and running the image by using Docker

To build the image:

```
docker build . -t weather_app:latest
```

Before running the run command, we have to stop old containers as they could be binding the expose port for the container, you can remove them by using the following commands:

```
docker stop weather_web_app
docker rm weather_web_app
```

You can also run them together by using the command below

````
docker stop demo && docker rm demo 
```

The first command stops the running container and the second remove it from the container list.

To run the Image:


```
docker run -dp 8000:8000 --name weather_web_app weather_app:latest 
```

kjkbscjbadjbds
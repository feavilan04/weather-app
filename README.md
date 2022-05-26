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
Docker stop weather_web_app
Docker rm weather_web_app
```

The first command stops the running container and the second remove it from the container list.

To run the Image:

```
docker run -p 8000:8000 weather_app:latest --name weather_web_app
```

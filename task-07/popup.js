document.addEventListener("DOMContentLoaded", function () {
  const locationInput = document.getElementById("locationInput");
  const getWeatherButton = document.getElementById("getWeatherButton");
  const weatherResult = document.getElementById("weatherResult");

  getWeatherButton.addEventListener("click", function () {
    const location = locationInput.value;
    const apiKey = '31ab54d8e606edd3be43fe33b50bb91f';
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}`;

    weatherResult.textContent = '';

    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        var temperature = data.main.temp;
        const description = data.weather[0].description;
        const cityName = data.name;
        temperature = temperature - 273.15;
        temperature = temperature.toFixed(2)
        weatherResult.textContent = `Weather in ${cityName}: ${description}, Temperature: ${temperature} °C`;

        const suggestions = document.getElementById("suggestions");
        if (description.includes("rain")) {
          suggestions.textContent = "Don't forget to carry an umbrella!";
        } else if (description.includes("clear")) {
          suggestions.textContent = "Enjoy the sunny weather.";
        } else if(description.includes("mist")){
          suggestions.textContent = "Use your Fog Lights!!!";
        }
        else if (description.includes("cloudy") || description.includes("clouds")){
          suggestions.textContent = "Cloudy with a chance of meat balls";
        }
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
        weatherResult.textContent = 'Failed to fetch weather data.';
      });
    });
  });

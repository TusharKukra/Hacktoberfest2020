// Importing Libraries
const request = require("request");
const say = require("say");
const boxen = require("boxen");
const chalk = require("chalk");
const figlet = require("figlet");
const inquirer = require("inquirer");
const Spinner = require("clui").Spinner;

// Initializing url variable
let url;

// Wrapped Everything inside async function
(async () => {
  // Initialization
  console.log(
    chalk.green(figlet.textSync("Weathery", { horizontalLayout: "full" }))
  );

  // Asking City name and Api Key
  const answers = await inquirer.prompt([
    {
      name: "city",
      type: "input",
      message: "Enter name of the City: ",
      validate: function (value) {
        if (value.length) {
          return true;
        } else {
          return "Please enter the name of the city.";
        }
      },
    },
    {
      name: "apiKey",
      type: "input",
      message: "Enter Your https://api.openweathermap.org/ Api Key: ",
      validate: function (value) {
        if (value.length) {
          return true;
        } else {
          return "Please enter your Api Key given from https://api.openweathermap.org/.";
        }
      },
    },
  ]);
  url = `https://api.openweathermap.org/data/2.5/weather?q=${answers.city}&appid=${answers.apiKey}&units=metric`;

  // Initiazlizing Loader and Starting it.
  const loader = new Spinner(`Checking Weather of ${answers.city}...`);
  loader.start();

  const showWeather = async (err, _response, body) => {
    if (err) {
      console.warn("Error: ", err);
      process.exit(1);
    }

    const data = JSON.parse(body);

    const temp = data.main.temp;
    const feels_like = data.main.feels_like;
    const description = data.weather[0].description;
    const temp_min = data.main.temp_min;
    const temp_max = data.main.temp_max;
    const humidity = data.main.humidity;

    // Setting the weather data to message
    message = `It's ${temp} degrees and feels like ${feels_like} with ${description} in ${data.name}!\nToday's minimum temperature would be ${temp_min} and maximum would be ${temp_max}.\nNow, the humidity is ${humidity}%!\n\nThank You! And Have a nice day!`;

    loader.stop();

    console.log(
      boxen(message, {
        padding: 1,
        margin: 1,
        borderColor: "#3867d6",
        borderStyle: "round",
      })
    );

    process.exit(0);
  };

  request(url, showWeather);
})();

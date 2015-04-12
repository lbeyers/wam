wget http://m.weather.com/weather/tomorrow/SFXX0444 -O weather_com_$(date +%Y%m%dT%H%M%S).html
wget http://www.accuweather.com/en/za/stellenbosch/301201/weather-forecast/301201 -O accuweather_$(date +%Y%m%dT%H%M%S).html
wget http://www.yr.no/place/South_Africa/Western_Cape/Stellenbosch/long.html -O yr_no_longterm_$(date +%Y%m%dT%H%M%S).html
wget http://www.yr.no/place/South_Africa/Western_Cape/Stellenbosch/ -O yr_no_shortterm_$(date +%Y%m%dT%H%M%S).html
wget http://www.timeanddate.com/weather/south-africa/stellenbosch -O time_and_date_$(date +%Y%m%dT%H%M%S).html
wget http://www.wunderground.com/weather-forecast/ZA/Stellenbosch.html  -O weather_underground_$(date +%Y%m%dT%H%M%S).html

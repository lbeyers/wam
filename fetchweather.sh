mkdir fetched_data
wget http://m.weather.com/weather/tomorrow/SFXX0444 -O fetched_data/weather_com_$(date +%Y%m%dT%H%M%S).html
wget http://www.accuweather.com/en/za/stellenbosch/301201/weather-forecast/301201 -O fetched_data/accuweather_$(date +%Y%m%dT%H%M%S).html
wget http://www.yr.no/place/South_Africa/Western_Cape/Stellenbosch/long.html -O fetched_data/yr_no_longterm_$(date +%Y%m%dT%H%M%S).html
wget http://www.yr.no/place/South_Africa/Western_Cape/Stellenbosch/ -O fetched_data/yr_no_shortterm_$(date +%Y%m%dT%H%M%S).html
wget http://www.timeanddate.com/weather/south-africa/stellenbosch -O fetched_data/time_and_date_$(date +%Y%m%dT%H%M%S).html
wget http://api.wunderground.com/api/d9b8a12d46bf8df2/forecast/q/ZA/Stellenbosch.json -O fetched_data/weather_underground_$(date +%Y%m%dT%H%M%S).html
wget http://weather.sun.ac.za/home.php -O fetched_data/maties_$(date +%Y%m%dT%H%M%S).html
wget http://weather.lcao.co.za/index.php/Special_CurrentWeather -O fetched_data/la_colline_$(date +%Y%m%dT%H%M%S).html

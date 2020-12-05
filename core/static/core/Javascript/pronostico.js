const key ='d4lCENqd5A7laA7gRLMMNzqNR1wkbPXS';

//get weather information
const getWeather = async (id) => {
    const base = 'http://dataservice.accuweather.com/currentconditions/v1/';
    const query = `${id}?apikey=${key}`;

    const response = await fetch(base + query);
    const data = await response.json();

    
    return data[0];

};

//get city information
const getCity = async (city) =>{

    const base = 'http://dataservice.accuweather.com/locations/v1/search';
    const query = `?apikey=${key}&q=${city}`;

    const response = await fetch(base + query);
    const data = await response.json();

    return data[0];

};



//getCity('santiago').then(data => {
//        return getWeather(data.Key)
 //   }).then(data => {
//        console.log(data)
 //   }).catch(err => console.log(err));

//getWeather("60449");
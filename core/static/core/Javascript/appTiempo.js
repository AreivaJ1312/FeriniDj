
const cityForm = document.querySelector('form');
const card = document.querySelector('.card');
const details = document.querySelector('.details');
const time = document.querySelector('img.time');
const icon = document.querySelector('.icon img');

const updateUI = (data) => {
        // destructure propierties
        const { cityDets, weather } = data;

    //uptade details template
    details.innerHTML = `
        <h5 class="my-3">${cityDets.EnglishName}</h5>
        <div class="my-3">${weather.WeatherText}</div>
        <div class="display-4 my4">
            <span>${weather.Temperature.Metric.Value}</span>
            <span>&deg;</span>
        </div>
     `;

     //cargar imagens dia o noche
    const iconSrc = 'static/core/img/icons/' +weather.WeatherIcon + '.svg';
    icon.setAttribute('src', iconSrc);


     let timeSrc = weather.IsDayTime ? 'static/core/img/day.svg' : 'static/core/img/night.svg' ;
    time.setAttribute('src',timeSrc);

     //remove the d-none class if present
     if(card.classList.contains('d-none')){
         card.classList.remove('d-none');
     }
};


const updateCity = async (city) =>{

    const cityDets = await getCity(city);
    const weather = await getWeather(cityDets.Key);

    return{ cityDets, weather };

};

cityForm.addEventListener('submit',e =>{
    //prevent default action
    e.preventDefault();

    //get city value
    const city = cityForm.city.value.trim();
    cityForm.reset();

    // update de ui with new city
    updateCity(city)
        .then(data => updateUI(data))
        .catch(err => console.log(err));

});


const result = true ? 'value 1' : 'value 2';
console.log(result);

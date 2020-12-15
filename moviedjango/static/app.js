const icons = Array.from(document.getElementsByClassName("favorite-icon"));
console.log(icons)

/* let CSRF_KEY_NAME="csrftoken=";
let csrf = document.cookie.split(";").find((cookie)=>{
    return cookie.trim().substr(0, CSRF_KEY_NAME.length) == CSRF_KEY_NAME;
}).substr(CSRF_KEY_NAME.length); */

icons.forEach(icon =>{
    icon.addEventListener('click', async (e) =>
    {
        const result = await fetch(`favorite`,{method: 'POST',});
        const favored = document.getElementById('fav-id');
        const disfavored = document.getElementById('fav-id2');
        const fav_id_class = favored.classList;
        const disfav_id_class = disfavored.classList;
        if (fav_id_class.contains('hidden')) {
            disfav_id_class.add('hidden');
            fav_id_class.remove('hidden');
        }
        else {
            fav_id_class.add('hidden');
            disfav_id_class.remove('hidden');
            fav_id_class.add('hidden');
        }
    });
});

const iconstop = Array.from(document.getElementsByClassName("favorite-icon-top"));

iconstop.forEach(icontop =>{
    
    icontop.addEventListener('click', async (e) =>
    {
        const result = await fetch(`/movie/${icontop.dataset.movieid}/favorite`,{method: 'POST',});

        const favored = document.getElementById('fav-id');
        const disfavored = document.getElementById('fav-id2');

        const fav_id_class = favored.classList;
        const disfav_id_class = disfavored.classList;
        console.log(iconstop);

        if (fav_id_class.contains('hidden')) {
            disfav_id_class.add('hidden');
            fav_id_class.remove('hidden');
            console.log("aaa");
        }
        else {
            fav_id_class.add('hidden');
            disfav_id_class.remove('hidden');
            fav_id_class.add('hidden');
            console.log("bbb");
        }
    });
});
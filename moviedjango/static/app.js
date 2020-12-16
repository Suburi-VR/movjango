const icons = Array.from(document.getElementsByClassName("favorite-icon"));

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
        const favored = document.getElementById(`fav${icontop.dataset.movieid}`);
        const disfavored = document.getElementById(`disfav${icontop.dataset.movieid}`);
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




const iconsfav = Array.from(document.getElementsByClassName("favorite-icon-fav"));
iconsfav.forEach(iconfav =>{
    iconfav.addEventListener('click', async (e) =>
    {
        const result = await fetch(`/movie/${iconfav.dataset.movieid}/favorite`,{method: 'POST',});
        const favored = document.getElementById(`fav${iconfav.dataset.movieid}`);

        const fav_id_class = favored.classList;
        if (!fav_id_class.contains('hidden')) {
            fav_id_class.add('hidden');
            const movies = Array.from(document.getElementsByClassName("favorite_movies"));
            movies.forEach(movie =>{
                const favoredmov = document.getElementById(`favmov${iconfav.dataset.movieid}`);
                const favoredmov_id_class = favoredmov.classList;
                favoredmov_id_class.add('hidden');
            });
        }
    });
});
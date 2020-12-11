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
        if (fav_id_class.contains(hidden)) {
            disfav_id_class.add('hidden');
        }
        else {
            fav_id_class.add('hidden');
            disfav_id_class.remove('hidden');
        }
        console.log(fav_id_class);

    });
});
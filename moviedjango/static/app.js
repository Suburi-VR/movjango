const icons = Array.from(document.getElementsByClassName("favorite-icon"));

/* let CSRF_KEY_NAME="csrftoken=";
let csrf = document.cookie.split(";").find((cookie)=>{
    return cookie.trim().substr(0, CSRF_KEY_NAME.length) == CSRF_KEY_NAME;
}).substr(CSRF_KEY_NAME.length); */

icons.forEach(icon =>{
    icon.addEventListener('click', async (e) =>
    {
        const result = await fetch(`favorite`,{method: 'POST',});
        const id = document.getElementById("fav-id");
        const id2 = document.getElementById("fav-id2");
        console.log(id);
    });
});
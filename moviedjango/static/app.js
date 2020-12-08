const icons = Array.from(document.getElementsByClassName("favorite-icon"));
let f = document.createElement('form');
let CSRF_KEY_NAME="csrftoken=";
let csrf = document.cookie.split(";").find((cookie)=>{
    return cookie.trim().substr(0, CSRF_KEY_NAME.length) == CSRF_KEY_NAME;
}).substr(CSRF_KEY_NAME.length);
icons.forEach(icon => {
    icon.addEventListener('click', async (e) => {
        const result = await fetch(`/favorite`)
        f.method = 'post';
        f.innerHTML = `<input type="hidden" name="csrfmiddlewaretoken" value="${csrf}" />`;
        document.body.append(f);
        f.submit();
    });
    console.log(await result.json());
});
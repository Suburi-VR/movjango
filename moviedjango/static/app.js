const icons = Array.from(document.getElementsByClassName("favorite-icon"));
icons.forEach(icon =>{
    icon.addEventListener('click', async () => {
        const result = await fetch(`favorite`,{ method: 'POST' });
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
    icontop.addEventListener('click', async (e) => {
        const result = await fetch(`/movie/${icontop.dataset.movieid}/favorite`, { method: 'POST' });
        const favored = document.getElementById(`fav${icontop.dataset.movieid}`);
        const disfavored = document.getElementById(`disfav${icontop.dataset.movieid}`);
        const fav_id_class = favored.classList;
        const disfav_id_class = disfavored.classList;
        disfav_id_class.toggle('hidden');
        fav_id_class.toggle('hidden');
    });
});

/* jQuery使うとこうなるけど…。 */
/* $(document).ready(function(event){
    console.log("1111111")
    $(document).on('submit', '.post-form', function(event){
        console.log("22222222")
        event.preventDefault();
        console.log($(this).serialize());
        $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response){
            console.log("333333333")
            $('.main-comment-section').html(response['form']);
            const textbox = document.getElementById("id_text");
            textbox.value = "";
        },
        error: function(rs, e){
            console.log("44444444444444")
            console.log(rs.responseText);
        },
        });
    });
}); */


/* jQueryを使わずに！ */
const commentSend = document.getElementById("comment_send");
console.log(commentSend);
commentSend.addEventListener('click', async (e) => {
    let form = new FormData();
    form.append('text', '何入れる？');
    console.log(form);
    const result = await fetch(
        `comment_send`,
        {
            method: 'POST',
            headers: {'Content-Type': 'form-data'},
            body: form,
        })
        .then(response => console.log(response));
});
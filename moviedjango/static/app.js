const icons = Array.from(document.getElementsByClassName("favorite-icon"));
console.log(icons)
icons.forEach(icon =>{
    icon.addEventListener('click', async (e) => {
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

const commentSend = document.getElementById("comment-send");
console.log(commentSend);
commentSend.addEventListener('click', async (e) => {
    const result = await fetch(`comment_send`,{method: 'POST'});
    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response){
            $('.comment').html(response['comment']);
            console.log("OK");
        },
        error: function(rs, e){
            console.log(rs.responseText);
            console.log("NG");
        },
    });
});
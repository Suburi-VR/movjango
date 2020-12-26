const icons = Array.from(document.getElementsByClassName("favorite-icon"));
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

const commentSend = Array.from(document.getElementsByClassName("comment-send"));
console.log(commentSend);
commentSend.forEach(comment => {
    comment.addEventListener('click', async (e) => {
        const result = await fetch(`comment`,{ method: 'POST' });
    });
});
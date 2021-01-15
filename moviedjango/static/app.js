/* 【csrftoken】 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



const icons = Array.from(document.getElementsByClassName("favorite-icon"));
icons.forEach(icon => {
    icon.addEventListener('click', async () => {
        const result = await fetch(`favorite`, { method: 'POST' });
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
iconstop.forEach(icontop => {
    icontop.addEventListener('click', async (e) => {
        const result = await fetch(`/movie/${icontop.dataset.movieid}/favorite`, { method: 'POST' });
        const favored = document.getElementById(`fav${icontop.dataset.movieid}`);
        const disfavored = document.getElementById(`disfav${icontop.dataset.movieid}`);
        const fav_id_class = favored.classList;
        const disfav_id_class = disfavored.classList;
        console.log(fav_id_class);
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
            console.log("333333333");
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
commentSend.addEventListener('click', async (e) => {
    const value = document.getElementById("id_text").value;
    if (!value.match(/^[ 　\r\n\t]*$/)){
        const result = await fetch(
            `comment_send`,
            {
                method: 'POST',
                body: JSON.stringify(value),
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-type': 'application/json'
                }
            });
        const comments = document.getElementById("comments");
        const commentsList = Array.from(document.getElementsByClassName("comment"));
        console.log(commentsList[0])
        if (commentsList[0] == undefined){
            comments.insertAdjacentHTML('afterbegin',
            `<div class="modal fade" id="commentdeleteModal" tabindex="-1" role="dialog" aria-labelledby="commentdeleteModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="commentdeleteModalLabel">このコメントを削除します</h5>
                            <button type="button" class="close" datadismiss="modal" aria-label="Close">
                                <span aria-hidden="true" data-dismiss="modal">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            よろしいですか？
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary rounded-0" data-dismiss="modal">キャンセル</button>
                            <a href="{% url 'comment_delete' id=comment.id %}"><button type="button" class="btn btn-danger rounded-0">削除</button></a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="comment" id="new" data-id="new">
                <strong>NAME : ${comments.dataset.user}</strong>
                    <div class="row justify-content-between">
                        <p class="addcomment" style="width:1160px">${value}
                            <div class="comment_delete col-1">
                                <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#commentdeleteModal">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-square-fill" viewBox="0 0 16 16">
                                        <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm3.354 4.646L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 1 1 .708-.708z"/>
                                    </svg>
                                </button>
                            </div>
                        </p>`);
        }
        else{
            var commentId = Number(commentsList[0].id) + 1;
            comments.insertAdjacentHTML('afterbegin',
            `<div class="modal fade" id="commentdeleteModal${commentId}" tabindex="-1" role="dialog" aria-labelledby="commentdeleteModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="commentdeleteModalLabel">このコメントを削除します</h5>
                            <button type="button" class="close" datadismiss="modal" aria-label="Close">
                                <span aria-hidden="true" data-dismiss="modal">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            よろしいですか？
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary rounded-0" data-dismiss="modal">キャンセル</button>
                            <a href=/${commentId}/comment_delete><button type="button" class="btn btn-danger rounded-0">削除</button></a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="comment" id=${commentId} data-id=${commentId}>
                <strong>NAME : ${comments.dataset.user}</strong>
                    <div class="row justify-content-between">
                        <p class="addcomment" style="width:1160px">${value}
                            <div class="comment_delete col-1">
                                <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#commentdeleteModal${commentId}">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-square-fill" viewBox="0 0 16 16">
                                        <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm3.354 4.646L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 1 1 .708-.708z"/>
                                    </svg>
                                </button>
                            </div>
                        </p>`);
        }
        console.log(result);
    }
    const textbox = document.getElementById("id_text");
    textbox.value = "";
});
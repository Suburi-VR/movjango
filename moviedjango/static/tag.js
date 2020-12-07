const btn = document.getElementById("button-addon2");
btn.addEventListener('click', async (e) => {
    const input = document.getElementById("tag_input");
    const name = input.value;
    const result = await fetch(
        '/tag',
        {
            method: 'POST',
            body: JSON.stringify({
                name: name
            })
        }
    );
    console.log(await result.json());
});
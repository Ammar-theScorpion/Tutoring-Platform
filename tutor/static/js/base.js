/* Project specific Javascript goes here. */
console.log('sdfsdf')
document.addEventListener("htmx:afterRequest", (e) => {
    console.log('sdfsdf', e.detail)
    document.getElementById("overlay").classList.remove("hidden");
    const detail = e.detail;
    if(detail.target.id == 'popup'){
        document.getElementById("popup").classList.remove("hidden");
    }

    if(detail.target.id == 'all-posts'){
        document.getElementById("overlay").classList.add("hidden");
        document.getElementById("popup").classList.add("hidden");
    }
});

function closePopup() {
    document.getElementById("overlay").classList.add("hidden");
    document.getElementById("popup").classList.add("hidden");
}

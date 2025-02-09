const body = document.body

body.contentEditable = true

body.addEventListener('change', save)
function save(){
    localStorage.setItem("saved-content", body.innerHTML)
    body.innerHTML = localStorage.getItem("saved-content")
}




const me = document.getElementById(".loginform")
const button = document.getElementById("signing")

button.addEventListener("click", () => {
    if (me.style.display === "none") {
        me.style.display = "block"
    } else {
        me.style.display = "none"
    })
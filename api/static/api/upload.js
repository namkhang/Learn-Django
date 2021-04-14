let imageHTML = document.getElementById("image")
let file = document.getElementById("upload")

function change(){
    console.log(file);
    let image = URL.createObjectURL(file.files[0])
    imageHTML.src = image
}
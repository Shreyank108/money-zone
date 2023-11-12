const micro = document.getElementById('micro')

const loadImage = (event) => {
    micro.style.backgroundImage = "url(" + URL.createObjectURL(event.target.files[0]) + ")"
}

const add_image = document.getElementById('add_image')
add_image.addEventListener('click', () =>{
    micro.style.display = "flex"
})

const remove = document.getElementById('remove')
remove.addEventListener('click', () =>{
    micro.style.display = "none"
})
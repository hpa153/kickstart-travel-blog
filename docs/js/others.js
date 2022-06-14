// Show big gallery image on scroll
const galleryImage = document.querySelector(".gallery-big");

const appearOnScroll = () => {

  if (window.pageYOffset >= 400 && window.innerWidth > 600) {
    galleryImage.style.opacity = "1";
  } else { 
    galleryImage.style.opacity = "0";
  }
}

window.addEventListener("scroll", appearOnScroll);

// Change image of gallery big on click
function viewBig(source) {
  document.querySelector(".gallery-big-img").src = source;
}
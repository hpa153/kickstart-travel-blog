// Remove loader after loading complete
document.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {
    document.querySelector(".loader-container").style.display = "none";
  }, 4000);
})

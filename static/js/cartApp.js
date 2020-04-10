const button = document.querySelector(".no-cart-items a input");
const face = document.querySelector(".no-cart-items p");
if (button) {
  button.addEventListener("mouseover", () => {
    face.classList.remove("fa", "fa-frown-o");
    face.classList.add("fa", "fa-smile-o");
  });
  button.addEventListener("mouseout", () => {
    face.classList.remove("fa", "fa-smile-o");
    face.classList.add("fa", "fa-frown-o");
  });
}

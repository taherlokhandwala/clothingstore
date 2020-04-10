const changePassModal = document.querySelector(".change-password-modal");
const cancelButton = document.querySelector(".cancel-change-password");
const chnagePassword = document.querySelector(".change-password-link");

chnagePassword.addEventListener("click", () => {
  changePassModal.style.display = "block";
});
cancelButton.addEventListener("click", () => {
  changePassModal.style.display = "none";
});
window.addEventListener("click", (event) => {
  if (event.target == changePassModal) {
    changePassModal.style.display = "none";
  }
});

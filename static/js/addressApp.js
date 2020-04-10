const addNewAddress = document.querySelector(".add-new-address button");
const newAddressModal = document.querySelector(".new-address-modal");
const closeButton = document.querySelector(".address-action-buttons")
  .children[0];

addNewAddress.addEventListener("click", () => {
  newAddressModal.style.display = "block";
});
closeButton.addEventListener("click", () => {
  newAddressModal.style.display = "none";
});
window.addEventListener("click", (event) => {
  if (event.target == newAddressModal) {
    newAddressModal.style.display = "none";
  }
});

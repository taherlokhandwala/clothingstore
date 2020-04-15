const sizeChart = document.querySelector(".size-chart-span");
const sizeChartModal = document.querySelector(".size-chart-modal");
const closeButton = document.querySelectorAll(".close-modal-span");
const radioButtons = document.getElementsByName("size");
const submitButton = document.querySelector(".size-form button");
const sizeForm = document.querySelector(".size-form");
const h2BeforeAddCart = document.querySelector(".h2-before-addcart");
const productInfoContainer = document.querySelector(".product-info-container");
const productImages = document.querySelectorAll(".product-images img");
const imageModal = document.querySelector(".image-modal");
const imageModalImage = document.querySelector(".image-modal-image img");

// **Size chart modal logic**
sizeChart.addEventListener("click", () => {
  sizeChartModal.style.display = "block";
});

// **Image modal logic
productImages.forEach((image) => {
  image.addEventListener("click", () => {
    imageModal.style.display = "block";
    imageModalImage.src = image.src;
  });
});

// ** General closing of all modals
closeButton.forEach((button) => {
  button.addEventListener("click", () => {
    sizeChartModal.style.display = "none";
    imageModal.style.display = "none";
  });
});

window.addEventListener("click", (event) => {
  if (event.target == sizeChartModal) {
    sizeChartModal.style.display = "none";
  } else if (event.target == imageModal) {
    imageModal.style.display = "none";
  }
});

// **Size selection logic**
submitButton.addEventListener("click", () => {
  for (let i = 0; i < radioButtons.length; ++i) {
    if (radioButtons[i].checked) {
      sizeForm.submit();
      return;
    }
  }
  const h3 = document.createElement("h3");
  h3.innerHTML = "<span>x</span> &nbsp;&nbsp;Please Select Size";
  h3.classList.add("select-size-error");
  productInfoContainer.insertBefore(h3, h2BeforeAddCart);
});

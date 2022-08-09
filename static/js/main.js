// tooltips

const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

// tooltips

// popovers

const popoverTriggerList = document.querySelectorAll(
  '[data-bs-toggle="popover"]'
);
const popoverList = [...popoverTriggerList].map(
  (popoverTriggerEl) => new bootstrap.Popover(popoverTriggerEl)
);

// popovers

// hide add to cart alert

const autoHideAlert = () => {
  $("#cart-success-alert").removeClass("show");
  $("#cart-success-alert").addClass("hide");
};

// hide add to cart alert

$(document).ready(() => {
  // add to cart alert

  $("#to-cart").click(() => {
    $("#cart-success-alert").removeClass("hide");
    $("#cart-success-alert").addClass("show");

    setTimeout(autoHideAlert(), 2000);
  });

  $("#close-alert").click(() => {
    $("#cart-success-alert").addClass("hide");
  });

  // add to cart alert

  // back to top button

  $("#back-top").hide();

  $(window).scroll(function () {
    var scroll = $(document).scrollTop();

    if (scroll > 300) {
      $("#back-top").fadeIn();
    } else {
      $("#back-top").fadeOut();
    }
  });

  // back to top button

  // product details navigation

  $("#write-review").hide();
  $("#description").hide();

  $("#reviews-nav").click(() => {
    $("#reviews-nav").addClass("active");
    $("#description-nav").removeClass("active");
    $("#write-review-nav").removeClass("active");

    $("#reviews").fadeIn();
    $("#write-review").hide();
    $("#description").hide();
  });

  $("#description-nav").click(() => {
    $("#reviews-nav").removeClass("active");
    $("#description-nav").addClass("active");
    $("#write-review-nav").removeClass("active");

    $("#reviews").hide();
    $("#write-review").hide();
    $("#description").fadeIn();
  });

  $("#write-review-nav").click(() => {
    $("#reviews-nav").removeClass("active");
    $("#description-nav").removeClass("active");
    $("#write-review-nav").addClass("active");

    $("#reviews").hide();
    $("#write-review").fadeIn();
    $("#description").hide();
  });

  // product details navigation
});

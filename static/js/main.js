$(document).ready(() => {
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

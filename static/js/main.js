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
});

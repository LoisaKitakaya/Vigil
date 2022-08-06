$(document).ready(() => {
  // active navigation links

  $("#dashboard").click(() => {
    $("#dashboard").addClass("active");
    $("#signin").removeClass("active");
    $("#cart").removeClass("active");
  });

  $("#signin").click(() => {
    $("#signin").addClass("active");
    $("#dashboard").removeClass("active");
    $("#cart").removeClass("active");
  });

  $("#cart").click(() => {
    $("#cart").addClass("active");
    $("#signin").removeClass("active");
    $("#dashboard").removeClass("active");
  });

  // active navigation links

  // back to top button

  $("#back-top").hide();

  $(window).scroll(function () {
    var scroll = $(document).scrollTop();

    if (scroll > 100) {
      $("#back-top").fadeIn();
    } else {
      $("#back-top").fadeOut();
    }
  });

  // back to top button
});

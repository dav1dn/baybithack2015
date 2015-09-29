particlesJS.load('particles-js', 'static/js/particles.json', function() { console.log('callback');});

$(function () {
    $.scrollIt({
        easing: 'linear',
        scrollTime: 400,
        activeClass: 'active',
        topOffset: -43
    });
});

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    if (scroll >= 68) {
        $("#navbar").addClass("scrollHeader");
    } else {
        $("#navbar").removeClass("scrollHeader");
    }
});

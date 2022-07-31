function resetState() {
    localStorage.setItem("state", null);
}

function syncState(state) {
    localStorage.setItem("state", JSON.stringify(state));
}

function getState() {
    return JSON.parse(localStorage.getItem("state"));
}



function refresh() {
    $(".grocery-list li").each(function (i) {
        $(this)
            .delay(70 * i)
            .queue(function () {
                $(this).addClass("animated bounceOutLeft");
                $(this).dequeue();
            });
    });

    setTimeout(function () {
        $(".grocery-list li").remove();
        $(".no-items").removeClass("hidden");
        $(".err").addClass("hidden");
    }, 800);
}

$(function () {

    $(".grocery-list").on("click", '.checkbox-mask', function () {
        var li = $(this)
            .parent()
            .parent()
            .parent();
        li.toggleClass("danger");
        li.toggleClass("animated flipInX bounceOutLeft");
        li.attr('id', 'start');

        setTimeout(function () {
            li.removeClass("animated flipInX");
        }, 500);
    });

    $(".grocery-list").on("click", ".close", function () {
        var box = $(this)
            .parent()
            .parent();

        if ($(".grocery-list li").length == 1) {
            box.removeClass("animated flipInX").addClass("animated bounceOutLeft");
            setTimeout(function () {
                box.remove();
                $(".no-items").removeClass("hidden");
                $(".refresh").addClass("hidden");
            }, 500);
        } else {
            box.removeClass("animated flipInX").addClass("animated bounceOutLeft");
            setTimeout(function () {
                box.remove();
            }, 500);
        }

    });


    $(".grocery-list").sortable();
    $(".grocery-list").disableSelection();
});

var todayContainer = document.querySelector(".today");


var d = new Date();


var weekday = new Array(7);
weekday[0] = "Sunday 🖖";
weekday[1] = "Monday 💪😀";
weekday[2] = "Tuesday 😜";
weekday[3] = "Wednesday 😌☕️";
weekday[4] = "Thursday 🤗";
weekday[5] = "Friday 🍻";
weekday[6] = "Saturday 😴";


var n = weekday[d.getDay()];


var randomWordArray = Array(
    "Oh my, it's ",
    "Whoop, it's ",
    "Happy ",
    "Seems it's ",
    "Awesome, it's ",
    "Have a nice ",
    "Happy fabulous ",
    "Enjoy your "
);

var randomWord =
    randomWordArray[Math.floor(Math.random() * randomWordArray.length)];


todayContainer.innerHTML = randomWord + n;

$(document).ready(function () {


    var mins, secs, update;

    init();
    function init() {
        (mins = 25), (secs = 59);
    }


    set();
    function set() {
        $(".mins").text(mins);
    }


    $("#start").on("click", start_timer);
    $("#reset").on("click", reset);
    $("#inc").on("click", inc);
    $("#dec").on("click", dec);

    function start_timer() {

        set();

        $(".dis").attr("disabled", true);

        $(".mins").text(--mins);
        $(".separator").text(":");
        update_timer();

        update = setInterval(update_timer, 1000);
    }

    function update_timer() {
        $(".secs").text(secs);
        --secs;
        if (mins == 0 && secs < 0) {
            reset();
        } else if (secs < 0 && mins > 0) {
            secs = 59;
            --mins;
            $(".mins").text(mins);
        }
    }


    function reset() {
        clearInterval(update);
        $(".secs").text("");
        $(".separator").text("");
        init();
        $(".mins").text(mins);
        $(".dis").attr("disabled", false);
    }


    function inc() {
        mins++;
        $(".mins").text(mins);
    }


    function dec() {
        if (mins > 1) {
            mins--;
            $(".mins").text(mins);
        } else {
            alert("This is the minimum limit.");
        }
    }
});


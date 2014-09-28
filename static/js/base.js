/**
 * Created by Muhammads on 9/28/2014.
 */
function show(dialog) {
    return true;
}

function open(dialog) {
    // add padding to the buttons in firefox/mozilla
    if ($.browser) {

        if ($.browser.mozilla) {
            $('#simplemodal-container .button').css({
                'padding-bottom': '2px'
            });
        }
        // input field font size
        if ($.browser.safari) {
            $('#simplemodal-container .input').css({
                'font-size': '.9em'
            });
        }
    }
    // dynamically determine height
    var h = 280;

    var title = $('#simplemodal-container .title').html();
    $('#simplemodal-container .title').html('Loading...');
    dialog.overlay.fadeIn(200, function () {
        dialog.container.fadeIn(200, function () {
            dialog.data.fadeIn(200, function () {
                $('#simplemodal-container .content').animate({
                    height: h
                }, function () {
                    $('#simplemodal-container .title').html(title);
                    $('#simplemodal-container form').fadeIn(200, function () {
                        $('#simplemodal-container #simplemodal-name').focus();


                    });
                });
            });
        });
    });
}


function close(dialog) {
    try {
        $('#simplemodal-container .message').fadeOut();
        //$('#simplemodal-container').html('Goodbye...');
        $('#simplemodal-container form').fadeOut(200);

        $('#simplemodal-container').animate({
            height: 40
        }, function () {
            dialog.data.fadeOut(200, function () {
                dialog.container.fadeOut(200, function () {
                    dialog.overlay.fadeOut(200, function () {

                        $.modal.close();
                    });
                });
            });
        });
    } catch (ex) {

        alert(ex);
    }


}

$("#add_server").click(function (e) {
    e.preventDefault();

    $.get("/add", function (data) {
        // create a modal dialog with the data
        $.modal(data, {
            closeHTML: "<a href='#' title='Close' class='modal-close'>x</a>",
            escClose: true,
            onOpen: open,
            onShow: show,
            overlayId: 'simplemodal-overlay',
            containerId: 'simplemodal-container',
            onClose: close


        });
    });
});

function auto_refresh(val) {
    xAjax.postWithLoadTarget("/refresh_script/" + val, null,
        $(".divtest"), function (data) {
            if (data.err) {
                console.log("error while refresh" + data.err + data.err_desc);
            }
            else {
                test(val);
            }
        });

}

$("#diable_auto_refresh").click(function (e) {
    e.preventDefault();
    auto_refresh(-1);
});

$(".refresh").each(function (i, v) {

    var $id = $.attr(v, 'id');
    var $rate = $.attr(v, 'rate');

    $("a#" + $id).click(function (e) {
        $("a.refresh").disabled = true;
        e.preventDefault();
        auto_refresh($rate);

    })
});

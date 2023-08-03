$(document).ready(function() {
    $("DIV#add_item").click(function() {
        $("<li>Item</li>").appendTo("UL.my_list");
    });

    $("DIV#remove_item").click(function() {
        $("UL.my_list li").last().remove();
    });

    $("DIV#clear_list").click(function() {
        while ($("UL.my_list li").last().length > 0) {
            $("UL.my_list li").last().remove();
        }
    });
});

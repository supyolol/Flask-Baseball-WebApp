$(document).ready(function(){




$('.somethingroster').on('click',function() {

    var player = $(this).data('id');
    var gameid = $('#gameid').data('id');

    location.href='/playing/'+gameid+'/'+player+'/0'

});


$('.playbtn').on('click',function() {

    var player = $(this).data('id');
    var gameid = $('#gameid').data('id');

    location.href='/playing/'+gameid+'/'+player+'/0'

});






});
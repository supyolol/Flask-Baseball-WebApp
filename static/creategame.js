$(document).ready(function(){

    $('#newGame').on('click',function() {
    
    
        var GameName = $('#GameName').val()
        var GameDate = $('#DateOption1').val()
        var GameLocation = $('#WhereLocation').val()
    
        console.log(GameDate)
            $.ajax({
                url: '/creategame',
                type: 'post',
                data: {
    
                GameName:GameName,
                GameDate:GameDate,
                GameLocation:GameLocation
    
    
                },
                success: function(data){
                    console.log("Didn't Crash! :)")
                    window.location.reload();
                }
    
            });
    
    
    });
    
    
    
    $('.something').on('click',function() {
    
        var gameid = $(this).data('id');
    
        location.href='/select/'+gameid
    
    
    });
    
    
    
    
    });
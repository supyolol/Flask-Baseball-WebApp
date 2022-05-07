



function DEVdrawfromdb(data){

    const fastballimg = document.getElementById('Fastballsource');
    const changeupimg = document.getElementById('ChangeUpsource');
    const curveballimg = document.getElementById('CurveBallsource');



    var canvas = document.getElementById("myCanvas");
    canvas.width = 318;
    canvas.height = 398;

    var ctx = canvas.getContext("2d");
    ctx.lineWidth = 2;
    ctx.strokeRect(62, 67, 198, 264); // inner box
    var ctxmid = canvas.getContext("2d");
    ctxmid.setLineDash([5, 3])
    ctxmid.lineWidth = 1;
    ctxmid.strokeRect(33, 35, 254, 330); // middle box


    for(let y in data){

    var im = new Image();
    var ballindex = data[y].BallIndex
    var balltype = data[y].BallType
    var xcords = data[y].Xcord
    var ycords = data[y].Ycord


    switch (balltype) {
      case 'Fastball':

            ctx.drawImage(fastballimg,xcords,ycords)

            ctx.fillText(ballindex,xcords,ycords)


        break;
      case 'Curve Ball':

            ctx.drawImage(curveballimg,xcords,ycords)

            ctx.fillText(ballindex,xcords,ycords)


        break;
      case 'Change Up':

            ctx.drawImage(changeupimg,xcords,ycords)

            ctx.fillText(ballindex,xcords,ycords)


        break;

      default:
        text = "Looking forward to the Weekend";
}


    }




}




$(document).ready(function(){


    const fastballimg = document.getElementById('Fastballsource');
    const changeupimg = document.getElementById('ChangeUpsource');
    const curveballimg = document.getElementById('CurveBallsource');


//////////////////////////////////////////////////////////////////////////////////////////
////  Buttons Logic
//////////////////////////////////////////////////////////////////////////////////////////


var im = new Image();

var im2 = new Text("None")

var balltypeYo = new Text("None")

balltypeYo = 'None'

var fastball = document.querySelector('#Fastball');

fastball.addEventListener('click', function(event) {

var buttonVAR = $(this).parent().find('#Fastball');
// for change button
var changebutton = document.querySelector('#Change');
var changebuttonparent = changebutton.closest('#Change')

// for curve button
var curvebutton = document.querySelector('#Curve');
var curvebuttonparent = curvebutton.closest('#Curve')

if (buttonVAR.hasClass('btn-outline-danger')) {
     buttonVAR.removeClass('btn-outline-danger');
   }
if ($(changebuttonparent).hasClass('btn-warning')) {
     $(changebuttonparent).removeClass('btn-warning');

   }
if ($(curvebuttonparent).hasClass('btn-success')) {
     $(curvebuttonparent).removeClass('btn-success');

   }

$(changebuttonparent).addClass('btn-outline-warning')
$(curvebuttonparent).addClass('btn-outline-success')
$(this).addClass('btn-danger')

im2 = fastballimg

balltypeYo = "Fastball"


});


var changeup = document.querySelector('#Change');

changeup.addEventListener('click', function(event) {

var buttonVAR = $(this).parent().find('#Change');
if (buttonVAR.hasClass('btn-outline-warning')) {
     buttonVAR.removeClass('btn-outline-warning');
   }

// for fastball button
var fastballbutton = document.querySelector('#Fastball');
var fastballbuttonparent = fastballbutton.closest('#Fastball')

// for curve button
var curvebutton = document.querySelector('#Curve');
var curvebuttonparent = curvebutton.closest('#Curve')

if (buttonVAR.hasClass('btn-outline-warning')) {
     buttonVAR.removeClass('btn-outline-warning');
   }
if ($(fastballbuttonparent).hasClass('btn-danger')) {
     $(fastballbuttonparent).removeClass('btn-danger');

   }
if ($(curvebuttonparent).hasClass('btn-success')) {
     $(curvebuttonparent).removeClass('btn-success');

   }

$(fastballbuttonparent).addClass('btn-outline-danger')
$(curvebuttonparent).addClass('btn-outline-success')
$(this).addClass('btn-warning')



im2 = changeupimg

balltypeYo = "Change Up"




});

var Curve = document.querySelector('#Curve');

Curve.addEventListener('click', function(event) {


var buttonVAR = $(this).parent().find('#Curve');
if (buttonVAR.hasClass('btn-outline-success')) {
     buttonVAR.removeClass('btn-outline-success');
   }

// for fastball button
var fastballbutton = document.querySelector('#Fastball');
var fastballbuttonparent = fastballbutton.closest('#Fastball')

// for curve button
var changebutton = document.querySelector('#Change');
var changebuttonparent = changebutton.closest('#Change')

if (buttonVAR.hasClass('btn-outline-success')) {
     buttonVAR.removeClass('btn-outline-success');
   }
if ($(fastballbuttonparent).hasClass('btn-danger')) {
     $(fastballbuttonparent).removeClass('btn-danger');

   }
if ($(changebuttonparent).hasClass('btn-warning')) {
     $(changebuttonparent).removeClass('btn-warning');

   }

$(fastballbuttonparent).addClass('btn-outline-danger')
$(changebuttonparent).addClass('btn-outline-warning')

$(this).addClass('btn-success')



im2 = curveballimg

balltypeYo = "Curve Ball"

});


var PitchResults = new Text("None")

PitchResults = 'Take'

var SM = document.querySelector('#SM');

SM.addEventListener('click', function(event) {

var buttonVAR = $(this).parent().find('#SM');
var foulbutton = document.querySelector('#Foul');
var foulbuttonparent = foulbutton.closest('#Foul')


if (buttonVAR.hasClass('btn-outline-info')) {
     buttonVAR.removeClass('btn-outline-info');
   }

if ($(foulbuttonparent).hasClass('btn-info')) {
     $(foulbuttonparent).removeClass('btn-info');

   }

$(foulbuttonparent).addClass('btn-outline-info')
$(this).addClass('btn-info')


PitchResults = "SM"

});



var Foul = document.querySelector('#Foul');

Foul.addEventListener('click', function(event) {


var buttonVAR = $(this).parent().find('#Foul');
var SMbutton = document.querySelector('#SM');
var SMbuttonparent = SMbutton.closest('#SM');


if (buttonVAR.hasClass('btn-outline-info')) {
     buttonVAR.removeClass('btn-outline-info');
   }

if ($(SMbuttonparent).hasClass('btn-info')) {
     $(SMbuttonparent).removeClass('btn-info');

   }

$(SMbuttonparent).addClass('btn-outline-info')
$(this).addClass('btn-info')


PitchResults = "Foul"

});

//////////////////////////////////////////////////////////////////////////////////////////
// For AT-BAT RESULTS TOTALS TABLE
//////////////////////////////////////////////////////////////////////////////////////////


    $(document).on('click', '.resultsbtn',function() {

        var countText = ''
        var results = $(this).text()
        var hitstring = "Hit"
        var Outstring = "Out"

        if(results.includes(hitstring)){

            console.log($(this).parent().parent().data('id'))
            countText = $(this).parent().parent().data('id')

        }
        else if(results.includes(Outstring)){

            console.log($(this).parent().parent().data('id'))
            countText = $(this).parent().parent().data('id')

        }
        else{

            countText = results


        }

        var game = $('#gameidheader').data('id');
        var player = $('#playeridheader').data('id');
        var rowid = $('#rowidheader').data('id');
        var resultsvalue = document.querySelector('#selectedResults');
        var CountCell = document.getElementById(countText+"id");
        var TotalCountCell = document.getElementById("Totalid")
        var TotalCountCelltext = document.getElementById("Totalid").textContent
        var IntTotallCountCell = parseInt(TotalCountCelltext)



       $.ajax({
            url: '/updateresultstable',
            type: 'post',
            data: {

            rowid:rowid, // HittervsPitcher Row Id
            results:results,
            game:game,
            player:player,
            countText:countText


            },
            success: function(data){
                console.log("Didn't Crash! :)")
                resultsvalue.textContent = results
                CountCell.textContent = data
                TotalCountCell.textContent = IntTotallCountCell + 1

            }

        });



    });

//////////////////////////////////////////////////////////////////////////////////////////
// End of For AT-BAT RESULTS TOTALS TABLE
//////////////////////////////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////////////////////////////
////  End of Buttons Logic
//////////////////////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////////////////////
////  Hitter vs Pitcher On Click
//////////////////////////////////////////////////////////////////////////////////////////


    //$('.hvprow').on('click',function() {
    $(document).on('click', '.hvprow',function() {


        var rowid = $(this).data('id');

        console.log(rowid)

        var gameid = $('#gameidheader').data('id');

        var playerid = $('#playeridheader').data('id');

        location.href='/playing/'+gameid+'/'+playerid+'/'+rowid


    });



//////////////////////////////////////////////////////////////////////////////////////////
////  End of Hitter vs Pitcher On Click
//////////////////////////////////////////////////////////////////////////////////////////





//////////////////////////////////////////////////////////////////////////////////////////
////  End Game for Player Button
//////////////////////////////////////////////////////////////////////////////////////////

   //$('.hvprow').on('click',function() {
    $(document).on('click', '#EndGameofPlayer',function() {


        var gameid = $('#gameidheader').data('id');

        location.href='/select/'+gameid


    });




//////////////////////////////////////////////////////////////////////////////////////////
////  End of End Game for Player Button
//////////////////////////////////////////////////////////////////////////////////////////




//////////////////////////////////////////////////////////////////////////////////////////
////  Undo Button
//////////////////////////////////////////////////////////////////////////////////////////

    $(document).on('click', '#UndoButton',function() {


       var rowid = $('#rowidheader').data('id');


       $.ajax({
            url: '/undobutton',
            type: 'post',
            data: { rowid:rowid },
            success: function(data){
                console.log("Didn't Crash! :)")
                if (data == 'None'){

                    alert("No More Undos")

                }
                else{
                window.location.reload();
                }


            }

        });



    });




//////////////////////////////////////////////////////////////////////////////////////////
////  End of Undo Button
//////////////////////////////////////////////////////////////////////////////////////////







//////////////////////////////////////////////////////////////////////////////////////////
////  Box Logic
//////////////////////////////////////////////////////////////////////////////////////////

canvas = document.getElementById("myCanvas");

ctx = canvas.getContext("2d");


var myCanvas = document.querySelector('#myCanvas');

var ballcount = HvsPIndex = $('#datatable').children().length;


console.log("Ball Count 1: ", ballcount)

var ballcountDB = $('#lastballstrikecount').data('ball');
var strikecountDB = $('#lastballstrikecount').data('strike');

var ballinoutcount = 0
var strikeinoutcount = 0




if(ballcountDB == 'None'){

ballinoutcount = 0

}
else{

ballinoutcount = ballcountDB

}

if(strikecountDB == 'None'){

strikeinoutcount = 0

}
else{

strikeinoutcount = strikecountDB

}


var vinput =  0



$('#myCanvas').unbind('click');

$(document).on('click','#myCanvas' ,function() {

    var checkifrowselected = $('#rowidheader').data('id')

    if (checkifrowselected == 0){

        alert("You must select a Row in the Hitter-vs-Pitcher before entering data. :)");
        return


    }


    if (balltypeYo == "None"){

        alert("You must select a Ball Type first. :)");
        return


    }


    ballcount++

    var rect = myCanvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;

    console.log(x,y)
    var Xoffset = x - 8
    var Yoffset = y - 10

    ctx.drawImage(im2,Xoffset,Yoffset)

    var XoffsetRounded = Math.round(Xoffset * 100) / 100
    var YoffsetRounded = Math.round(Yoffset * 100) / 100
    console.log("Ball Count 2: ", ballcount)
    ctx.fillText(ballcount,XoffsetRounded,YoffsetRounded)
    if (x < 57 || x > 266){ // true max is 258 and true min is 60
        //console.log("Not in X Zone")
        var inout = "Out"


        }
    else if (y < 63 || y > 341){ // true max is 331 true min is 67
        //console.log("Not in Y Zone")
        var inout = "Out"

        }
    else{

        var inout = "In"
    }

    if ((inout == "Out") && (PitchResults == "Foul") ||
        (inout == "Out") && (PitchResults == "SM") ||
        (inout == "In") && (PitchResults == "Foul") ||
        (inout == "In") && (PitchResults == "SM")){

        strikeinoutcount++

    }
    else if(inout == "In") {

        strikeinoutcount++

    }else if(inout == "Out") {

        ballinoutcount++

    }



    var tableballcount = ballcount


    var rowid = $('#rowidheader').data('id');

    console.log("Inside outter",PitchResults)



    $.ajax({
            url: '/createstatsrow',
            type: 'post',
            data: {

            rowid:rowid, 
            tableballcount:tableballcount,
            balltype:balltypeYo,
            inout:inout,
            PitchResults:PitchResults,
            xcord:XoffsetRounded,
            ycord:YoffsetRounded,
            ballinoutcount:ballinoutcount,
            strikeinoutcount:strikeinoutcount

            },
            success: function(data){

                console.log("Inside Success",PitchResults,balltypeYo)

                $('#exampleModal').modal('show');

                $('#SaveV').unbind('click');

                $('#SaveV').on('click',function() {

                    console.log("yo V!")
                    vinput =  $("#vinput").val()

                    console.log(vinput)

                    $.ajax({
                            url: '/postVinput',
                            type: 'post',
                            data: {

                            rowid:rowid, 
                            tableballcount:tableballcount,
                            vinput:vinput


                            },
                            success: function(data) {
                            console.log("Inside",data)

                            var obj = data

                            document.getElementById("datatable").innerHTML +=
                            "<td>"+tableballcount+"</td><td>"+obj.BallType+"</td><td>"+inout+"</td><td>"+vinput+"</td><td>"+ballinoutcount+"/"+strikeinoutcount+"</td><td>"+obj.pitch_results+"</td>";



                            }
                           })

                });


            },
            complete: function(data){


                // Reset SM and Foul Buttons

                var SMbutton = document.querySelector('#SM');
                var SMbuttonparent = SMbutton.closest('#SM');

                if ($(SMbuttonparent).hasClass('btn-info')) {
                $(SMbuttonparent).removeClass('btn-info');

                }

                $(SMbuttonparent).addClass('btn-outline-info')


                var foulbutton = document.querySelector('#Foul');
                var foulbuttonparent = foulbutton.closest('#Foul')

                if ($(foulbuttonparent).hasClass('btn-info')) {
                    $(foulbuttonparent).removeClass('btn-info');

                }

                $(foulbuttonparent).addClass('btn-outline-info')

                // fastball rest
                var fastballbutton = document.querySelector('#Fastball');
                var fastballbuttonparent = fastballbutton.closest('#Fastball')

                if ($(fastballbuttonparent).hasClass('btn-danger')) {
                    $(fastballbuttonparent).removeClass('btn-danger');

                }
                $(fastballbuttonparent).addClass('btn-outline-danger')
                // Change Up rest
                var changebutton = document.querySelector('#Change');
                var changebuttonparent = changebutton.closest('#Change')
                if ($(changebuttonparent).hasClass('btn-warning')) {
                    $(changebuttonparent).removeClass('btn-warning');

                }
                $(changebuttonparent).addClass('btn-outline-warning')
                // Curve Reset
                var curvebutton = document.querySelector('#Curve');
                var curvebuttonparent = curvebutton.closest('#Curve')
                if ($(curvebuttonparent).hasClass('btn-success')) {
                    $(curvebuttonparent).removeClass('btn-success');

                }
                $(curvebuttonparent).addClass('btn-outline-success')



                balltypeYo = 'None'
                PitchResults = 'Take'










            }

        });






    //////////////////////////////////////////////////////////////////////////////////////////
    ////  Send Data to Table Logic
    //////////////////////////////////////////////////////////////////////////////////////////




});
//////////////////////////////////////////////////////////////////////////////////////////
////  End of Box Logic
//////////////////////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////////////////////
////  Hitter vs Pitcher Table and Buttons
//////////////////////////////////////////////////////////////////////////////////////////


var RightLeftValue = new Text("None")

var leftbtn = document.querySelector('#LeftHandedbtn');

leftbtn.addEventListener('click', function(event) {


RightLeftValue = "Left"


});

var rightbtn = document.querySelector('#RightHandedbtn');

rightbtn.addEventListener('click', function(event) {


RightLeftValue = "Right"


});


HvsPIndex = $('#HitvsPitchtablebody').children().length;


$(document).on('click', '#HitvsPitch',function() {



    HvsPIndex = HvsPIndex + 1
    var gameid = $('#gameidheader').data('id');

    var playerid = $('#playeridheader').data('id');
    console.log("Game ID",gameid)
    console.log("Player ID",playerid)
    console.log("HvP Index",HvsPIndex)
    console.log("RL",RightLeftValue)


    $.ajax({
            url: '/createindexrowleftright',
            type: 'post',
            data: {

            gameid:gameid,
            playerid:playerid,
            HvsPIndex:HvsPIndex,
            RightLeftValue:RightLeftValue


            },
            success: function(data){
                console.log(data)
                document.getElementById("HitvsPitchtablebody").innerHTML += "<td class='hvprow' data-id="+data+">"+HvsPIndex+"</td><td class='hvprow' data-id="+data+">"+RightLeftValue+"</td><td class='hvprow' data-id="+data+">None</td>";
            }

        });






});

//////////////////////////////////////////////////////////////////////////////////////////
////  End of Hitter vs Pitcher Table and Buttons
//////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////
////  Hitter vs Pitcher Toggle button
//////////////////////////////////////////////////////////////////////////////////////////

var ToggleIds = []


$(document).on('click', '.form-check-input',function() {


    var idid = $(this).data('id')
    var ididjson = JSON.parse(idid)
    ToggleIds.push(ididjson)


    //filterfastball




});

$(document).on('click', '.filterbtn',function() {


    var type = $(this).data('id')
    var gameid = $('#gameidheader').data('id');
    var playerid = $('#playeridheader').data('id');

    location.href='/dev?gameid='+gameid+'&playerid='+playerid+'&ToggleIds='+ToggleIds+'&type='+type





    });

//////////////////////////////////////////////////////////////////////////////////////////
////  End of Hitter vs Pitcher Toggle button
//////////////////////////////////////////////////////////////////////////////////////////




});



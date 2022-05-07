



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


//////////////////////////////////////////////////////////////////////////////////////////
////  Go Back Button
//////////////////////////////////////////////////////////////////////////////////////////

  $(document).on('click', '#GoBack',function() {



      var gameid = $('#gameidheader').data('id');

      var playerid = $('#playeridheader').data('id');

      location.href='/playing/'+gameid+'/'+playerid+'/0'


  });



});


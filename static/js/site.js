$(document).ready(function(){
  var cnt=0, length=$(".banner li").length || 0;

  function slide() {
    if (cnt>=length) cnt=0;
    $($(".banner li")[cnt++])
      .fadeIn('slow').animate({opacity: 1.0}, 6000).fadeOut('slow',
       function() {
         return slide()
       }
    );
  }
  if(length>1) slide();
})

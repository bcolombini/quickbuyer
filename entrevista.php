<?php include_once('header.php') ?>
  <div class='row'>
    <div class='col l3 offset-l2 s12' id="alataj">
      <iframe width="100%" height="400" src="http://alataj.com.br/top-5-alataj/burn-residency" frameBorder="0"></iframe>
    </div>
    <div class='col l3 offset-l2 s12' id='containerSoundCloud'>
      <iframe width="100%" height="400" src="https://www.mixcloud.com/widget/iframe/?feed=https%3A%2F%2Fwww.mixcloud.com%2FN%25C3%25A3o_Pare_Na_Pista%2Fn%25C3%25A3o-pare-na-pista-34-bcx%2F&light=1&autoplay=0" frameborder="0"></iframe>
    </div>
  </div>
  <div class='row hide-on-med-and-down' style='min-height:60px'>
    <div class='col s12'></div>
  </div>
  <div class='row '>
    <div class='col s12 final' style='position:fixed;bottom:-7px;padding:0;'>
      <iframe width="100%" height="60" src="https://www.mixcloud.com/widget/iframe/?feed=https%3A%2F%2Fwww.mixcloud.com%2Fbcxbr%2Fbcx-double-colors-set-23052016%2F&hide_cover=1&mini=1&light=1&autoplay=0" frameborder="0"></iframe>
    </div>
  </div>
  <?php
  include_once("footer.php");
  ?>
  <script>
  $(document).ready(function(){
    var pageHeight = -$('.final').height()-$('nav').height()+$(window).height();
    if(pageHeight > 450)
    {
      $('#containerSoundCloud').css({'margin-top':pageHeight/2-225});
      $('#alataj').css({'margin-top':pageHeight/2-225});
    }
    else if(pageHeight > 400)
    {
     $('#containerSoundCloud').css({'margin-top':(pageHeight+$('.final').height)/2-225});
     $('#alataj').css({'margin-top':(pageHeight+$('.final').height)/2-225});
   }

   $('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
    );
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();


 });
</script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-77512812-1', 'auto');
  ga('send', 'pageview');

</script>
</body>
</html>

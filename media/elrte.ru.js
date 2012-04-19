<script type="text/javascript" charset="utf-8">
     $().ready(function() {
         var opts = {
             lang         : 'ru',   // set your language
             styleWithCSS : false,
             height       : 400,
             toolbar      : 'maxi'
         };
         // create editor
         $('#our-element').elrte(opts);

         // or this way
         // var editor = new elRTE(document.getElementById('our-element'), opts);
     });
</script>
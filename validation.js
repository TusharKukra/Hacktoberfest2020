
<script type = "text/javascript">
 

function validate() {
      
    if( document.myForm.username.value == "" ) {
       alert( "Please provide your name!" );
       document.myForm.username.focus() ;
       return false;
    }
    
    if( document.myForm.Enrollment_No.value == "" || isNaN( document.myForm.Enrollment_No.value ) ||
       document.myForm.Enrollment_No.value.length != 5 ) {
       
       alert( "Please provide a Enrollment No ." );
       document.myForm.Enrollment_No.focus() ;
       return false;
    }
      
         var email = document.myForm.EMail.value;
         atpos = email.indexOf("@");
         dotpos = email.lastIndexOf(".");
         
         if (atpos < 1 || ( dotpos - atpos < 2 )) {
            alert("Please enter correct email ID")
            document.myForm.email.focus() ;
            return false;
         }
         return( true );
      }
   

</script>
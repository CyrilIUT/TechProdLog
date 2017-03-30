$(document).ready(function()
{
    $.ajax(
    {
      url:'/activities',
      type:'GET',
      dataType:'json',
      data:'',
      success: function(donnees)
      {
        donnees.activities.forEach(function(donnee) 
        {
          console.log(donnee);
          $("#act").append("<option>"+donnee.label + "</option>");
        });

      },
      error: function(resultat,statut,erreur)
      {
        alert("erreur");
      }
    });
});
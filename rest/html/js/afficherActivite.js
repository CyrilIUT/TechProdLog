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
        $("#act").append("<option value="+donnee.code+">"+donnee.label+" : "+donnee.code+"</option>");
      });

    },
    error: function(resultat,statut,erreur)
    {
      alert("erreur");
    }
  });

  $.ajax(
  {
    url:'/villeActivity/8901',
    type:'GET',
    dataType:'json',
    data:'',
    success: function(donnees)
    {
      $("#vil").html("");
      donnees.villes.forEach(function(donnee) 
      {
        $("#vil").append("<option value="+donnee.nom+">"+donnee.nom+" ("+donnee.codePostal+")</option>");
      });
    },
    error: function(resultat,statut,erreur)
    {
      alert("erreur");
    }
  });

  $('#act').on('change', function() {
    $.ajax(
    {
      url:'/villeActivity/'+this.value,
      type:'GET',
      dataType:'json',
      data:'',
      success: function(donnees)
      {
        $("#vil").html("");
        donnees.villes.forEach(function(donnee) 
        {
          $("#vil").append("<option value="+donnee.nom+">"+donnee.nom+" ("+donnee.codePostal+")</option>");
        });
      },
      error: function(resultat,statut,erreur)
      {
        alert("erreur");
      }
    });
  });

  $('#recherche').on('click', function() {
    $.ajax(
    {
      url:'/installationsVille/'+$("#act").val()+'/'+$("#vil").val(),
      type:'GET',
      dataType:'json',
      data:'',
      success: function(donnees)
      {
        donnees.installations.forEach(function(donnee) 
        {
          $("#resultats").html("");
          $("#resultats").append("<tr><th>Nom de l'installation</th><th>Adresse</th><th>Vue sur la carte</th></tr>");
          $("#resultats").append("<tr><td>"+donnee.nom+"</td><td>"+donnee.adresse+"</td><td id="+donnee.code+"><button class=\"boutonVoirCarte\">Afficher la carte</button><br/><img class=\"carte\" src='https://beta.mapquestapi.com/staticmap/v5/map?locations="+donnee.latitude+","+donnee.longitude+"&key=sW3AW9ZdHwL01qxlAr1iYA8SAqEKQ9fr&zoom=17'/></td></tr>");
        });
        $(".carte").css("display","none");
        $('.boutonVoirCarte').on('click', function() 
        {
          if($(this).text() == "Cacher la carte")
          {
            $(this).html("Afficher la carte");
            $("#"+this.parentNode.id+" img").css("display","none");
          }
          else
          {
            $(this).html("Cacher la carte");
            $("#"+this.parentNode.id+" img").css("display","");
          }
          
        });
      },
      error: function(resultat,statut,erreur)
      {
        alert("erreur");
      }
    });
  });

  
});
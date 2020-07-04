{% load leaflet_tags %}
<html>
  <head>
    {% leaflet_js %}
    {% leaflet_css %}
    <style> 
      .leaflet-container { height: 100%; }
    </style>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>

    {% leaflet_map "main" callback="ourfunction"%}
    <script>
        function ourfunction(map, options){
            var ourdata = "{% url 'data2' %}"
            $.getJSON(ourdata, function(data){
                L.geoJson(data).addTo(map);
            })
        }
    </script>
  </head>
  <body>
    <h1>Map data</h1>
  </body>
</html>
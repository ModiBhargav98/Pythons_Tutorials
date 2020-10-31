function getBathvalue() {
    var uiBathrooms = document.getElementByName("uiBathrooms");
    for(var in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
     return -1;  //Invalid Value
}


function getBHKvalue() {
    var uiBHK = document.getElementByName("uiBHK");
    for(var i in uiBHK) {
        if(uiBHK[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;   //Invalid Value
}


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uisqft");
    var bhk  = getBHKvalue();
    var bathrooms = getBathvalue();
    var location = document.getElementById("uiLocations");
    var estprice = document.getElementById("uiEstimatedPrice")

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft.Value),
        bhk: bhk,
        bath: bathrooms,
        location: location.Value
    },
       function(data, status) {
           console.log(data.estimated_price);
           estprice.innerHTML = "<h2>" + data.estimated_price.toString() + "Lakh</h2>"
       });
    
}



function onPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status){
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocation = document.getElementById("uiLocations");
            $("#uiLocation").empty();
            for(var i in locations){
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;
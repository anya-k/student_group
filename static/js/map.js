/**
 * Created by Anya on 24.12.2015.
 */

window.addEventListener("map:init", function (e) {
    var detail = e.detail;
    //...
    L.marker([50.5, 30.5]).addTo(detail.map);
    //...
}, false);

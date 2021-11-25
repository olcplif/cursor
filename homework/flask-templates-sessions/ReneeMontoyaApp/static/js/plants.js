$(document).ready(function () {
    $.ajax({
        url: '/api/v1/plants',
        method: 'GET',
        success: function (response) {
            for (let plant of response) {
                let el = " <li class='list-group-item'>" + plant.name + "</li>";
                $('#plants-name').append(el);
            }

            for (let plant of response) {
                let el = " <li class='list-group-item'>" + plant.location + "</li>";
                $('#plants-location').append(el);
            }

            for (let plant of response) {
                let el = " <li class='list-group-item'>" + plant.director.name + "</li>";  // Fixed  display director name
                $('#plants-director-id').append(el);
            }
        }
    })
});
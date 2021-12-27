$(document).ready(function () {
    $.ajax({
        url: '/api/v1/plants',
        method: 'GET',
        success: function (response) {
            for (let plant of response) {
                let el = "<li class='list-group-item'>" + "<a href='/plant/" + plant.id + "'>" + plant.name + "</a>" + "</li>";
                $('#plants-name').append(el);
            }

            for (let plant of response) {
                let el = "<li class='list-group-item'>" + plant.location + "</li>";
                $('#plants-location').append(el);
            }

            for (let plant of response) {
                let el = "<li class='list-group-item'>" + "<a href='/employee/" + plant.director.id + "'>" + plant.director.name + "</a>" + "</li>";
                $('#plants-director-id').append(el);
            }
        }
    })
});
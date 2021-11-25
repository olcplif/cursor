$(document).ready(function () {
    $.ajax({
        url: '/api/v1/salons',
        method: 'GET',
        success: function (response) {
            for (let salon of response) {
                let el = " <li class='list-group-item'>" + salon.name + "</li>";
                $('#salons-name').append(el);
            }

            for (let salon of response) {
                let el = " <li class='list-group-item'>" + salon.city + "</li>";
                $('#salons-city').append(el);
            }

            for (let salon of response) {
                let el = " <li class='list-group-item'>" + salon.address + "</li>";
                $('#salons-address').append(el);
            }
            for (let salon of response) {
                let el = " <li class='list-group-item'>" + salon.director.name + "</li>";
                $('#salons-director').append(el);
            }
        }
    })
});
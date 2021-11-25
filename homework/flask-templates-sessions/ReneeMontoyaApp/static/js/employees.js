$(document).ready(function () {
    $.ajax({
        url: '/api/v1/employees',
        method: 'GET',
        success: function (response) {
            for (let employee of response) {
                let el = " <li class='list-group-item'>" + employee.name + "</li>";
                $('#employees-name').append(el);
            }

            for (let employee of response) {
                let el = " <li class='list-group-item'>" + employee.email + "</li>";
                $('#employees-email').append(el);
            }

            for (let employee of response) {
                let el = " <li class='list-group-item'>" + employee.department_type + "</li>";
                $('#employees-department-type').append(el);
            }
        }
    })
});
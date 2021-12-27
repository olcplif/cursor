$(document).ready(function () {
    $.ajax({
        url: '/api/v1/employees',
        method: 'GET',
        success: function (response) {
            for (let employee of response) {
                let el = "<li class='list-group-item'>" + "<a href='/employee/" + employee.id + "'>" + employee.name + "</a>" + "</li>";
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

            for (let employee of response) {
                if (employee.department_type === "plant"){
                    let el = "<li class='list-group-item'>" + "<a href='/plant/" + employee.department_id + "'>" + employee.department + "</a>" + "</li>";
                    $('#employees-department').append(el);
                }
                else {
                    let el = "<li class='list-group-item'>" + "<a href='/salon/" + employee.department_id + "'>" + employee.department + "</a>" + "</li>";
                    $('#employees-department').append(el);
                }
                // let el = " <li class='list-group-item'>" + employee.department + "</li>";
            }
        }
    })
});
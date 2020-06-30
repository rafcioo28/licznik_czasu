import $ from 'jquery';
window.jQuery = $;
window.$ = $;
import 'bootstrap';
import './scss/style.scss';


$(document).ready(function () {
    $('#myModal').on('show.bs.modal', function (e) {
        var button = $(e.relatedTarget)
        var id_person = button.data('id_person')

        $.ajax({
            type: 'GET',
            url: '/api/person/' + id_person + '/',
            dataType: 'json',
            success: function (data) {
                $('#id_person_ajx').val(data.id)
                $('#last_name_ajx').val(data.last_name)
                $('#first_name_ajx').val(data.first_name)
                $('#type_of_person_ajx').val(data.type_of_person)
                $('#id_family_ajx').val(data.family)
            },
            error: function () {
                $('#errors').val(`error`);
            }
        });

        var modal = $(this)
        modal.find('#person_id').text('Osoba ID ' + id_person)
    })
    $('#save_button').on('click', function () {
        var id_person = $('#id_person_ajx').val()

        $.ajax({
            type: 'POST',
            url: '/api/person/' + id_person + '/',
            data: {
                last_name: $('#last_name_ajx').val(),
                first_name: $('#first_name_ajx').val(),
                type_of_person: $('#type_of_person_ajx').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post',
            },
            success: function () {
                window.location.reload(false);
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            },
        })

    })
})
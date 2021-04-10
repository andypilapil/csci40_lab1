$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal .modal-content").html("");
        $("#modal").modal("show");
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#table tbody").html(data.html_list);
          $("#modal").modal("hide");
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create key
  $(".js-create-key").click(loadForm);
  $("#modal").on("submit", ".js-key-create-form", saveForm);

  // Edit key
  $("#table").on("click", ".js-edit-key", loadForm);
  $("#modal").on("submit", ".js-key-edit-form", saveForm);

  // Delete key
  $("#table").on("click", ".js-delete-key", loadForm);
  $("#modal").on("submit", ".js-key-delete-form", saveForm);

  // Create this week item
  $(".js-create-this_week").click(loadForm);
  $("#modal").on("submit", ".js-this_week-create-form", saveForm);

  // Edit this week item
  $("#table").on("click", ".js-edit-this_week", loadForm);
  $("#modal").on("submit", ".js-this_week-edit-form", saveForm);

  // Delete this week item
  $("#table").on("click", ".js-delete-this_week", loadForm);
  $("#modal").on("submit", ".js-this_week-delete-form", saveForm);

  // Create today item
  $(".js-create-today").click(loadForm);
  $("#modal").on("submit", ".js-today-create-form", saveForm);

  // Edit today item
  $("#table").on("click", ".js-edit-today", loadForm);
  $("#modal").on("submit", ".js-today-edit-form", saveForm);

  // Delete today item
  $("#table").on("click", ".js-delete-today", loadForm);
  $("#modal").on("submit", ".js-today-delete-form", saveForm);

  $("#table").on("submit", ".js-markasdone-this_week", saveForm);
});

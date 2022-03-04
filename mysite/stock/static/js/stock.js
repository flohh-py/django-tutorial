$(document).ready(function() {
  $("#id_item").select2({
    dropdownParent: $('#itemModal'),
    ajax: {
      url: "/product/",
      dataType: "json",
      processResults: function(data) {
        return {
          results: $.map(data, function(r) {
            return { id: r.id, text: r.code };
          })
        };
      },
    },
    minimumInputLength: 2
  });
  $("#id_item").on("select2:select", function(e) {
    $.ajax({
      type: "GET",
      url: "/product/detail/" + $("#id_item").select2('data')[0].id
    }).then(function(data) {
      $("#id_qty").val(1.0)
      $("#id_price").val(data.price)
    })
  })
});
function edit_line(id) {
  $.get("/stock/edit_line/" + id, function(data) {
    $("#item-modal-content").html(data)
  })
  $("#itemModal").modal("toggle");
}
function add_line(id) {
  $.get("/stock/add_line/", function(data) {
    $("#item-modal-content").html(data)
    $("#id_parent").val(id) //gambiarra?
  })
  $("#itemModal").modal("toggle");
}
function delete_line(id) {
  $.get("/stock/delete_line/" + id, function(data) {
    $("#item-modal-content").html(data)
  })
  $("#itemModal").modal("toggle");
}

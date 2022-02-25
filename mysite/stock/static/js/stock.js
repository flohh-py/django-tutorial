$(document).ready(function() {
  $("#id_item").select2({
    dropdownParent: $('#itemAddModal'),
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
function edit(id) {
  $.get("/stock/edit_line/" + id, function(data) {
    $("#modal-edit-line-body").html(data)
  })
  $("#itemEditModal").modal("toggle");
}

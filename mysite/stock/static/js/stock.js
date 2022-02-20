$(document).ready(function() {
  $("#id_product").select2({
    dropdownParent: $('#prodAddModal'),
    ajax: {
      url: "/product/",
      dataType: "json",
      processResults: function(data) {
        return {
          results: $.map(data, function(r) {
            return { id: r.id, text: r.code };
          })
        };
      }
    },
    minimumInputLength: 2
  });
});

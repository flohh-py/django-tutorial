$(document).ready(function() {
  $("#id_item").select2({
    dropdownParent: $('#itemModal'),
    ajax: {
      url: "/invoice/",
      dataType: "json",
      processResults: function(data) {
        return {
          results: $.map(data, function(r) {
            return { id: r.id, text: r.code };
          })
        };
      }
    },
    minimumInputLength: 1
  });
  $("#id_item").on("select2:select", function(e) {
    $.ajax({
      type: "GET",
      url: "/invoice/detail/" + $("#id_item").select2('data')[0].id
    }).then(function(data) {
      $("#id_outstanding").val(data.outstanding)
      $("#id_total").val(data.total)
    })
  })
  $("#id_partner").select2({
    // dropdownParent: $('#itemAddModal'),
    ajax: {
      url: "/partner/",
      dataType: "json",
      data: function name(params) {
        invo_type = $("#id_type").val()
        return {
          type: invo_type,
          term: params.term
        }
      },
      processResults: function(data) {
        return {
          results: $.map(data, function(r) {
            return { id: r.id, text: r.name };
          })
        };
      }
    },
    minimumInputLength: 2
  });
});
function edit_line(id) {
  $.get("/payment/edit_line/" + id, function(data) {
    $("#item-modal-content").html(data)
  })
  $("#itemModal").modal("toggle");
}
function add_line(id) {
  $.get("/payment/add_line/", function(data) {
    $("#item-modal-content").html(data)
    $("#id_parent").val(id) //gambiarra?
  })
  $("#itemModal").modal("toggle");
}
function delete_line(data) {
  $.ajax({
    url: "/payment/delete_line/" + data['id'],
    type: "POST",
    headers: { "X-CSRFToken": data['token'] },
  }).then(
    location.reload()
  )
  // $("#itemModal").modal("toggle");
}
function create_ste(invo_id) {
  // $("#itemModal").modal("toggle");
  $.get("/payment/create_stockentry/" + invo_id, function(data) {
    $("#item-modal-content").html(data)
  })
  // $("#itemModal").modal("toggle");
}
function list_ste(invo_id) {
  $.get("/payment/list_stockentry/" + invo_id, function(data) {
    $("#item-modal-content").html(data)
    // $("#item-modal-content").modal({ backdrop: 'static', keyboard: false })
  })
  $("#itemModal").modal("toggle");
}

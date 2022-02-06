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
  // $("#id_invoice-0-product").select2({
  //   ajax: {
  //     url: "/product/",
  //     dataType: "json",
  //     processResults: function(data) {
  //       return {
  //         results: $.map(data, function(r) {
  //           return { id: r.id, text: r.code };
  //         })
  //       };
  //     }
  //   },
  //   minimumInputLength: 2
  // });
  // $("#add-new").click(function(event) {
  //   if (event) {
  //     event.preventDefault()
  //   }
  //   let targetForm = $("#line-form-list")
  //   let countFrom = $(".line-form").length
  //   let emptyForm = $("#empty-form").clone(true)

  //   emptyForm.removeAttr('data-select2-id')
  //   emptyForm.removeAttr('id')
  //   emptyForm.find('option').removeAttr('data-select2-id')
  //   emptyForm.find('span').remove()

  //   emptyForm.attr("class", "line-form");
  //   emptyForm.attr("id", "line-form-" + countFrom);

  //   let regex = new RegExp("__prefix__", "g")
  //   let rep = emptyForm.html();
  //   emptyForm.html(rep.replace(regex, countFrom))
  //   $("#id_invoice-TOTAL_FORMS").attr("value", countFrom + 1)
  //   targetForm.append(emptyForm)

  //   $(`#id_invoice-${countFrom}-product`).select2({
  //     ajax: {
  //       url: "/product/",
  //       dataType: "json",
  //       processResults: function(data) {
  //         return {
  //           results: $.map(data, function(r) {
  //             return { id: r.id, text: r.code };
  //           })
  //         };
  //       }
  //     },
  //     minimumInputLength: 2
  //   });
  // });
});

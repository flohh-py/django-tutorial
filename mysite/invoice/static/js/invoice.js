$(document).ready(function() {
  // $("#id_invoice-0-product").select2({
  //   ajax: {
  //     url: "{% url 'product:list' %}",
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
  $("#add-new").click(function(event) {
    if (event) {
      console.log("TEST")
    }
    const targetForm = $("#line-form-list")
    const countFrom = $(".line-form").length
    const emptyForm = $("#empty-form").clone()
    emptyForm.attr("class", "line-form");
    const regex = new RegExp("__prefix__", "g")

    var rep = emptyForm.html();
    emptyForm.html(rep.replace(regex, countFrom))
    $("#id_invoice-TOTAL_FORMS").attr("values", countFrom + 1)
    targetForm.append(emptyForm)
  });
});

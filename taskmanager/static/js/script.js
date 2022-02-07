document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    //date pickers
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd, mmmm, yyyy",
      i18: {done: "Select"}
    });

    //dropdown select
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);

    // toggle tasks description
    var collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse);

});

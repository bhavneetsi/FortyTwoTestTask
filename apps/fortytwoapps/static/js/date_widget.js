$(document).ready(function () {
$("#id_dateofbirth").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "yy-mm-dd",
        yearRange: "1700:2100"
    });
});
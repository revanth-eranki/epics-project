<script>
    // Get the current URL path
    var path = window.location.pathname;

    // Find the corresponding nav link and mark it as active
    $('.nav-pills a').each(function() {
        var href = $(this).attr('href');
        if (path === href) {
            $(this).addClass('active');
        }
    });
</script>

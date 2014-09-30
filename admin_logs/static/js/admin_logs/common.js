!function($) {
    $(document).ready(function(){
        $('.admin-logs-collapsed,.admin-logs-expanded').click(function(){
            var $this = $(this);
            if ($this.hasClass('admin-logs-collapsed')) {
                $this.addClass('admin-logs-expanded');
                $this.removeClass('admin-logs-collapsed')
            } else {
                $this.addClass('admin-logs-collapsed');
                $this.removeClass('admin-logs-expanded')
            }
            return false;
        });
    });
}(django.jQuery);

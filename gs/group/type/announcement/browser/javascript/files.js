jQuery.noConflict();
jQuery(document).ready( function () {
    // HACK to get the group ID for the AJAX.
    var bodyId = null;
    var gId = null;
    var e = /_.*$/;
    var filesSearch = null;
    var d = null;
    var show_files = null;

    bodyId = jQuery('body').attr('id');
    gId = String(e.exec(bodyId)).slice(1);
    d = {'g': gId, 't': '0', 'f': '1'};
    filesSearch = GSSearch('#gs-group-messages-files-search',
		           '/s/search.ajax', 0, 6, d, null);

    show_files = function(event, ui) {
        var panel = jQuery(ui.panel);
        if ((panel.attr('id') ===  'task-tab-1') && 
            (!filesSearch.results_shown())) {
	    filesSearch.load();
	}
    };
    jQuery('#task-tabs').bind('tabsshow', show_files);
});

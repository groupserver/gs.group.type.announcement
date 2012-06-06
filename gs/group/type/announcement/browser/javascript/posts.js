jQuery.noConflict();
jQuery(document).ready( function () {
    // HACK to get the group ID for the AJAX.
    var bodyId = null;
    var gId = null;
    var e = /_.*$/;
    var postsSearch = null;

    bodyId = jQuery('body').attr('id');
    gId = String(e.exec(bodyId)).slice(1);

    postsSearch = GSSearch('#gs-group-type-announcement-posts',
                           '/s/search.ajax', 0, 6, 
                           {'t': '0', 'p': '1', 'g': gId}, null);
    postsSearch.load();
});

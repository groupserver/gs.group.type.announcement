jQuery.noConflict();

function gs_group_type_announcement_posts() {
    // HACK to get the group ID for the AJAX.
    var bodyId = null, gId = null, e = /_.*$/,  postsSearch = null;

    bodyId = jQuery('body').attr('id');
    gId = String(e.exec(bodyId)).slice(1);

    postsSearch = GSSearch('#gs-group-type-announcement-posts',
                           '/s/search.ajax', 0, 6, 
                           {'t': '0', 'p': '1', 'g': gId}, null);
    postsSearch.load();
    jQuery('#gs-group-messages-base-tabs-buttons li:first-child a').click();
}

jQuery(document).ready( function () {
    gsJsLoader.with_module('/++resource++gs-search-base-js-min-20121217.js', 
                           gs_group_type_announcement_posts);
});

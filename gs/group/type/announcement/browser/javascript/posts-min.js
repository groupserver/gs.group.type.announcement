jQuery.noConflict();function gs_group_type_announcement_posts(){var b=null,a=null,c=/_.*$/,d=null;
b=jQuery("body").attr("id");a=String(c.exec(b)).slice(1);d=GSSearch("#gs-group-type-announcement-posts","/s/search.ajax",0,6,{t:"0",p:"1",g:a},null);
d.load();jQuery("#gs-group-messages-base-tabs-buttons li:first-child a").click()}jQuery(document).ready(function(){gsJsLoader.with_module("/++resource++gs-search-base-js-min-20121217.js",gs_group_type_announcement_posts)
});
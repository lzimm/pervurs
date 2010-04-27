var podActive = null;

var podSelected = false;

function podDrop(pod) {
	if (podActive) {
	    $("#top_pod_drop").removeClass(podActive);
		$("#top_pod_drop_" + podActive).hide();
	}
	
	podActive = pod;
	$("#top_pod_drop_" + podActive).show();
	$("#top_pod_drop").show();
	$("#top_pod_drop").addClass(pod);
	$("#top_search_drop").hide();
	
	podSelected = true;
}

function podClear() {
    podSelected = false;
    
    setTimeout(function() {
        if (!podHover && !podSelected) {
    		$("#top_pod_drop").hide();
    	}
    }, 250);
}

var podHover = false;

function podFocus() {
	podHover = true;
}

function podBlur() {
	podHover = false;
	podClear();
}

var podLoginContainerTypes = {}

function podSetLoginType(type, container) {
    podLoginContainerTypes[container] = type;
    
    switch(type) {
        case 'login':
            $('#top_pod_drop_' + container + ' .top_pod_drop_username').hide();
            $('#top_pod_drop_' + container + ' .top_pod_drop_email').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_website').hide();
            $('#top_pod_drop_' + container + ' .top_pod_drop_password').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_password_confirm').hide();
        break;

        case 'register':
            $('#top_pod_drop_' + container + ' .top_pod_drop_username').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_email').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_website').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_password').show();
            $('#top_pod_drop_' + container + ' .top_pod_drop_password_confirm').show();
        break;
    }
    
    $('#top_pod_drop_' + container).find(':radio').each(function (i) {
        this.checked = this.value == type;
    });
}

function podLogin(container) {
    var name             = $('#top_pod_drop_' + container + ' .top_pod_drop_username:first input:first').val();
    var email            = $('#top_pod_drop_' + container + ' .top_pod_drop_email:first input:first').val();
    var password         = $('#top_pod_drop_' + container + ' .top_pod_drop_password:first input:first').val();
    var password_confirm = $('#top_pod_drop_' + container + ' .top_pod_drop_password_confirm:first input:first').val();

    switch (podLoginContainerTypes[container]) {
        case 'login':
            qonvo.login(email, password);
        break;
        
        case 'register':
            qonvo.register(name, email, password, password_confirm)
        break;
    }
}

podSetLoginType('login', 'social');
podSetLoginType('login', 'post');

function qonvo_post_auth() {    
    if (qonvo.uid == null) {
        $("#top_pod_drop").removeClass("auth");
        $('.top_pod_drop_content').hide();
        $('.top_pod_drop_login').show();
    } else {
        $("#top_pod_drop").addClass("auth");
        $('.top_pod_drop_content').show();
        $('.top_pod_drop_login').hide();

        $('.top_pod_drop_content').html('<ul></ul>');
        
        /*
        qonvo.request('getposts', [qonvo.uid], function(res) {
            if (res.title) {
                var html = "<li><a href='" + res.ref.replace("/chan/", "http://") + "' target='_blank'>" + res.title + "</a></li>";
                $('#top_pod_drop_post .top_pod_drop_content ul').append(html);
            }
        });
        
        qonvo.request('getresponders', [qonvo.uid], function(res) {
            console.log(res);
            if (res.name) {
                var html = "<li><a href='javascript:qonvo.whois(\"" + res.id + "\");'>" + res.name + "</a></li>";
                $('#top_pod_drop_social .top_pod_drop_content ul').append(html);
            }            
        });
        */
    }
}

var autoCompleteHistory = null;
function autoComplete(word) {
	if (word == autoCompleteHistory) {
		return;
	}
	
	if (word.length < 1) {
	    searchDropClear();
	}
		
	autoCompleteHistory = word;
	
	$.getJSON("/async/search/suggest", {'q':word}, function(res) {
		var html = "<ul>";
		for (var i in res) {
		    var val = res[i];
		    
			html += "<li onclick=\"$('#top_search_q').val('" + val + "'); $('#top_search_q').focus();\"><a href='javascript:void(0);'>";
			html += val
			html += "</a></li>";
		}
		html += "</ul>";
		
		$("#top_search_drop_content").html(html);
		$("#top_search_drop").show();
	});
}

function searchDropClear() {
    searchDropActive = false;
    
    setTimeout(function() {
        if (!searchDropHover) {
    		$("#top_search_drop").hide();
    	}
    }, 250);
}

var searchDropHover = false;

function searchDropFocus() {
	searchDropHover = true;
}

function searchDropBlur() {
	searchDropHover = false;
	searchDropClear();
}
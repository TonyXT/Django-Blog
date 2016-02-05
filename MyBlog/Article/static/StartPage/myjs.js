/**
 * Created by tangni on 1/20/16.
 */
jQuery(document).ready(function(){
    var $form_modal = $('.cd-user-modal')
    var $form_login = $form_modal.find('#cd-login'),
	    $form_signup = $form_modal.find('#cd-signup'),
		$form_modal_tab = $('.cd-switcher'),
		$tab_login = $form_modal_tab.children('li').eq(0).children('a'),
		$tab_signup = $form_modal_tab.children('li').eq(1).children('a')


    $("#signin").click(function(event){
      $form_modal.addClass('is-visible');
      login_selected();
    })

    $("#signup").click(function(event){
        $form_modal.addClass('is-visible');
        signup_selected();
    })

    $($form_modal).on('click', function(event){
        if( $(event.target).is($form_modal) || $(event.target).is('.cd-close-form') ) {
            $form_modal.removeClass('is-visible');
        }
    });
    	$(document).keyup(function(event){
    	if(event.which=='27'){
    		$form_modal.removeClass('is-visible');
	    }
    });


        $($form_modal_tab).on('click', function(event) {
        event.preventDefault();
        ( $(event.target).is( $tab_login ) ) ? login_selected() : signup_selected();
    });

    function login_selected(){
        $form_login.addClass('is-selected');
        $form_signup.removeClass('is-selected');
        $tab_login.addClass('selected');
        $tab_signup.removeClass('selected');
    }

    function signup_selected(){
        $form_login.removeClass('is-selected');
        $form_signup.addClass('is-selected');
        $tab_login.removeClass('selected');
        $tab_signup.addClass('selected');
    }
})
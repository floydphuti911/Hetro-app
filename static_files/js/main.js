
$(document).ready(function(){
new UISearch( document.getElementById( 'sb-search' ) );
});

	$(function(){
	  $('#audio-player').mediaelementplayer({
		alwaysShowControls: true,
		features: ['prevtrack', 'playpause', 'nexttrack', 'current', 'progress', 'duration', 'volume', 'playlist', 'shuffle', 'loop'],
		audioVolume: 'horizontal',
		iPadUseNativeControls: true,
		iPhoneUseNativeControls: true,
		AndroidUseNativeControls: true
	});
 });




$(function () {
  // Slideshow 4
  $("#slider4").responsiveSlides({
	auto: true,
	pager:true,
	nav:true,
	speed: 500,
	namespace: "callbacks",
	before: function () {
	  $('.events').append("<li>before event fired.</li>");
	},
	after: function () {
	  $('.events').append("<li>after event fired.</li>");
	}
  });

});




$(document).ready(function() {
$('.popup-with-zoom-anim').magnificPopup({
	type: 'inline',
	fixedContentPos: false,
	fixedBgPos: true,
	overflowY: 'auto',
	closeBtnInside: true,
	preloader: false,
	midClick: true,
	removalDelay: 300,
	mainClass: 'my-mfp-zoom-in'
});
});
	



$(document).ready(function(){

new jPlayerPlaylist({
	jPlayer: "#jquery_jplayer_1",
	cssSelectorAncestor: "#jp_container_1"
}, [
	
	{
		title:"1. Ellie-Goulding",
		artist:"",
		webmv: "/static/video/Ellie-Goulding.webm",
		poster:"/static/video/play1.png"
	},
	{
		title:"2. Mark-Ronson-Uptown",
		artist:"",
		mp4: "/static/video/Mark-Ronson-Uptown.mp4",
		ogv: "/static/video/Mark-Ronson-Uptown.ogv",
		webmv: "/static/video/Mark-Ronson-Uptown.webm",
		poster:"/static/video/play2.png"
	}
], {
	swfPath: "../../dist/jplayer",
	supplied: "webmv,ogv,mp4",
	useStateClassSkin: true,
	autoBlur: false,
	smoothPlayBar: true,
	keyEnabled: true
});

});




$(window).load(function() {
              
              $("#flexiselDemo1").flexisel({
                visibleItems: 5,
                animationSpeed: 1000,
                autoPlay: true,
                autoPlaySpeed: 3000,        
                pauseOnHover: false,
                enableResponsiveBreakpoints: true,
                responsiveBreakpoints: { 
                  portrait: { 
                    changePoint:480,
                    visibleItems: 2
                  }, 
                  landscape: { 
                    changePoint:640,
                    visibleItems: 3
                  },
                  tablet: { 
                    changePoint:800,
                    visibleItems: 4
                  }
                }
              });
              });
          	

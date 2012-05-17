#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import logging

def PageFooter(val):
  footer_text = """ <div id="footer">
		<div>
			<div class="first">
				<h3>Reach us at:</h3>
				<div>
					<p>Telephone. : <span><b>+91-124-4257924</span></b></p>

					<p>Email : <span><b>futureinframail@gmail.com</span></b></p>
				</div>
			</div>

			<div>
				<h3>Get Social with us!</h3>
				<p> </p>
				<div>
					<a href="https://www.facebook.com/pages/Future-Infra-Enterprise/222378047828885" class="facebook" target="_blank"></a>
					<a href="http://twitter.com" class="twitter" target="_blank"></a>
					<a href="#" class="linked-in"></a>
				</div>
			</div>

			<div>
				<h3>Subscribe to latest feeds!</h3>
				<p> If you would like to receive latest news
				about the company, please subscribe by providing
				your email address.
				<form>
					<input type="text" id="subscribe" maxlength="100" value="email address" />
					<button class="btn primary" type="submit" id="btnSubscribe"> Submit </button>
				</form>
			</div>
		</div>

			<div align="center">
				<br>
				<br>
				<p>Copyright &copy; 2012 FutureInfra Enterprises. All Rights reserved.</p>
			</div>
	</div>

	<!-- Modal for Feedback -->
	<div id="feedback-modal" class="modal hide fade">
		<div class="modal-header">
			<a href="#" class="close">x</a>
			<h3>We would love to hear your feedback</h3>
		</div>

		<div class="modal-body span9" align="left">
			<div class="row">
				<div class="span9 errorTxt clearfix" style="display:none" id="regError">
				</div>
			</div>

			<input class="span5 clearField clearFieldBlurred" id="txtFeedName" name="feedName" type="text" value="Name">
			<br> <br>
			<input class="span8 clearField clearFieldBlurred" id="txtFeedEmail" name="feedEmail" type="text" value="Email address">
			<br> <br>
			<input class="span8 clearField clearFieldBlurred" id="txtFeedPhone" name="feedPhone" type="text" value="Phone number">
			<br> <br>
			<textarea rows="10" cols="100" class="span8 clearField clearFieldBlurred" id="txtFeedComment"
				name="feedComment"> Your feedback here... </textarea>


			<div class="modal-footer">
        <div class="span1">
          <img src="../static/images/spinner.gif" id="submitSpinner" style="display:none">
        </div>
				<button type="submit" id="feedSubmitBtn" class="btn primary" onclick="SendFeedback()"> Submit</button>
				<a onclick=CloseFeedbackModal() class="btn secondary">Cancel</a>
			</div>
		</div>
	</div>
</body>
</html>
	<!-- Modal for Feedback ends --> """
  return footer_text

def PageHeader(page):
  empty_class = " "
  current_class = "class = 'current'"

  header_text = """ <!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" />
	<title>Future Infra</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css" />
	<link href="../static/bootstrap.css?v=1" rel="stylesheet">
	<!--[if IE 9]>
		<link rel="stylesheet" type="text/css" href="../static/ie9.css" />
	<![endif]-->
	<!--[if IE 8]>
		<link rel="stylesheet" type="text/css" href="../static/ie8.css" />
	<![endif]-->
	<!--[if IE 7]>
		<link rel="stylesheet" type="text/css" href="../static/ie7.css" />
	<![endif]-->

	<script type="text/javascript" src="../static/jquery.1.6.4.min.js"></script>
	<script type="text/javascript" src="../static/jquery.cookie.js"></script>
	<script type="text/javascript" src="../static/bootstrap-dropdown.js"></script>
	<script type="text/javascript" src="../static/bootstrap-modal.js"></script>

	<script type="text/javascript">

	function SendFeedback()
  {
      $('#infoLbl').hide();
      var submitBtn = $("#feedSubmitBtn");
      $('#submitSpinner').show();
      submitBtn.attr('disabled', 'disabled');

      var name = $("#txtFeedName").val();
      var email = $("#txtFeedEmail").val();
      var phone = $("#txtFeedPhone").val();
      var comment = $("#txtFeedComment").val();

      $.ajax({
    url: "/feedback",
    type: "GET",
    dataType: "jsonp",
    data: {
      "name": name,
      "email": email,
      "phone": phone,
      "comment": comment
    },

    success: function(data) {
      if (data.success === true) {
        $('#msgbox').fadeIn("slow");
      }
      else {
      }
    },
    error: function(jqXHR) {
        $('#msgbox').fadeIn("slow");
		     $("#feedback-modal").modal("hide");
         $('#regSpinner').hide();
         submitBtn.removeAttr('disabled');
    }

    });
  }

	function CloseFeedbackModal()
	{
      $('#submitSpinner').show();
		  $("#feedback-modal").modal("hide");
	}

	</script>

</head>
<body>
	<div id="header">
		<div>
			<div id="logo">
        <a href="/"><img width="150" src="../static/images/logo.png" alt="Logo" /></a>
			</div>
			<div id="navigation">
				<div>
					<ul>
						<li %s style="line-height:50px"><a href="/">Home</a></li>
						<li %s style="line-height:50px"><a href="/profile">Profile</a></li>
						<li %s style="line-height:50px"><a href="/aboutus">Team</a></li>
						<li %s style="line-height:50px"><a href="/projects">Projects</a></li>
						<li %s style="line-height:50px"><a href="/services">Services</a></li>
						<li %s style="line-height:50px"><a href="/dealers">Dealerships</a></li>
						<li style="line-height:50px"><a href="#" data-controls-modal="feedback-modal" data-backdrop="true">Feedback</a><li>
					</ul>
				</div>
			</div>
		</div>
	</div>

  <div class="alert-message success fade in" id="msgbox"  style="display:none" align="center"> Thank you for submitting your valuable feedback.</div>
  """ % (current_class if page == "home" else empty_class,
      current_class if page == "profile" else empty_class,
      current_class if page == "aboutus" else empty_class,
      current_class if page == "projects" else empty_class,
      current_class if page == "services" else empty_class,
      current_class if page == "dealers" else empty_class
      )

  return header_text


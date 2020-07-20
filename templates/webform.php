{% extends 'layout.html' %}

{% block body %}
<?php
    $message_sent= false;

    if(isset($_POST['email']) && $_POST['email'] != ''){

        if( filter_var($_POST['email'], FILTER_VALIDATE_EMAIL))

        $userName = $_POST['name'];
        $userEmail = $_POST['email'];
        $messageSubject = $_POST['subject'];
        $message = $_POST['message'];

        $to = "eddiebrett@hotmail.co.uk";
        $subject = "website message";
        $body = "";

        $body .= "From: ".$userName. "\r\n";
        $body .= "Email: ".$userEmail. "\r\n";
        $body .= "Message: ".$message. "\r\n";

        mail($to,$subject,$body);

        $message_sent= true;
}
    
?>


<div class="contact_container">

<?php
    if($message_sent):
?>
    <h3>Thanks we'll be in touch</h3>

<?php
    else:
?>

		<div class="contact-box">
			<div class="left">
            <br><br>
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2481.848276563022!2d-0.058115084784400556!3d51.534342616554746!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761cdd09f30e0f%3A0x839b8c83f7470e1e!2s10%2C%2049%20Mowlem%20St%2C%20London%20E2%209HE!5e0!3m2!1sen!2suk!4v1594825836916!5m2!1sen!2suk"  frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe><br><br>
            Unit 10,<br>

49 Mowlem Street,<br>

London<br>

E2 9HE<br><br>
Tel: 0208 980 8583

            </div>
            
			<div class="right">
				<h2>Contact Us</h2>
                <form action="webform.php" method="POST" class="form">
            <div class="form-group">
                <label for="name" class="form-label">Your Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="Enter name" tabindex="1" required>
            </div>
            <div class="form-group">
                <label for="email" class="form-label">Your Email</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Enter email" tabindex="2" required>
            </div>
            <!-- <div class="form-group">
                <label for="subject" class="form-label">Subject</label>
                <input type="text" class="form-control" id="subject" name="subject" placeholder="Hello There!" tabindex="3" required>
            </div> -->
            <div class="form-group">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" rows="5" cols="50" id="message" name="message" placeholder="Enter Message..." tabindex="4"></textarea>
            </div>
            <div>
                <button type="submit" class="btn">Send Message!</button>
            </div>
        </form>
                <!-- <form action="webform.php" method="POST">
				<input name="name" type="text" class="field" placeholder="Your Name">
				<input name="email" type="text" class="field" placeholder="Your Email">
				<input name="phone" type="text" class="field" placeholder="Phone">
				<textarea name="message" placeholder="Message" class="field"></textarea>
				<button class="btn">Send</button>
                </form> -->
			</div>
		</div>
	</div>

{% endblock %} 

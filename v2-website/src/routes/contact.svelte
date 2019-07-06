<!-- Section -->
<section id="learn-more">
    <header class="major">
        <h2>Contact Us</h2>
    </header>
    <form action="/message" method="post">
        <div class="row gtr-uniform">
            <div class="col-4 col-6-medium col-12-xsmall">
                <input type="text" name="name" id="name" value="" placeholder="Name">
            </div>
            <div class="col-4 col-6-medium col-12-xsmall">
                <input type="email" name="email" id="email" value="" placeholder="Email">
            </div>
             <div class="col-4 col-12-medium">
                <select name="reason" id="reason">
                    <option value="">I am...</option>
                    <option value="member">Looking to join</option>
                    <option value="sponsor">Looking to sponsor</option>
                    <option value="other">Something else</option>
                </select>
            </div>
            <div class="col-12">
                <textarea name="msg" id="message" placeholder="Message..." rows="6"></textarea>
            </div>
            <div class="col-12">
                <ul class="actions">
                    <li><input type="submit" value="Send Message" class="primary"></li>
                    <li><input type="reset" value="Reset"></li>
                </ul>
            </div>
        </div>
    </form>
</section>

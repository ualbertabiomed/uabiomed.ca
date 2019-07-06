<Layout>
    <section>
        <header class="major">
            <h2>Want to sponsor us?</h2>
        </header>
        <p>Contact us here</p>
        <form action="/iamanewsponsor" method="post">
            <div class="row gtr-uniform">
                <div class="col-6 col-12-xsmall">
                    <input type="text" name="name" id="name" value="" placeholder="Name">
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="email" name="email" id="email" value="" placeholder="Email">
                </div>
                <div class="col-12">
                    <textarea name="msg" id="message" placeholder="Send us a message..." rows="6"></textarea>
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
</Layout>

<script>
    import Layout from './layout.svelte'
</script>

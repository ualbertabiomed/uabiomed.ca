<div id="sidebar" class="inactive">
    <a href="#sidebar" class="toggle" on:click={toggleSidebar} >Toggle</a>
    <div class="inner">
        <nav id="menu">
            <header class="major">
                <h2>Menu</h2>
            </header>
            <ul>
                {#each links as link}
                    <li><a href={link.loc}>{link.name}</a></li>
                {/each}
            </ul>
        </nav>
        <footer id="footer">
            <p class="copyright">
                &copy; UAB. All rights reserved.<br>Design: Modified from <a href="https://html5up.net">HTML5 UP</a>.
            </p>
        </footer>
    </div>
</div>

<script>
    const links = [
        { loc: '/', name: 'About us' },
        { loc: '/join', name: 'Join the Group' },
        { loc: '/events', name: 'Events' },
        { loc: '/sponsors', name: 'Sponsor Us' },
        { loc: '/docs', name: 'Club Documents' },
    ]

    const toggleSidebar = (event) => {
        event.preventDefault();
        event.stopPropagation();

        document.getElementById('sidebar').classList.toggle('active')
        document.getElementById('sidebar').classList.toggle('inactive')
    }
</script>

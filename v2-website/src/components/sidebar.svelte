<div id="sidebar" class={sidebarStateString}>
    <a href="#sidebar" class="toggle" on:click={toggleSidebar} >Toggle</a>
    <div class="inner">
        <nav id="menu">
            <header class="major">
                <h2>Menu</h2>
            </header>
            <ul>
                {#each links as link}
                    <li><a on:click={()=>setSidebar(false)} href={link.loc}>{link.name}</a></li>
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
    import { isSidebarEnabled } from '../stores/app.js'

    const links = [
        { loc: '/', name: 'About us' },
        { loc: '/team', name: 'The Team' },
        { loc: '/outreach', name: 'Educational Outreach' },
        { loc: '/contact', name: 'Contact Us' },
        { loc: '/press', name: 'Press' },
    ]

    $: sidebarStateString = $isSidebarEnabled ? 'active' : 'inactive'

    const toggleSidebar = (event) => {
        event.preventDefault()
        isSidebarEnabled.set(!$isSidebarEnabled)
        return false
    }
    const setSidebar = (val) => isSidebarEnabled.set(val)

</script>

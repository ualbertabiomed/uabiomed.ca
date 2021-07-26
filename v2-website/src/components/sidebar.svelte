<div id="sidebar" class={sidebarStateString}>
    <a href="#sidebar" class="toggle" on:click={toggleSidebar} >Toggle</a>
    <div class="inner">
        <nav id="menu">
            <header class="major">
                <h2>Menu</h2>
            </header>
            <ul>
                {#each links as link}
                    {#if link.has_sub === 0}
                        <li><a on:click={()=>setSidebar(false)} href={link.loc}>{link.name}</a></li>
                    {:else}
                        <li>
                            <span class="opener">{link.name}</span>
                            <ul>
                                {#each link.submenu as submenu}
                                    <li><a on:click={()=>setSidebar(false)} href = {submenu.loc}>{submenu.name}</a></li>
                                {/each}
                            </ul>
                        </li>
                    {/if}
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
        { loc: '/', name: 'About us', has_sub: 0, submenu: [] },
        { loc: '/exoskeleton', name: 'ALEX - The Exoskeleton', has_sub: 0, submenu: [] },
        { loc: '/3dwrist', name: '3D Wrist Project', has_sub: 0, submenu: []},
        { loc: '/team', name: 'The Team', has_sub: 0, submenu: [] },
        { loc: '/info', name: 'Why Join a Biomedical Engineering Group? (Non-STEM students)', has_sub: 0, submenu: [] },
        { loc: '/join', name: 'Join the Team', has_sub: 0, submenu: [] },
        { loc: '/press', name: 'Press and Educational Outreach', has_sub: 0, submenu: [] },
        { loc: '/contact', name: 'Contact Us', has_sub: 0, submenu: [] },
        { loc: '/team', name: '(web Testing)', has_sub: 1, 
            submenu: [ { loc: '/3dwrist', name: 'Test 1'} ] }
    ]

    $: sidebarStateString = $isSidebarEnabled ? 'active' : 'inactive'

    const toggleSidebar = (event) => {
        event.preventDefault()
        isSidebarEnabled.set(!$isSidebarEnabled)
        return false
    }
    const setSidebar = (val) => isSidebarEnabled.set(val)

</script>

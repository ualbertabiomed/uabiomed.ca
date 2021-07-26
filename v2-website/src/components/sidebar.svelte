<div id="sidebar" class={sidebarStateString}>
    <a href="#sidebar" class="toggle" on:click={toggleSidebar} >Toggle</a>
    <div class="inner">
        <nav id="menu">
            <header class="major">
                <h2>Menu</h2>
            </header>
            <ul>
                {#each links as link}
                    {#if !link.submenu}
                    <li><a on:click={()=>setSidebar(false)} href={link.loc}>{link.name}</a></li>
                    {:else}
                    <li>
                        <span class="opener">{link.name}</span>
                        <ul>
                            {#each link.options as option}
                                <li><a on:click={()=>setSidebar(false)} href={option.loc}>{option.name}</a></li>
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
        { loc: '/', name: 'About us', submenu: false, options: [] },
        { loc: '/exoskeleton', name: 'ALEX - The Exoskeleton', submenu: false, options: [] },
        { loc: '/3dwrist', name: '3D Wrist Project', submenu: false, options: []},
        { loc: '/team', name: 'The Team', submenu: false, options: [] },
        { loc: '/info', name: 'Why Join a Biomedical Engineering Group? (Non-STEM students)', submenu: false, options: [] },
        { loc: '/join', name: 'Join the Team', submenu: false, options: [] },
        { loc: '/press', name: 'Press and Educational Outreach', submenu: false, options: [] },
        { loc: '/contact', name: 'Contact Us', submenu: false, options: [] },
        { loc: '/', name: '(Web Testing)', submenu: true, 
            options: 
                [ { loc: '/team', name: 'Test 1'} ]}
    ]

    $: sidebarStateString = $isSidebarEnabled ? 'active' : 'inactive'

    const toggleSidebar = (event) => {
        event.preventDefault()
        isSidebarEnabled.set(!$isSidebarEnabled)
        return false
    }
    const setSidebar = (val) => isSidebarEnabled.set(val)

</script>

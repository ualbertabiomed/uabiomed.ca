<div id="sidebar" class={sidebarStateString}>
    <a href="#sidebar" class="toggle" on:click={toggleSidebar} >Toggle</a>
    <div class="inner">
        <nav id="menu">
            <header class="major">
                <h2>Menu</h2>
            </header>
            <ul>
                <!--{#each links as link}
                    <li><a on:click={()=>setSidebar(false)} href={link.loc}>{link.name}</a></li>
                {/each}
                -->
                <li><a on:click={()=>setSidebar(false)} href={'/'}>About Us</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'../routes/exoskeleton.svelte'}>ALEX - The Exoskeleton</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/3dwrist'}>3D Wrist Project</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/team'}>The Team</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/info'}>Why Join a Biomedical Engineering Group? (Non-STEM students)</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/join'}>Join the Team</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/press'}>Press and Educational Outreach</a></li>
                <li><a on:click={()=>setSidebar(false)} href={'/contact'}>Contact Us</a></li>
                <li>
                    <span class="opener">Test Submenu</span>
                    <ul>
                        <li><a on:click={()=>setSidebar(false)} href={'/contact'}>Test 1 (contact)</a></li>
                        <li><a on:click={()=>setSidebar(false)} href={'/team'}>Test 2 (team)</a></li>
                    </ul>
                </li>
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
        { loc: '/', name: 'About us', },
        { loc: '/exoskeleton', name: 'ALEX - The Exoskeleton', },
        { loc: '/3dwrist', name: '3D Wrist Project',},
        { loc: '/team', name: 'The Team', },
        { loc: '/info', name: 'Why Join a Biomedical Engineering Group? (Non-STEM students)', },
        { loc: '/join', name: 'Join the Team', },
        { loc: '/press', name: 'Press and Educational Outreach', },
        { loc: '/contact', name: 'Contact Us', },
    ]

    $: sidebarStateString = $isSidebarEnabled ? 'active' : 'inactive'

    const toggleSidebar = (event) => {
        event.preventDefault()
        isSidebarEnabled.set(!$isSidebarEnabled)
        return false
    }
    const setSidebar = (val) => isSidebarEnabled.set(val)

</script>

<svelte:head>
	<title>UAB</title>
</svelte:head>

<div>
    <div id="wrapper">
        <div id="main" on:click={hideSideBar}>
            <div class="inner">
                <header id="header">
                    <a href="/" class="logo">UAlberta <strong>Biomed</strong></a>
                    <ul class="icons">
                        <li>
                            <a href="https://www.facebook.com/UAlbertaBiomed" class="icon fa-facebook">
                                <span class="label">Facebook</span>
                            </a>
                        </li>
                        <li>
                            <a href="https://www.instagram.com/uabiomed/" class="icon fa-instagram">
                                <span class="label">Instagram</span>
                            </a>
                        </li>
                    </ul>
                </header>
                <slot><!-- Content --></slot>
            </div>
        </div>

        <Sidebar />

    </div>
</div>

<style>
    nav ul li {
        cursor: pointer;
    }
</style>

<script>
    import Sidebar from '../components/sidebar.svelte'
    const hideSideBar = (event) => {
        event.preventDefault();
        event.stopPropagation();

        document.getElementById('sidebar').classList.remove('active')
        document.getElementById('sidebar').classList.add('inactive')
    }
</script>
